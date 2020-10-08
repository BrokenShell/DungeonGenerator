from Fortuna import *

from DungeonGenerator.backgrounds import random_background
from DungeonGenerator.gear_lib import *
from DungeonGenerator.monsters_lib import damage_type_cat
from DungeonGenerator.treasure import Loot, get_loot, magic_table_by_cr
from DungeonGenerator.utilities import damage_types


class Base:
    damage_dice = 8

    def damage_str(self, num_dam_dice, bonus):
        return f"{num_dam_dice}d{self.damage_dice} + {bonus}"

    def damage(self, num_dam_dice, bonus):
        return dice(num_dam_dice, self.damage_dice) + bonus


class Apprentice(Base):
    hd = 4
    stats = {
        'STR': ability_dice(3),
        'DEX': ability_dice(3),
        'CON': ability_dice(3),
        'INT': ability_dice(3),
        'WIS': ability_dice(3),
        'CHA': ability_dice(3),
    }
    random_ability = TruffleShuffle(set(stats.keys()))
    fav_stat = max(stats)
    sec_stat = "CON"
    armor_ac = 10
    max_ac_dex = 4
    random_sub_class = TruffleShuffle((
        "Acolyte",
        "Scribe",
        "Squire",
        "Cultist",
        "Neophyte",
    ))

    def __init__(self):
        self.save_prof = {self.fav_stat, self.random_ability()}
        self.sub_class = self.random_sub_class()
        self.name = f"Apprentice, {self.sub_class}"
        self.damage_type = f"{damage_types('Physical')}"
        self.pref_weapon = villager_weapons()


class Barbarian(Base):
    hd = 12
    fav_stat = 'STR'
    sec_stat = 'DEX'
    primary_att = 'Melee Weapon'
    armor_ac = 10
    max_ac_dex = 4
    random_sub_class = TruffleShuffle((
        "Berserker",
        TruffleShuffle(("Bear Totem", "Eagle Totem", "Wolf Totem")),
        "Ancestral Guardian",
        "Storm Herald",
        "Zealot",
    ))
    stats = {'STR': 15, 'DEX': 13, 'CON': 14, 'INT': 8, 'WIS': 12, 'CHA': 10}
    save_prof = ('STR', 'CON')

    def __init__(self):
        self.pref_weapon = two_hand_weapons()
        self.sub_class = self.random_sub_class()
        self.name = f"Barbarian, Path of the {self.sub_class}"
        if self.sub_class == "Storm Herald":
            self.damage_type = f"{damage_types('Physical')} or lightning"
        if self.sub_class == "Ancestral Guardian" or self.sub_class == "Zealot":
            self.damage_type = f"{damage_types('Physical')} and holy fire"
        else:
            self.damage_type = f"{damage_types('Physical')}"


class Bard(Base):
    hd = 8
    fav_stat = 'CHA'
    sec_stat = 'DEX'
    primary_att = 'Charm'
    armor_ac = 12
    max_ac_dex = 4
    random_sub_class = TruffleShuffle((
        "Lore",
        "Valor",
        "Glamour",
        "Swords",
        "Whispers",
    ))
    stats = {'STR': 8, 'DEX': 14, 'CON': 13, 'INT': 10, 'WIS': 12, 'CHA': 15}
    save_prof = ('DEX', 'CHA')

    def __init__(self):
        self.sub_class = self.random_sub_class()
        self.name = f"Bard, College of {self.sub_class}"
        if self.sub_class == "Valor":
            self.damage_type = f"{damage_types('Physical')}"
            self.pref_weapon = main_hand_weapons()
        if self.sub_class == "Swords":
            self.damage_type = f"{damage_types('Physical')}"
            self.pref_weapon = "Longsword" if percent_true(50) else "Rapier"
        else:
            self.damage_type = f"{damage_types('Arcane')}"
            self.pref_weapon = caster_weapons()


