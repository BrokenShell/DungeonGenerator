from Fortuna import *
from DungeonGenerator.cr import CR
from DungeonGenerator.monsters import Villain, Monster, ItemEncounter
from DungeonGenerator.npc_lib import npc_dict, random_human
from DungeonGenerator.gear import BasicGear, Potion
from DungeonGenerator.skills import SkillSet
from DungeonGenerator.treasure import get_loot, Loot, career_loot
from DungeonGenerator.player_lib import Player, Fighter, Paladin, Barbarian, Wizard, Sorcerer, Warlock, random_character_class
from DungeonGenerator.player_lib import Cleric, Druid, Bard, Rogue, Ranger, Monk, Knight
from DungeonGenerator.backgrounds import random_background


class Npc:
    professions = TruffleShuffle(npc_dict['professions'])
    races = QuantumMonty(npc_dict['races']).front_linear
    appearances = TruffleShuffle(npc_dict['appearances'])
    talents = TruffleShuffle(npc_dict['talents'])
    mannerisms = TruffleShuffle(npc_dict['mannerisms'])
    traits = TruffleShuffle(npc_dict['traits'])
    bonds = TruffleShuffle(npc_dict['bonds'])
    flaws = TruffleShuffle(npc_dict['flaws'])
    trinkets = TruffleShuffle(npc_dict['trinkets'])
    treasure = Loot()
    save_dc_list = (
        13, 13, 13, 13, 13, 13, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 18, 18,
        18, 18, 19, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 24
    )
    racial_bonuses = {
        "Human": {"STR": 1, 'DEX': 1, 'CON': 1, 'INT': 1, 'WIS': 1, 'CHA': 1},
        "Mountain Dwarf": {"STR": 2, 'CON': 2},
        "Hill Dwarf": {"WIS": 1, 'CON': 2},
        "Shout Halfling": {"DEX": 2, 'CON': 1},
        "Lightfoot Halfling": {"DEX": 2, 'CHA': 1},
        "Forest Gnome": {"INT": 2, 'DEX': 1},
        "Rock Gnome": {"INT": 2, 'CON': 2},
        "High Elf": {"DEX": 2, 'INT': 1},
        "Wood Elf": {"DEX": 2, 'WIS': 1},
        "Half-elf": {"CHA": 2, "DEX": 1, "CON": 1},
        "Drow": {"DEX": 2, 'CHA': 1},
        "Half-orc": {"STR": 2, 'CON': 1},
        "Dragonborn": {"STR": 2, 'CHA': 1},
        "Tiefling": {"CHA": 2, 'INT': 1},
    }

    def __init__(self, cr=1, race=None):
        self.name = "NPC"
        self.damage = 0
        self.cr = smart_clamp(cr, 1, 20)
        self.profession = self.professions()
        self.race = race if race else random_human() if percent_true(50) else self.races()
        self.appearance = self.appearances()
        self.talent = self.talents()
        self.mannerism = self.mannerisms()
        self.trait = self.traits()
        self.bond = self.bonds()
        self.flaw = self.flaws()
        self.trinket = self.trinkets()
        self.save_dc = self.save_dc_list[self.cr + 3]
        self.xp = 0
        self.stats = {}
        self.stat_mod = {}
        self.stat_mod_str = {}
        self._set_stats()
        self._set_racial_bonuses()
        self._set_stat_mods()
        self.background = random_background()
        self.saving_throws = self.set_saves()
        self.health = self._set_health()
        self.ac = 10 + self.stat_mod["DEX"]

    def _set_racial_bonuses(self):
        if self.race in self.racial_bonuses.keys():
            for stat, val in self.racial_bonuses[self.race].items():
                self.stats[stat] += val

    def _set_health(self):
        return smart_clamp(4 + self.stat_mod['CON'], 1, 20)

    def _set_stats(self):
        stats = ('STR', 'INT', 'DEX', 'WIS', 'CON', 'CHA')
        for ability in stats:
            self.stats[ability] = ability_dice(3)

    def _set_stat_mods(self):
        mod_by_stat = (
            -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10
        )
        for ability in self.stats:
            self.stat_mod[ability] = mod_by_stat[smart_clamp(self.stats[ability], 1, 30)]
            if self.stat_mod[ability] > 0:
                self.stat_mod_str[ability] = f"+{self.stat_mod[ability]}"
            else:
                self.stat_mod_str[ability] = f"{self.stat_mod[ability]}"

    def set_saves(self):
        result = []
        for key, val in self.stat_mod.items():
            if val > 0:
                result.append(f"{key} +{val}")
            else:
                result.append(f"{key} {val}")
        return result

    @property
    def ability_scores(self):
        return "\n".join(f"  {key} {val} ({self.stat_mod_str[key]})" for key, val in self.stats.items())

    def __str__(self):
        self.output = (
            f"NPC: {self.profession}",
            f"Race: {self.race}",
            f"Appearance: {self.appearance}",
            f"Mannerism: {self.mannerism}",
            f"Ideal: {self.background.ideal}",
            f"Flaw: {self.background.flaw}",
            f"Hit Points: {self.health}",
            f"Armor Class: {self.ac}",
            ""
        )
        return "\n".join(self.output)


