from Fortuna import *

from DungeonGenerator.backgrounds import random_background
from DungeonGenerator.cr import CR
from DungeonGenerator.utilities import damage_types, cr_str
from DungeonGenerator.treasure import Loot, get_loot, magic_table_f, magic_table_g, magic_table_h, magic_table_i, no_coin
from DungeonGenerator.monsters_lib import motivation, random_monster, damage_type_cat


class Monster:

    def __init__(self, cr, room_name="Any", name=None):
        self.name = random_monster('monster') if not name else name
        self.cr = CR(cr)
        self.cr_val = self.cr.val
        self.tier = self.cr.tier
        self.cr_key = self.cr.key
        self.total_hp = self.set_hit_points(self.cr_val)
        self.current_hp = self.total_hp
        self.damage = (
            "1d2", "1d2 + 1", "1d2 + 2", "1d2 + 3",
            "1d6 + 8", "1d6 + 14", "1d6 + 20", "1d6 + 26", "1d6 + 32",
            "1d6 + 40", "1d6 + 45", "1d6 + 50", "1d6 + 65", "1d6 + 70",
            "1d8 + 75", "1d8 + 80", "1d8 + 85", "1d8 + 90", "1d8 + 95",
            "1d10 + 100", "1d10 + 105", "1d10 + 110", "1d10 + 115", "1d10 + 120",
            "1d12 + 140", "1d12 + 150", "1d12 + 160", "1d12 + 180", "1d12 + 200",
            "1d20 + 260", "1d20 + 270", "1d20 + 280", "1d20 + 290", "1d20 + 300",
        )[self.cr_key]
        self.xp = self.set_xp_by_cr(self.cr_val)
        self.motive = motivation()
        self.treasure = get_loot(self.cr_val, monster_name=self.name, room_name=room_name, is_villain=False)
        self.prof_bonus = self.set_prof_bonus(self.cr_val)
        variance = plus_or_minus_gauss(3)
        self.ac = self.set_ac(self.cr_val) + variance
        self.att_bonus = self.set_att_bonus(self.cr_val) + -variance
        self.save_dc = self.set_save_dc(self.cr_val)
        self.num_appearing = 1
        self.dam_type = self.find_dam_type()
        self.at_will_dam = f"{smart_clamp(self.cr_val // 3, 1, 10)}d6 + {self.prof_bonus} {self.dam_type}"
        self.rank_by_cr = tuple(x // 5 for x in range(34))
        self.abilities = ["STR", "DEX", "INT", "WIS", "CHA", "CON"]
        self.rank = self.rank_by_cr[self.cr.key]
        self.stats = {
            ability: ability_dice(4) for ability in self.abilities
        }
        self.stat_mod = {}
        self.stat_mod_str = {}
        self.set_stat_mods()
        self.special_damage = f"{self.damage} {damage_types()}"

    def set_stat_mods(self):
        mod_by_stat = (
            -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10
        )
        for ability in self.stats:
            self.stat_mod[ability] = mod_by_stat[smart_clamp(self.stats[ability], 1, 30)]
            if self.stat_mod[ability] > 0:
                self.stat_mod_str[ability] = f"+{self.stat_mod[ability]}"
            else:
                self.stat_mod_str[ability] = f"{self.stat_mod[ability]}"

    def find_dam_type(self):
        dam_type = damage_types()
        for key, val in damage_type_cat.items():
            if any(ele in self.name for ele in val):
                dam_type = key
                break
        if dam_type in ("Physical", "Arcane", "Unholy", "Holy", "Nature", "Divine"):
            dam_type = damage_types(dam_type)
        return dam_type

    @property
    def ability_scores(self):
        return "\n".join(f"  {key} {val} ({self.stat_mod_str[key]})" for key, val in self.stats.items())

    def __lt__(self, other):
        return self.cr_val < other.cr

    def __str__(self):
        self.output = (
            f"Monster: {self.name}, CR {cr_str(self.cr_val)}",
            f"Abilities:\n{self.ability_scores}",
            f"Hit Points: {self.total_hp}",
            f"Armor Class: {self.ac}",
            f"Attack Bonus: {self.att_bonus}",
            f"Basic Attack: {self.at_will_dam}",
            f"Save DC: {self.save_dc}",
            f"XP Value: {self.xp}",
            f"Treasure: {self.treasure}",
            ""
        )
        return '\n'.join(self.output)

    @staticmethod
    def cr_mod(num_players, average_level, difficulty):
        cr_modifier = (-3, -3, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        diff_mod = {'Easy': -1, 'Normal': 0, 'Hard': 1, 'Deadly': 2, 'Insane': 3}
        return average_level + cr_modifier[num_players + diff_mod[difficulty]]

    @staticmethod
    def set_prof_bonus(cr):
        stats_by_cr = (
            2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5,
            5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10
        )
        return stats_by_cr[cr + 3]

    @staticmethod
    def set_ac(cr):
        stats_by_cr = (
            10, 11, 12, 13, 13, 13, 14, 14, 14, 15, 15, 16, 16, 17, 17, 17, 18,
            18, 18, 18, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21, 22,
        )
        return stats_by_cr[cr + 3]

    @staticmethod
    def set_hit_points(cr):
        stats_by_cr = (
            (1, 6), (7, 35), (36, 49), (50, 70), (71, 85), (86, 100),
            (101, 115), (116, 130), (131, 145), (146, 160), (161, 175),
            (176, 190), (191, 205), (206, 220), (221, 235), (236, 250),
            (251, 265), (266, 280), (281, 295), (296, 310), (311, 325),
            (326, 340), (341, 355), (356, 400), (401, 445), (446, 490),
            (491, 535), (536, 580), (581, 625), (626, 670), (671, 715),
            (716, 760), (761, 805), (806, 850), (851, 900)
        )
        return random_range(stats_by_cr[cr + 3][0], stats_by_cr[cr + 3][1] + 1)

    @staticmethod
    def set_att_bonus(cr):
        stats_by_cr = (
            3, 3, 3, 3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8,
            8, 9, 10, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 15
        )
        return stats_by_cr[cr + 3]

    @staticmethod
    def set_damage(cr):
        stats_by_cr = (
            (1, 2), (2, 3), (4, 5), (6, 8),
            (9, 14), (15, 20), (21, 26), (27, 32), (33, 38),
            (39, 44), (45, 50), (51, 56), (57, 62), (63, 68),
            (69, 74), (75, 80), (81, 86), (87, 92), (93, 98),
            (99, 104), (105, 110), (111, 116), (117, 122), (123, 140),
            (141, 158), (159, 176), (177, 194), (195, 212), (213, 230),
            (231, 248), (249, 266), (267, 284), (285, 302), (303, 320), (321, 350)
        )
        return random_range(stats_by_cr[cr + 3][0], stats_by_cr[cr + 3][1] + 1)

    @staticmethod
    def set_save_dc(cr):
        stats_by_cr = (
            13, 13, 13, 13, 13, 13, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 18, 18,
            18, 18, 19, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 24
        )
        return stats_by_cr[cr + 3]

    @staticmethod
    def set_xp_by_cr(cr):
        xp_lookup = (
            10, 25, 50, 100, 200, 450, 700, 1100, 1800, 2300, 2900, 3900, 5000, 5900, 7200, 8400, 10000,
            11500, 13000, 15000, 18000, 20000, 22000, 25000, 33000, 41000, 50000, 62000, 155000, 155000,
            155000, 155000, 155000, 155000, 155000, 155000, 155000, 155000, 155000, 155000
        )
        return xp_lookup[cr + 3]


class MonsterGroup(Monster):
    def __init__(self, cr, room_name="Any", name=None):
        super().__init__(cr, room_name, name)
        self.num_appearing = dice(2, 2)
        self.individual_hp = max(1, int(self.total_hp // self.num_appearing))
        for _ in range(self.num_appearing - 1):
            self.treasure += get_loot(self.cr_val, self.name, room_name)
        self.damage_dice = (
            "1d2", "1d2", "1d2", "1d2",
            "1d6", "1d6", "1d6", "1d6", "1d6",
            "1d6", "1d6", "1d6", "1d6", "1d6",
            "1d8", "1d8", "1d8", "1d8", "1d8",
            "1d10", "1d10", "1d10", "1d10", "1d10",
            "1d12", "1d12", "1d12", "1d12", "1d12",
            "1d20", "1d20", "1d20", "1d20", "1d20"
        )[self.cr_val + 3]
        self.damage_bonus = (
            1, 1, 2, 3,
            8, 14, 20, 26, 32,
            40, 45, 50, 65, 70,
            75, 80, 85, 90, 95,
            100, 105, 110, 115, 120,
            140, 150, 160, 180, 200,
            260, 270, 280, 290, 300
        )[self.cr_val + 3]
        actual_damage_bonus = self.damage_bonus // self.num_appearing
        if actual_damage_bonus > 0:
            self.individual_dam = f"{self.damage_dice} + {actual_damage_bonus}"
        else:
            self.individual_dam = f"{self.damage_dice}"
        self.at_will_dam = f"{smart_clamp(self.cr_val // 4, 1, 5)}d6 + {self.prof_bonus} {self.dam_type}"

    def __str__(self):
        self.output = (
            f"Monster Group: {self.name}, CR {cr_str(self.cr_val)}",
            f"Number Appearing: {self.num_appearing}",
            f"Abilities:\n{self.ability_scores}",
            f"Hit Points: {self.individual_hp} each",
            f"Armor Class: {self.ac}",
            f"Attack Bonus: {self.att_bonus}",
            f"Attack Damage: {self.num_appearing}x ({self.at_will_dam})",
            f"Save DC: {self.save_dc}",
            f"XP Value: {self.xp}",
            f"Treasure: {self.treasure}",
            ""
        )
        return '\n'.join(self.output)


class MinionGroup(Monster):
    def __init__(self, cr, room_name="Any", name=None):
        minion_cr = cr - 3 if cr < 6 else cr // 2
        minion_cr = smart_clamp(minion_cr, -3, 17)
        minion_name = name or random_monster("minion")
        super().__init__(minion_cr, room_name, minion_name)
        self.dam_type = self.find_dam_type()
        self.num_appearing = dice(2, 2)
        self.stats = {
            ability: ability_dice(7) for ability in self.abilities
        }
        self.set_stat_mods()
        self.individual_hp = max(1, int(self.total_hp // self.num_appearing))
        self.treasure = Loot()
        self.damage_dice = (
            "1d2", "1d2", "1d4", "1d4",
            "1d6", "1d6", "1d6", "1d6", "1d6",
            "1d6", "1d6", "1d6", "1d6", "1d6",
            "1d8", "1d8", "1d8", "1d8", "1d8",
            "1d10", "1d10", "1d10", "1d10", "1d10",
            "1d12", "1d12", "1d12", "1d12", "1d12",
            "1d20", "1d20", "1d20", "1d20", "1d20"
        )[minion_cr + 3]
        self.damage_bonus = (
            0, 2, 4, 6,
            8, 14, 20, 26, 32,
            40, 45, 50, 65, 70,
            75, 80, 85, 90, 95,
            100, 105, 110, 115, 120,
            140, 150, 160, 180, 200,
            260, 270, 280, 290, 300
        )[minion_cr + 3]
        actual_damage_bonus = self.damage_bonus // self.num_appearing
        if actual_damage_bonus > 0:
            self.individual_dam = f"{self.damage_dice} + {actual_damage_bonus}"
        else:
            self.individual_dam = f"{self.damage_dice}"
        self.at_will_dam = f"{smart_clamp(self.cr_val // 5, 1, 5)}d4 + {self.prof_bonus} {self.dam_type}"

    def __str__(self):
        self.output = (
            f"Minion Group: {self.name}, CR {cr_str(self.cr_val)}",
            f"Number Appearing: {self.num_appearing}",
            f"Abilities:\n{self.ability_scores}",
            f"Hit Points: {self.individual_hp} each",
            f"Armor Class: {self.ac}",
            f"Attack Bonus: {self.att_bonus}",
            f"Attack Damage: {self.num_appearing}x ({self.at_will_dam})",
            f"Save DC: {self.save_dc}",
            f"XP Value: {self.xp}",
            ""
        )
        return '\n'.join(self.output)


class ItemEncounter(Monster):
    items_by_rank = (
        magic_table_f,
        magic_table_g,
        magic_table_h,
        magic_table_i,
    )

    def __init__(self, cr, room_name="Any", name=""):
        cr_rand = cr + plus_or_minus_linear(2)
        self.cr = smart_clamp(cr_rand + 3 if "legendary" in name.lower() else cr_rand, -3, 30)
        item_rank = smart_clamp(self.cr + 3 // 5, 0, 3)
        self.item_name = self.items_by_rank[item_rank]() if not name else name
        super().__init__(self.cr, room_name, self.item_name)
        self.treasure = Loot()
        self.treasure.magic_items.append(f"Sentient {self.item_name}")

    def __str__(self):
        self.output = (
            f"Animated Item: {self.item_name}, CR {cr_str(self.cr_val)}",
            f"Hit Points: {self.total_hp}",
            f"Armor Class: {self.ac}",
            f"Attack Bonus: {self.att_bonus}",
            f"Attack Damage: {self.at_will_dam}",
            f"XP Value: {self.xp}",
            f"Treasure: {self.treasure}",
            ""
        )
        return "\n".join(self.output)


class Villain(Monster):
    special_abilities = TruffleShuffle((
        "Oracle of War. The villain fights with an unnatural defensive advantage.",
        lambda: f"Diabolic Genius. The villain fights with an unnatural "
        f"offensive advantage for the next {dice(2, 2)} turns.",
        "Shadow Step. Once per round as a bonus action, the villain can instantly teleport up to 30 feet.",
        "Blood Pact. The villain will heal to full health.",
        lambda: f"Whirlwind of {damage_types('Physical')}.",
        "Necromancy. The villain will attempt to raise undead champions to fight the party.",
        lambda: f"Breath Weapon. Cone of {damage_types('Arcane')}.",
        "Stone Gaze. The villain will attempt to turn an opponent in to stone.",
        lambda: f"Horrific Intent. This villain will attempt to cause intense fear, preferring to target casters. "
        f"A horrified victim is paralyzed with fear for up to {dice(3, 3)} rounds. "
        f"While horrified, a victim develops a speech impediment and can do little more than wet themselves. "
        f"The paralysis can be negated if an non-fearful ally takes one full turn to snap them out of it. "
        "Even so, the victim will be fearful and attack with disadvantage until the Horrify duration ends.",
        lambda: f"Puppet Master. The villain will attempt to control an opponent. "
        f"The target's body will obey the master in every way for {dice(2, 2)} turns.",
        lambda: f"Raging Madness. The villain grows bigger and more chaotic for {dice(2, 2)} turns. "
        f"While this ability is active the villain gains +5 Attack Roll bonus and -5 AC penalty.",
        lambda: f"Demonic Metamorphosis. The villain transforms into its true form for {dice(2, 2)} turns. "
        "Demonic Metamorphosis is required for this villain to use its special attack. "
        "With this ability active the villain can make 2 special attacks per turn.",
        "Magical Shield. Immune to one damage type of choice for 3 rounds.",
        lambda: f"Mind Games. A random opponent is forced to solve a mental puzzle and is stunned "
        f"for {dice(2, 2)} rounds. Some say this is like playing a game with God, "
        f"but she's playing chess and you're playing checkers. And still, you have no idea why you keep loosing.",
        "Legendary Resistance. If the villain fails a saving throw, they can choose to succeed instead.",
        "Magic Resistance. The villain has advantage on saving throws against spells and magical effects.",
        "Reflective Carapace. Any time the villain is targeted by a magic missile, or any spell that "
        "requires a ranged attack roll, roll a d6. On a roll of 1 to 5, "
        "the villain is unaffected, and the spell is safely deflected away. "
        "On a roll of 6, the villain is still unaffected, but the spell is reflected back at the caster.",
        lambda: f"Natural Damage Resistances: {', '.join(set(damage_types() for _ in range(3)))}."
    ))
    special_weaknesses = TruffleShuffle((
        lambda: f"Susceptible to {damage_types()} damage.",
        "A hidden object in this room holds the villain's soul.",
        lambda: f"The villain is weakened in the presence of a particular magic item. {magic_table_f()}.",
        "The villain is weakened if the entire party laughs at the villain for a full round.",
        "Weapons found in this dungeon deal double damage when used against this villain.",
        "The villain is weakened if its true name is spoken aloud within the villain's range of hearing.",
        "An unknowable prophecy reveals how the villain can be defeated.",
        "An unsolvable riddle reveals how the villain can be defeated.",
        "The villain falls when an ancient enemy forgives them.",
        "The villain loses its special ability if a mystic bargain it struck long ago is satisfied.",
        "The villain is afraid of magic and has disadvantage on saving throws versus spells.",
        lambda: f"Susceptible to {damage_types()} damage.",
    ))

    def __init__(self, cr, room_name="Any", name=None):
        super().__init__(cr, room_name, name)
        self.name = random_monster("villain") if not name else name
        self.dam_type = self.find_dam_type()
        self.background = random_background()
        self.treasure = get_loot(self.cr_val, monster_name=self.name, room_name=room_name, is_villain=True)
        self.special = self.special_abilities()
        self.weakness = self.special_weaknesses()
        self.at_will_dam = f"{smart_clamp(self.cr_val // 3, 1, 10)}d8 + {self.prof_bonus} {self.dam_type}"
        self.total_specials = 3
        self.stats = {
            ability: ability_dice(6) for ability in self.abilities
        }
        self.stats[random_value(list(self.stats.keys()))] += dice(2, 4)
        for key, val in self.stats.items():
            self.stats[key] = smart_clamp(self.stats[key], 3, 24)
        self.set_stat_mods()
        self.special_damage = f"{self.damage} {damage_types()}"

    def __str__(self):
        self.output = (
            f"Villain: {self.name}, CR {cr_str(self.cr_val)}",
            f"Motivation: {self.motive}",
            f"Background: {self.background}",
            f"Abilities:\n{self.ability_scores}",
            f"Proficiency Bonus: {self.prof_bonus}",
            f"Hit Points: {self.total_hp}",
            f"Armor Class: {self.ac}",
            f"Attack Bonus: {self.att_bonus}",
            f"Number of Attacks: {self.total_specials - 1} basic attacks or 1 special per turn.",
            f"Basic Attack Damage: {self.at_will_dam}",
            f"Special Attack Damage: {self.special_damage}",
            f"Special Ability: {self.special} Usable {self.total_specials} times per day.",
            f"Weakness: {self.weakness}",
            f"Save DC: {self.save_dc}",
            f"XP Value: {self.xp}",
            f"Treasure: {self.treasure}",
            ""
        )
        return '\n'.join(self.output)


class Boss(Villain):
    def __init__(self, cr, room_name="Any", name=None):
        super().__init__(cr, room_name, name=None)
        self.name = random_monster("boss") if not name else name
        self.dam_type = self.find_dam_type()
        while (len(self.treasure) - self.num_potions()) < 3:
            self.treasure += no_coin(get_loot(cr, monster_name=self.name, room_name="Lair", is_villain=True))
        self.total_specials = 5
        if "Legendary" in self.name:
            self.treasure += get_loot(cr, monster_name=self.name, room_name=room_name, is_villain=True)
            second_ability = self.special_abilities()
            while second_ability is self.special:
                second_ability = self.special_abilities()
            self.special += f"\nSpecial Ability: {second_ability}"
        self.at_will_dam = f"{smart_clamp(self.cr_val // 3, 1, 10)}d10 + {self.prof_bonus} {self.dam_type}"
        self.stats = {
            ability: ability_dice(7) for ability in self.abilities
        }
        for _ in range(3):
            self.stats[random_value(list(self.stats.keys()))] += dice(2, 6)
        for key, val in self.stats.items():
            self.stats[key] = smart_clamp(self.stats[key], 3, 30)
        self.set_stat_mods()
        self.special_damage = f"{self.damage} {damage_types()}"

    def num_potions(self):
        return str(self.treasure).count("Potion")

    def __str__(self):
        self.output = (
            f"Boss: {self.name}, CR {cr_str(self.cr_val)}",
            f"Abilities:\n{self.ability_scores}",
            f"Hit Points: {self.total_hp}",
            f"Armor Class: {self.ac}",
            f"Attack Bonus: {self.att_bonus}",
            f"Number of Attacks: {self.total_specials - 1} basic attacks or 1 special per turn.",
            f"Basic Attack: {self.at_will_dam}",
            f"Special Attack: {self.special_damage}",
            f"Special Ability: {self.special}",
            f"Legendary Action. The boss may use one basic attack or move action at the end of every opponent's turn.",
            f"Save DC: {self.save_dc}",
            f"XP Value: {self.xp}",
            f"Treasure: {self.treasure}",
            ""
        )
        return '\n'.join(self.output)


class CampaignBoss(Boss):

    def __init__(self, cr, name=None):
        n = name if name else random_monster("campaign boss")
        super().__init__(cr, name=n)
        while (len(self.treasure) - self.num_potions()) < self.tier:
            self.treasure += no_coin(get_loot(cr, monster_name=self.name, room_name="Lair", is_villain=True))

    def __str__(self):
        self.output = (
            f"Campaign Boss: {self.name}, {self.cr.string}",
            f"Abilities:\n{self.ability_scores}",
            f"Hit Points: {self.total_hp}",
            f"Armor Class: {self.ac}",
            f"Attack Bonus: {self.att_bonus}",
            f"Number of Attacks: {self.total_specials} basic attacks or 1 special per turn.",
            f"Basic Attack: {self.at_will_dam}",
            f"Special Attack: {self.special_damage}",
            f"Special Ability: {self.special}",
            f"Legendary Action. The boss may use one basic attack or move action at the end of every opponent's turn.",
            f"Save DC: {self.save_dc}",
            f"XP Value: {self.xp}",
            f"Treasure: {self.treasure}",
            ""
        )
        return '\n'.join(self.output)

    def __repr__(self):
        return f"Campaign Boss: {self.name}, {self.cr}"


if __name__ == "__main__":
    print()
    print(MinionGroup(5))
    print(Monster(7))
    print(Villain(13))
    print(Boss(17))
    print(CampaignBoss(20))