class Cleric(Base):
    hd = 8
    name = 'Cleric'
    fav_stat = 'WIS'
    sec_stat = 'STR'
    primary_att = 'Spell'
    armor_ac = 15
    max_ac_dex = 2
    random_sub_class = TruffleShuffle((
        "Knowledge",
        "Life",
        "Light",
        "Nature",
        "Tempest",
        "Trickery",
        "War",
        "Forge",
        "Grave",
        "Death",
    ))
    stats = {'STR': 8, 'DEX': 12, 'CON': 14, 'INT': 10, 'WIS': 15, 'CHA': 13}
    save_prof = ('WIS', 'CHA')

    def __init__(self):
        self.sub_class = self.random_sub_class()
        self.name = f"Cleric, {self.sub_class} Domain"
        if self.sub_class == "War" or self.sub_class == "Forge":
            self.damage_type = f"{damage_types('Physical')} and {damage_types('Holy')}"
            self.pref_weapon = f"{off_hand_shield()} and {main_hand_weapons()}"
        elif self.sub_class == "Nature" or self.sub_class == "Tempest":
            self.damage_type = damage_types('Nature')
            self.pref_weapon = caster_weapons()
        elif self.sub_class == "Death" or self.sub_class == "Grave":
            self.damage_type = damage_types('Unholy')
            self.pref_weapon = caster_weapons()
        elif self.sub_class == "Light" or self.sub_class == "Life":
            self.damage_type = damage_types('Holy')
            self.pref_weapon = caster_weapons() if percent_true(75) else villager_weapons()
        else:
            self.damage_type = f"{damage_types('Divine')}"
            self.pref_weapon = f"{off_hand_weapons()} and {off_hand_shield()}"


class Druid(Base):
    hd = 8
    fav_stat = 'WIS'
    sec_stat = 'DEX'
    primary_att = 'Nature Spell'
    armor_ac = 15
    max_ac_dex = 2
    random_sub_class = TruffleShuffle((
        "the Land",
        "the Moon",
        "Dreams",
        "the Shepherd",
        "Spores",
    ))
    stats = {'STR': 13, 'DEX': 8, 'CON': 14, 'INT': 10, 'WIS': 15, 'CHA': 12}
    save_prof = ('INT', 'WIS')

    def __init__(self):
        self.pref_weapon = caster_weapons() if percent_true(75) else villager_weapons()
        self.sub_class = self.random_sub_class()
        self.name = f"Druid, Circle of {self.sub_class}"
        self.damage_type = "poison" if self.sub_class == "Spores" else damage_types("Nature")


class Fighter(Base):
    hd = 10
    fav_stat = 'STR'
    sec_stat = 'DEX'
    primary_att = 'Weapon'
    armor_ac = 15
    max_ac_dex = 2
    random_sub_class = TruffleShuffle((
        "Champion",
        "Battle Master",
        "Eldritch Knight",
        "Arcane Archer",
        "Cavalier",
        "Samurai",
        "Gladiator",
    ))
    stats = {'STR': 15, 'DEX': 13, 'CON': 14, 'INT': 8, 'WIS': 12, 'CHA': 10}
    save_prof = ('STR', 'CON')
    weapon_options = TruffleShuffle((
        lambda: f"{two_hand_weapons()}",
        lambda: f"{off_hand_shield()} and {versatile_weapons()}",
        lambda: f"{off_hand_shield()} and {main_hand_weapons()}",
        lambda: f"{off_hand_weapons()} and {main_hand_weapons()}",
        lambda: f"{off_hand_weapons()} and {off_hand_shield()}",
        lambda: f"{off_hand_weapons()} and {off_hand_weapons()}",
        lambda: f"Matched pair of {off_hand_weapons()}s",
    ))

    def __init__(self):
        self.sub_class = self.random_sub_class()
        self.name = f"Fighter, {self.sub_class}"
        if self.sub_class == "Eldritch Knight":
            self.damage_type = f"{damage_types('Physical')} and {damage_types('Arcane')}"
            self.pref_weapon = main_hand_weapons()
        elif self.sub_class == "Arcane Archer":
            self.damage_type = f"{damage_types('Physical')} and {damage_types('Arcane')}"
            self.pref_weapon = bow_weapons()
        elif self.sub_class == "Cavalier":
            self.damage_type = f"{damage_types('Physical')}"
            self.pref_weapon = pole_weapons()
        elif self.stats['DEX'] > self.stats['STR']:
            self.pref_weapon = thrown_weapons() if percent_true(50) else f"Dual Wield {off_hand_weapons()}s"
        else:
            self.damage_type = f"{damage_types('Physical')}"
            self.pref_weapon = self.weapon_options() if self.stats['STR'] > self.stats['DEX'] else thrown_weapons()