class QuestGiver(Npc):
    random_quest = TruffleShuffle(npc_dict['quests'])
    skill_list = TruffleShuffle((
        "Acrobatics DEX",
        "Animal handling WIS",
        "Arcana INT",
        "Athletics STR",
        "Deception CHA",
        "History INT",
        "Insight WIS",
        "Intimidation CHA",
        "Investigation INT",
        "Medicine WIS",
        "Nature INT",
        "Perception WIS",
        "Performance CHA",
        "Persuasion CHA",
        "Religion INT",
        "Sleight of hand DEX",
        "Stealth DEX",
        "Survival WIS"
    ))

    def __init__(self, cr, race=None):
        super().__init__(cr, race)
        self.quest = self.random_quest()
        self.magic_item = ItemEncounter(cr).item_name
        self.coinage = get_loot(min(30, self.cr + 5))
        self.skill = self.skill_list()
        self.chest = get_loot(max(-3, self.cr - 15), is_villain=True)

    def __str__(self):
        self.output = (
            f"NPC: Quest Giver",
            f"Race: {self.race}",
            f"Appearance: {self.appearance}",
            f"Mannerism: {self.mannerism}",
            f"Ideal: {self.background.ideal}",
            f"Quest: {self.quest}",
            f"Required PC Skill: {self.skill} {self.save_dc}",
            f"Quest Rewards: (choose one below)",
            f"1. Mysterious magic item: {self.magic_item}",
            f"2. Fat bag of coins: {self.coinage}",
            f"3. Gem encrusted treasure chest: {self.chest}",
            ""
        )
        return "\n".join(self.output)


class ShopKeeper(Npc):
    def __init__(self, cr, race=None):
        super().__init__(cr, race)
        self.profession = 'Shop Keeper'
        if cr <= 5:
            self.for_sale = [BasicGear(cr) for _ in range(dice(2, 4))]
        elif cr <= 10:
            self.for_sale = [BasicGear(cr - 4) for _ in range(d(4))]
            self.for_sale.extend([BasicGear(cr) for _ in range(dice(2, 4))])
        elif cr <= 15:
            self.for_sale = [BasicGear(cr - 8) for _ in range(d(4))]
            self.for_sale.extend([BasicGear(cr - 4) for _ in range(d(4))])
            self.for_sale.extend([BasicGear(cr) for _ in range(dice(2, 4))])
        else:
            self.for_sale = [BasicGear(cr - 12) for _ in range(d(4))]
            self.for_sale.extend([BasicGear(cr - 8) for _ in range(d(4))])
            self.for_sale.extend([BasicGear(cr - 4) for _ in range(d(4))])
            self.for_sale.extend([BasicGear(cr) for _ in range(dice(2, 4))])
        self.trinket_price = f"{BasicGear(5).price}"
        self.for_sale_names = [f"{val.name} ({val.id})" for val in self.for_sale]

    def __str__(self):
        self.output = (
            f"NPC: {self.profession}",
            f"Race: {self.race}",
            f"Appearance: {self.appearance}",
            f"Mannerism: {self.mannerism}",
            f"Bond: {self.background.bond}",
            f"Inspect Merchandise INT: DC {self.save_dc}",
            f"For Sale: " + "; ".join(self.for_sale_names) +
            f"; Trinket: {self.trinket}, Price {self.trinket_price}",
            ""
        )
        return "\n".join(self.output)