class Knight(Base):
    hd = 12
    fav_stat = 'STR'
    sec_stat = 'CON'
    primary_att = 'Polearm Weapon'
    armor_ac = 18
    max_ac_dex = 0
    random_sub_class = TruffleShuffle((
        "Flaming Tongue",
        "Frozen Wasteland",
        "Hidden Rose",
        "Storm",
        "Physical Shadow",
        "Broken Lance",
    ))
    stats = {'STR': 15, 'DEX': 14, 'CON': 13, 'INT': 12, 'WIS': 10, 'CHA': 8}
    save_prof = ('STR', 'CON')

    def __init__(self):
        self.pref_weapon = pole_weapons()
        self.sub_class = self.random_sub_class()
        self.name = f"Knight of the {self.sub_class}"
        self.damage_type = damage_types('Physical')


class Monk(Base):
    hd = 8
    fav_stat = 'DEX'
    sec_stat = 'WIS'
    primary_att = 'Unarmed Combat'
    armor_ac = 10
    max_ac_dex = 10
    random_sub_class = TruffleShuffle((
        "Open Hand",
        "Four Elements",
        "Shadow",
        "Drunken Master",
        "Kensei",
        "Sun Soul",
    ))
    stats = {'STR': 10, 'DEX': 15, 'CON': 14, 'INT': 8, 'WIS': 13, 'CHA': 12}
    save_prof = ('STR', 'DEX')
    monk_weapon = QuantumMonty(("Unarmed", "Fist Weapon", villager_weapons, off_hand_weapons)).front_linear

    def __init__(self):
        self.pref_weapon = self.monk_weapon()
        self.sub_class = self.random_sub_class()
        self.name = f"Monk, Way of the {self.sub_class}"
        if self.sub_class == "Four Elements":
            self.damage_type = f"{damage_types('Physical')} and {damage_types('Arcane')}"
        elif self.sub_class == "Shadow":
            self.damage_type = f"{damage_types('Physical')} and shadow"
        else:
            self.damage_type = f"{damage_types('Physical')}"


class Paladin(Base):
    hd = 10
    fav_stat = 'STR'
    sec_stat = 'CHA'
    primary_att = 'Melee Weapon or Divine Spell'
    armor_ac = 18
    max_ac_dex = 0
    random_sub_class = TruffleShuffle((
        "Oath of Devotion",
        "Oath of the Ancients",
        "Oath of Vengeance",
        "Oath of Conquest",
        "Oath of Redemption",
        "Oath of Glory",
        "Oath of Honor",
        "Oathbreaker",
    ))
    stats = {'STR': 15, 'DEX': 12, 'CON': 13, 'INT': 8, 'WIS': 10, 'CHA': 14}
    save_prof = ('STR', 'CHA')
    weapon_options = CumulativeWeightedChoice((
        (50, lambda: f"{pole_weapons()}"),
        (60, lambda: f"{versatile_weapons()} and {off_hand_shield()}"),
        (70, lambda: f"{two_hand_weapons()}"),
    ))

    def __init__(self):
        self.pref_weapon = self.weapon_options()
        self.sub_class = self.random_sub_class()
        self.name = f"Paladin, {self.sub_class}"
        self.damage_type = f"{damage_types('Physical')} and holy fire"


class Ranger(Base):
    hd = 8
    fav_stat = 'DEX'
    sec_stat = 'WIS'
    primary_att = 'Ranged Weapon'
    armor_ac = 12
    max_ac_dex = 10
    random_sub_class = TruffleShuffle((
        "Archer",
        "Hunter",
        "Beast Master",
        "Gloom Stalker",
        "Horizon Walker",
        "Monster Slayer",
    ))
    stats = {'STR': 8, 'DEX': 15, 'CON': 13, 'INT': 10, 'WIS': 14, 'CHA': 12}
    save_prof = ('DEX', 'WIS')
    weapon_options = QuantumMonty((
        lambda: f"{bow_weapons()}",
        lambda: f"{off_hand_weapons()} and {main_hand_weapons()}",
        lambda: f"{off_hand_weapons()} and {versatile_weapons()}",
        lambda: f"{thrown_weapons()} and {off_hand_weapons()}",
        lambda: f"Matched pair of {off_hand_weapons()}s",
        lambda: f"{two_hand_weapons()}",
    )).front_linear

    def __init__(self):
        self.sub_class = self.random_sub_class()
        self.name = f"Ranger, {self.sub_class}"
        if self.sub_class == "Archer":
            self.pref_weapon = bow_weapons()
        self.pref_weapon = self.weapon_options()
        self.damage_type = "piercing"


class Rogue(Base):
    hd = 8
    fav_stat = 'DEX'
    sec_stat = 'INT'
    primary_att = 'Light Weapon'
    armor_ac = 12
    max_ac_dex = 10
    random_sub_class = TruffleShuffle((
        "Thief",
        "Assassin",
        "Arcane Trickster",
        "Inquisitive",
        "Mastermind",
        "Scout",
        "Swashbuckler",
        "Acrobat",
    ))
    stats = {'STR': 8, 'DEX': 15, 'CON': 14, 'INT': 13, 'WIS': 12, 'CHA': 10}
    save_prof = ('DEX', 'INT')
    weapon_options = TruffleShuffle((
        lambda: f"Matched pair of {off_hand_weapons()}s",
        lambda: f"{off_hand_weapons()} and {main_hand_weapons()}",
        lambda: f"{off_hand_weapons()} and {off_hand_weapons()}",
        lambda: f"{thrown_weapons()}",
    ))

    def __init__(self):
        self.sub_class = self.random_sub_class()
        self.name = f"Rogue, {self.sub_class}"
        if self.sub_class == "Arcane Trickster":
            self.damage_type = f"{damage_types('Physical')} or {damage_types('Arcane')}"
            self.pref_weapon = off_hand_weapons() if percent_true(50) else bow_weapons()
        else:
            self.damage_type = f"{damage_types('Physical')}"
            self.pref_weapon = self.weapon_options()


class Sorcerer(Base):
    hd = 6
    name = 'Sorcerer'
    fav_stat = 'CHA'
    sec_stat = 'DEX'
    primary_att = 'Elemental Spell'
    armor_ac = 10
    max_ac_dex = 4
    random_sub_class = TruffleShuffle((
        "Fey Bloodline",
        "Dragonkin Bloodline",
        "Devilkin Bloodline",
        "Wild Magic",
        "Divine Soul",
        "Shadow Magic",
        "Storm Sorcery",
    ))
    stats = {'STR': 8, 'DEX': 14, 'CON': 13, 'INT': 12, 'WIS': 10, 'CHA': 15}
    save_prof = ('CHA', 'CON')

    def __init__(self):
        self.pref_weapon = caster_weapons() if percent_true(75) else villager_weapons()
        self.sub_class = self.random_sub_class()
        self.name = f"Sorcerer, {self.sub_class}"
        if self.sub_class == "Divine Soul":
            self.damage_type = f"{damage_types('Divine')}"
        if self.sub_class == "Shadow Magic":
            self.damage_type = "shadow"
        if self.sub_class == "Storm Sorcery":
            self.damage_type = "lightning"
        else:
            self.damage_type = f"{damage_types('Arcane')}"


class Warlock(Base):
    hd = 8
    fav_stat = 'CHA'
    sec_stat = 'DEX'
    primary_att = 'Demonic Spell'
    armor_ac = 12
    max_ac_dex = 4
    random_sub_class = TruffleShuffle((
        "Archfey",
        "Fiend",
        "Great Old One",
        "Celestial",
        "Hexblade",
    ))
    random_pact = TruffleShuffle(('Chain', 'Blade', 'Tome'))
    stats = {'STR': 8, 'DEX': 14, 'CON': 13, 'INT': 10, 'WIS': 12, 'CHA': 15}
    save_prof = ('CHA', 'WIS')

    def __init__(self):
        self.sub_class = self.random_sub_class()
        self.pact = self.random_pact()
        self.name = f"Warlock, {self.sub_class} Pact of the {self.pact}"
        if self.sub_class == "Celestial":
            self.damage_type = damage_types('Holy')
            self.pref_weapon = caster_weapons() if percent_true(75) else villager_weapons()
        else:
            self.damage_type = f"{damage_types('Arcane')}"
            self.pref_weapon = main_hand_weapons()
            if self.pact == "Blade":
                self.pref_weapon = "Longsword"
                self.damage_type += " and slashing"
            elif self.pact == "Tome":
                self.pref_weapon = "Iron Bound Tome"
                self.damage_type += " and bludgeoning"