class PotionDealer(Npc):
    def __init__(self, cr, race=None):
        super().__init__(cr, race)
        self.profession = 'Potion Dealer'
        self.for_sale = sorted([f"{Potion(cr)}" for _ in range(dice(3, 4))])

    def __str__(self):
        self.output = (
            f"NPC: {self.profession}",
            f"Race: {self.race}",
            f"Appearance: {self.appearance}",
            f"Mannerism: {self.mannerism}",
            f"Bond: {self.background.bond}",
            f"Inspect Merchandise INT: DC {self.save_dc}",
            f"For Sale: " + "; ".join(self.for_sale),
            ""
        )
        return "\n".join(self.output)


class Mercenary(Npc):
    pc_classes = CumulativeWeightedChoice((
        (20, Fighter),
        (40, Cleric),
        (60, Rogue),
        (70, Bard),
        (80, Ranger),
        (90, Barbarian),
        (100, Wizard),
    ), flat=False)

    def __init__(self, cr, race=None, pc_class=None):
        super().__init__(cr, race)
        self.profession = "Mercenary"
        if pc_class is None:
            self.npc_class = self.pc_classes()
        else:
            self.npc_class = pc_class
        self.level = smart_clamp(cr - 1, 1, 20)
        self.player = Player(self.npc_class, self.level)
        self.stats = self.player.stats
        self.stat_mod = self.player.stat_mod
        self.fav_stat_mod = self.stat_mod[self.npc_class.fav_stat]
        self.magic_bonus = self.player.magic_bonus
        x = self.player.level
        y = self.class_price_multi(self.player.cls.name)
        z = self.fav_stat_mod + self.magic_bonus
        self.price = smart_clamp(x * y * z, x, 99999)
        self.name = f"NPC {self.player.cls.name}"
        self.damage_bonus = self.stat_mod[self.npc_class.fav_stat] + self.player.magic_bonus
        self.damage_type = self.player.damage_type
        self.special_dam_type = self.player.cls.damage_type
        self.damage_formula = self.player.damage_formula
        self.special_dam = f"{Monster(self.level).damage}"
        self.skills = SkillSet(self.level, self.player.prof_bonus, self.stats, self.background)
        self.inventory = Loot()
        while len(self.inventory.magic_items) < CR(self.cr).tier:
            self.inventory.magic_items = career_loot(1, self.level - 1, self.level).magic_items
        if len(self.inventory.magic_items) > self.level:
            self.inventory.magic_items = self.inventory.magic_items[:self.level]
        self.treasure = Loot()

    @staticmethod
    def class_price_multi(class_name):
        output = {
            "Monk": 1,
            "Barbarian": 2,
            "Fighter": 3,
            "Rogue": 4,
            "Bard": 5,
            "Druid": 6,
            "Ranger": 7,
            "Warlock": 8,
            "Sorcerer": 9,
            "Paladin": 10,
            "Cleric": 11,
            "Wizard": 12,
            "Artificer": 13,
            "Knight": 14,
        }
        for key in output:
            if key in class_name:
                return output[key]

    def find_skills(self):
        skills = set(self.background.skills)
        for ability in self.stats:
            if self.stat_mod[ability] > 0 and percent_true(self.stat_mod[ability] * 20):
                skills.add(f"{random_value(npc_dict['skills'][ability])}")
        return list(skills)

    def __str__(self):
        coinage = ["Copper", "Silver", "Electrum", "Gold", "Platinum"]
        price_dom = coinage[smart_clamp(round(self.player.level / 5), 0, 4)]
        self.output = (
            f"NPC: {self.profession}",
            f"Salary: {self.price} {price_dom}",
            f"Class: {self.player.cls.name}",
            f"Level: {self.player.level}",
            f"Race: {self.race}",
            f"Appearance: {self.appearance}",
            f"Background: {self.background}",
            f"Abilities:\n{self.player.ability_scores}",
            f"Proficiency Bonus: {self.player.prof_bonus_str}",
            f"Preferred Weapon: {self.player.cls.pref_weapon}",
            f"Hit Points: {self.player.health}",
            f"Armor Class: {self.player.ac}",
            f"Attack Bonus: {self.player.att_bonus}",
            f"Attack Damage: {self.damage_formula} {self.damage_type}",
            f"Special Attack: {self.special_dam} {self.special_dam_type}",
            f"Save DC: {self.player.save_dc}",
            f"Save Proficiencies: {', '.join(self.player.saves)}",
            f"Save Modifiers: {', '.join(self.player.saving_throws)}",
            f"Skills: {self.skills}",
            f"Talent: {self.talent}",
            f"Inventory: {self.inventory}",
            ""
        )
        return "\n".join(self.output)


class Adventurer(Mercenary):
    goals = TruffleShuffle(npc_dict['quests'])
    pc_classes = CumulativeWeightedChoice((
        (30, Knight),
        (40, Paladin),
        (50, Druid),
        (60, Monk),
        (80, Ranger),
        (90, Barbarian),
        (95, Sorcerer),
        (100, Warlock),
    ), flat=False)

    def __init__(self, cr, race=None, pc_class=None):
        pcc = random_character_class() if not pc_class else pc_class
        super().__init__(cr + 1, race, pcc)
        self.goal = self.goals()

    def __str__(self):
        self.output = (
            f"NPC: Adventurer",
            f"Class: {self.player.cls.name}",
            f"Level: {self.player.level}",
            f"Race: {self.race}",
            f"Appearance: {self.appearance}",
            f"Background: {self.background}",
            f"Abilities:\n{self.player.ability_scores}",
            f"Proficiency Bonus: {self.player.prof_bonus_str}",
            f"Preferred Weapon: {self.player.cls.pref_weapon}",
            f"Hit Points: {self.player.health}",
            f"Armor Class: {self.player.ac}",
            f"Attack Bonus: {self.player.att_bonus}",
            f"Attack Damage: {self.damage_formula} {self.damage_type}",
            f"Special Attack: {self.special_dam} {self.special_dam_type}",
            f"Save DC: {self.player.save_dc}",
            f"Save Proficiencies: {', '.join(self.player.saves)}",
            f"Save Modifiers: {', '.join(self.player.saving_throws)}",
            f"Skills: {self.skills}",
            f"Talent: {self.talent}",
            f"Personal Goal: {self.goal}",
            f"Inventory: {self.inventory}",
            ""
        )
        return "\n".join(self.output)


class VillainNPC(Adventurer):

    def __init__(self, cr, race=None, pc_class=None):
        super().__init__(cr, race, pc_class)
        self.name = f"Villain disguised as a {self.professions()}"
        self.treasure = get_loot(self.level, is_villain=True)
        self.xp = Villain(self.cr).xp

    def __str__(self):
        self.output = (
            f"NPC: {self.name}",
            f"Class: {self.player.cls.name}",
            f"Level: {self.player.level}",
            f"Race: {self.race}",
            f"Appearance: {self.appearance}",
            f"Mannerism: {self.mannerism}",
            f"Background: {self.background}",
            f"Abilities:\n{self.player.ability_scores}",
            f"Proficiency Bonus: {self.player.prof_bonus_str}",
            f"Preferred Weapon: {self.player.cls.pref_weapon}",
            f"Hit Points: {self.player.health}",
            f"Armor Class: {self.player.ac}",
            f"Attack Bonus: {self.player.att_bonus}",
            f"Attack Damage: {self.damage_formula} {self.damage_type}",
            f"Special Attack: {self.special_dam} {self.special_dam_type}",
            f"Save DC: {self.player.save_dc}",
            f"Save Proficiencies: {', '.join(self.player.saves)}",
            f"Save Modifiers: {', '.join(self.player.saving_throws)}",
            f"Skills: {self.skills}",
            f"Talent: {self.talent}",
            f"XP Value: {self.xp}",
            f"Inventory: {self.treasure}",
            ""
        )
        return "\n".join(self.output)


class Farmer(Npc):
    professions = TruffleShuffle(npc_dict['farm_professions'])


city_npc = RelativeWeightedChoice((
    (10, Npc),
    (7, Farmer),
    (5, Mercenary),
    (4, QuestGiver),
    (3, PotionDealer),
    (2, ShopKeeper),
    (1, VillainNPC),
))


def random_city_npc(cr=1, room_name="Any"):
    _ = room_name
    return city_npc(cr)


dungeon_npc = RelativeWeightedChoice((
    (10, Npc),
    (5, PotionDealer),
    (2, ShopKeeper),
    (1, Adventurer),
))


def random_dungeon_npc(cr=1, room_name="Any"):
    _ = room_name
    return dungeon_npc(cr)


random_npc = RelativeWeightedChoice((
    (6, Npc),
    (5, Farmer),
    (4, Mercenary),
    (3, QuestGiver),
    (2, PotionDealer),
    (2, ShopKeeper),
    (1, VillainNPC),
    (1, Adventurer),
))

if __name__ == "__main__":
    print(PotionDealer(1))
    print(ShopKeeper(1))