class Wizard(Base):
    hd = 6
    name = 'Wizard'
    fav_stat = 'INT'
    sec_stat = 'DEX'
    primary_att = 'Arcane Spell'
    armor_ac = 10
    max_ac_dex = 4
    random_sub_class = TruffleShuffle((
        "Abjuration",
        "Conjuration",
        "Divination",
        "Enchantment",
        "Evocation",
        "Illusion",
        "Necromancy",
        "Transmutation",
    ))
    stats = {'STR': 8, 'DEX': 14, 'CON': 13, 'INT': 15, 'WIS': 12, 'CHA': 10}
    save_prof = ('INT', 'WIS')

    def __init__(self):
        self.pref_weapon = caster_weapons() if percent_true(75) else villager_weapons()
        self.sub_class = self.random_sub_class()
        self.name = f"Wizard, School of {self.sub_class}"
        self.damage_type = f"{damage_types('Arcane')}"


class Player:
    random_race = TruffleShuffle((
        "Human", "Mountain Dwarf", "Hill Dwarf", "Shout Halfling", "Lightfoot Halfling",
        "Forest Gnome", "Rock Gnome", "High Elf", "Wood Elf", "Half-elf", "Drow", "Half-orc",
        "Dragonborn", "Tiefling",
    ))
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

    def __init__(self, cls=None, level=0, race=None, point_buy=False):
        if not cls:
            self.cls = random_character_class()() if level > 0 else Apprentice()
        else:
            self.cls = cls() if level > 0 else Apprentice()
        self.level = smart_clamp(level, 0, 20)
        self.race = self.random_race() if not race else race
        self.health = 0
        self.xp = 0
        self.ac = 10
        self.prof_bonus = 0
        self.magic_bonus = 0
        self.save_dc = 0
        self.att_bonus = 0
        self.stats = dict(self.cls.stats) if point_buy else self.set_random_stats()
        self.set_racial_bonuses()
        self.stat_mod = {}
        self.stat_mod_str = {}
        self.set_stat_mods()
        self.set_ac()
        self.set_xp()
        self.set_health()
        self.prof_bonus_str = ""
        self.set_prof()
        self.set_save_dc()
        self.set_att_bonus()
        self.saves = list(self.cls.save_prof)
        self.saving_throws = self.set_saves()
        self.background = random_background()
        self.loot = Loot()
        dam_mod = smart_clamp(self.level // 4, 1, 4)
        dam_bonus = self.stat_mod[self.cls.fav_stat] + self.magic_bonus
        self.average_damage = (dam_mod * (self.cls.damage_dice // 2)) + dam_bonus
        self.damage_formula = f"{dam_mod}d10 + {dam_bonus}"
        self.special_damage_formula = f"{smart_clamp(self.level // 2, 1, 10)}d8 + {10 + dam_bonus}"
        self.damage_type = self.find_dam_type()
        self.special_damage_type = self.cls.damage_type
        self.loot = get_loot(self.level)
        self.treasures = set()
        if self.level > 0:
            for _ in range(smart_clamp(self.level - 5, 1, 10)):
                if percent_true(1):
                    self.treasures.add(magic_table_by_cr(self.level + 10))
                elif percent_true(50):
                    self.treasures.add(magic_table_by_cr(self.level))
                elif len(self.treasures) < 1:
                    self.treasures.add(magic_table_by_cr(self.level - 10))

    def find_dam_type(self):
        dam_type = damage_types()
        for key, val in damage_type_cat.items():
            if any(ele in self.cls.pref_weapon for ele in val):
                dam_type = key
                break
        if dam_type in ("Physical", "Arcane", "Divine"):
            dam_type = damage_types(dam_type)
        return dam_type

    def set_saves(self):
        result = []
        for key, val in self.stat_mod.items():
            if key in self.cls.save_prof:
                if val + self.prof_bonus > 0:
                    result.append(f"{key} +{val + self.prof_bonus}")
                else:
                    result.append(f"{key} {val + self.prof_bonus}")
            else:
                if val > 0:
                    result.append(f"{key} +{val}")
                else:
                    result.append(f"{key} {val}")
        return result

    def set_magic(self):
        return smart_clamp(self.prof_bonus - 2 + plus_or_minus_linear(1), 0, 3) if self.level > 1 else 0

    def evaluate(self):
        return (self.level * 10) + self.att_bonus

    def __lt__(self, other):
        return self.evaluate() < other.evaluate()

    @property
    def ability_scores(self):
        return "\n".join(f"  {key} {val} ({self.stat_mod_str[key]})" for key, val in self.stats.items())

    def __repr__(self):
        n_items = len(self.treasures)
        gear = '\n  ' + f"\n  ".join(self.treasures) if n_items > 1 else list(self.treasures)[0] if n_items == 1 else 'None'
        output = (
            f"{self.cls.name}",
            f"Level: {self.level}",
            f"Total XP: {self.xp}",
            f"Race: {self.race}",
            f"Background: {self.background}",
            f"Abilities:\n" + self.ability_scores,
            f"Proficiency Bonus: {self.prof_bonus_str}",
            f"Hit Points: {self.health}",
            f"Armor Class: {self.ac}",
            f"Attack Bonus: {self.att_bonus}",
            f"Basic Damage Formula: {self.damage_formula}",
            f"Special Damage Formula: {self.special_damage_formula}",
            f"Save DC: {self.cls.fav_stat} {self.save_dc}",
            f"Save Proficiencies: {', '.join(self.saves)}",
            f"Save Modifiers: {', '.join(self.saving_throws)}",
            f"Inventory: {self.loot}",
            f"Equipment: {gear}",
            "",
        )
        return '\n'.join(output)

    def set_racial_bonuses(self):
        if self.race in self.racial_bonuses.keys():
            for stat, val in self.racial_bonuses[self.race].items():
                self.stats[stat] += val

    def set_random_stats(self):
        result = {}
        stats = ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA')
        for ability in stats:
            if ability == self.cls.fav_stat:
                result[ability] = ability_dice(6)
            elif ability == self.cls.sec_stat:
                result[ability] = ability_dice(5)
            elif ability == 'CON':
                result[ability] = ability_dice(4)
            else:
                result[ability] = ability_dice(3)
        return result

    def set_ac(self):
        self.ac = self.cls.armor_ac + min(self.stat_mod['DEX'], self.cls.max_ac_dex) + self.magic_bonus

    def set_stat_mods(self):
        mod_by_stat = (
            -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7
        )
        for ability in self.stats:
            self.stat_mod[ability] = mod_by_stat[smart_clamp(self.stats[ability], 0, 24)]
            if self.stat_mod[ability] > 0:
                self.stat_mod_str[ability] = f"+{self.stat_mod[ability]}"
            else:
                self.stat_mod_str[ability] = f"{self.stat_mod[ability]}"

    def set_health(self):
        bonus = self.stat_mod['CON'] * self.level
        ave_hp_by_level = (self.level - 1) * ((self.cls.hd // 2) + 1)
        self.health = self.cls.hd + ave_hp_by_level + bonus

    def set_prof(self):
        prof_by_level = (0, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6)
        self.prof_bonus = prof_by_level[self.level]
        self.magic_bonus = self.set_magic()
        self.prof_bonus_str = f"{self.prof_bonus}"

    def set_save_dc(self):
        self.save_dc = 8 + self.prof_bonus + self.stat_mod[self.cls.fav_stat]

    def set_att_bonus(self):
        self.att_bonus = self.stat_mod[self.cls.fav_stat] + self.prof_bonus + self.magic_bonus

    def set_xp(self):
        xp_by_level = (
            0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000,
            100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000, 400000, 800000
        )
        if self.level <= 1:
            self.xp = xp_by_level[0]
        else:
            self.xp = random_range(xp_by_level[self.level - 1], xp_by_level[self.level])
            for _ in range(self.level // 4):
                self.boost_stats()

    def boost_stats(self):
        if self.stats[self.cls.fav_stat] <= 22:
            self.stats[self.cls.fav_stat] += 2
        elif self.stats[self.cls.fav_stat] == 23:
            self.stats[self.cls.fav_stat] += 1
            self.stats[self.cls.sec_stat] += 1
        else:
            if self.stats[self.cls.sec_stat] <= 22:
                self.stats[self.cls.sec_stat] += 2
            elif self.stats[self.cls.sec_stat] == 23:
                self.stats[self.cls.sec_stat] += 1
                if self.stats['CON'] <= 23:
                    self.stats['CON'] += 1
            else:
                self.stats['CON'] += 2 if self.stats['CON'] <= 22 else 1 if self.stats['CON'] == 23 else 0
        self.set_stat_mods()


random_character_class = TruffleShuffle((
    Barbarian, Bard, Cleric,
    Druid, Fighter, Monk,
    Paladin, Ranger, Rogue,
    Sorcerer, Warlock, Wizard,
    Knight,
), flat=False)

random_tank = QuantumMonty((Knight, Fighter, Barbarian, Paladin), flat=False).front_linear
random_healer = QuantumMonty((Cleric, Druid, Paladin), flat=False).front_linear

random_dps = FlexCat({
    "Common": (Rogue, Ranger, Wizard, Sorcerer, Warlock, Monk),
    "Uncommon": (Fighter, Barbarian, Bard, Knight),
    "Rare": (Cleric, Druid, Paladin),
}, flat=False)


class Party:

    def __init__(self, level=1, strategy="default", race=None):
        self.level = level
        self.party_list = []
        self.race = race
        if strategy == "party_1":
            self.party_1()
        elif strategy == "gold":
            self.gold_party(gold_level=10)
        elif strategy == "silver":
            self.gold_party(gold_level=5)
        elif strategy == "apprentice":
            self.apprentice()
        else:
            self.default_party()

    def apprentice(self):
        self.party_list.append(Player(Apprentice, self.level, self.race))
        self.party_list.append(Player(Apprentice, self.level, self.race))
        self.party_list.append(Player(Apprentice, self.level, self.race))
        self.party_list.append(Player(Apprentice, self.level, self.race))
        self.party_list.append(Player(Apprentice, self.level, self.race))

    def default_party(self):
        self.party_list.append(Player(random_tank(), self.level, self.race))
        self.party_list.append(Player(random_healer(), self.level, self.race))
        self.party_list.append(Player(random_dps(), self.level, self.race))
        self.party_list.append(Player(random_dps(), self.level, self.race))
        self.party_list.append(Player(random_dps(), self.level, self.race))

    def party_1(self):
        self.party_list.append(Player(Paladin, self.level, self.race))
        self.party_list.append(Player(Cleric, self.level, self.race))
        self.party_list.append(Player(Wizard, self.level, self.race))
        self.party_list.append(Player(Rogue, self.level, self.race))
        self.party_list.append(Player(Ranger, self.level, self.race))

    def gold_party(self, gold_level=10):
        tank = Player(random_tank(), self.level, self.race)
        for _ in range(gold_level):
            t = Player(random_tank(), self.level, self.race)
            if t > tank:
                tank = t
        self.party_list.append(tank)
        healer = Player(random_healer(), self.level, self.race)
        for _ in range(gold_level):
            h = Player(random_healer(), self.level, self.race)
            if h > healer:
                healer = h
        self.party_list.append(healer)
        for _ in range(3):
            dps = Player(random_dps(), self.level, self.race)
            for _ in range(gold_level):
                da = Player(random_dps(), self.level, self.race)
                if da > dps:
                    dps = da
            self.party_list.append(dps)

    def __repr__(self):
        return "\n".join(str(itm) for itm in self.party_list)


if __name__ == '__main__':
    print()
    for lev in (0, 1, 5, 10, 15, 20):
        print(f"\nParty Level: {lev}")
        print(f"---------------\n")
        pc_party = Party(lev, strategy='gold')
        print(pc_party)
