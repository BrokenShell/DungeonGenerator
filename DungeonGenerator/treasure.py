from Fortuna import *
from DungeonGenerator.utilities import cr_adapter
from DungeonGenerator.spells import random_spell


def magic_table_by_cr(cr):
    tables = (magic_table_f, magic_table_g, magic_table_h, magic_table_i)
    tier = smart_clamp(cr // 5, 0, 3)
    return tables[tier]()


def get_loot(cr, monster_name="Any", room_name="Any", is_villain=False):
    loot = get_monster_loot(cr)
    epic_monsters = ("Dragon", "Mimic", "Gelatinous", "Legendary")
    epic_rooms = ("Lair", "Fortuna", "Dungeon Heart", "Treasury")
    if is_villain or any(m in monster_name for m in epic_monsters) or any(r in room_name for r in epic_rooms):
        loot += get_villain_loot(cr)
    return loot


def get_monster_loot(cr):
    if cr <= 4:
        loot = RankOneLoot
    elif cr <= 10:
        loot = RankTwoLoot
    elif cr <= 16:
        loot = RankThreeLoot
    else:
        loot = RankFourLoot
    return loot()


def get_villain_loot(cr):
    if cr <= 4:
        loot = RankOneHoardLoot
    elif cr <= 10:
        loot = RankTwoHoardLoot
    elif cr <= 16:
        loot = RankThreeHoardLoot
    else:
        loot = RankFourHoardLoot
    return loot()


class Loot:
    """ Base Class for loot, starts empty """

    def __init__(self):
        self.coinage = {
            'Copper': 0, 'Silver': 0, 'Electrum': 0, 'Gold': 0, 'Platinum': 0,
            'Gems': 0, 'Jewels': 0
        }
        self.magic_items = []

    def get_gold_value(self):
        golds = (
            self.coinage["Gold"],
            self.coinage["Gems"],
            self.coinage["Jewels"],
            self.coinage["Platinum"] * 10,
            self.coinage["Electrum"] / 2,
            self.coinage["Silver"] / 10,
            self.coinage["Copper"] / 100,
        )
        return sum(golds)

    def __add__(self, other):
        new_loot = Loot()
        for val in self.coinage:
            new_loot.coinage[val] = self.coinage[val] + other.coinage[val]
        new_loot.magic_items.extend(self.magic_items + other.magic_items)
        return new_loot

    def __repr__(self):
        return self.reduce_loot()

    def __len__(self):
        return len(self.magic_items)

    def reduce_loot(self):
        output = []
        for coin in self.coinage:
            if self.coinage[coin] > 0:
                if coin == "Gems" or coin == "Jewels":
                    output.append(f"{coin} {self.coinage[coin]} GP")
                else:
                    output.append(f"{self.coinage[coin]} {coin} Coins")
        if self.magic_items:
            for itm in sorted(list(set(self.magic_items))):
                output.append(itm)
        if len(output) == 0:
            output = ['Empty']
        return '\n  ' + "\n  ".join(output) if len(output) > 1 else output[0]

    def set_loot(self, loot_data):
        loot = cumulative_weighted_choice(loot_data)
        for key in loot:
            if key == "Magic_Items":
                for itm in loot[key]:
                    table, amount = itm
                    if amount == 1:
                        self.magic_items.append(table())
                    else:
                        self.magic_items.extend(table() for _ in range(dice(*amount)))
            else:
                coin_type, amount = key, loot[key]
                n = len(amount)
                if n == 2:
                    r, s = amount
                    self.coinage[coin_type] += dice(r, s)
                elif n == 3:
                    r, s, m = amount
                    self.coinage[coin_type] += dice(r, s) * m


class RankOneLoot(Loot):
    """ Monster CR 0-4 """

    def __init__(self):
        super().__init__()
        loot_data = (
            (30, {"Copper": (5, 6)}),
            (60, {"Silver": (4, 6)}),
            (70, {"Electrum": (3, 6)}),
            (95, {"Gold": (3, 6)}),
            (100, {"Platinum": (1, 6)}),
        )
        self.set_loot(loot_data)


class RankTwoLoot(Loot):
    """ Monster CR 5-10 """

    def __init__(self):
        super().__init__()
        loot_data = (
            (30, {"Copper": (4, 6, 100), "Electrum": (1, 6, 10)}),
            (60, {"Silver": (6, 6, 100), "Gold": (2, 6, 10)}),
            (70, {"Electrum": (3, 6, 10), "Gold": (2, 6, 10)}),
            (95, {"Gold": (4, 6, 10)}),
            (100, {"Gold": (2, 6, 10), "Platinum": (3, 6)}),
        )
        self.set_loot(loot_data)


class RankThreeLoot(Loot):
    """ Monster CR 11-16 """

    def __init__(self):
        super().__init__()
        loot_data = (
            (20, {"Silver": (4, 6, 100), "Gold": (1, 6, 100)}),
            (35, {"Electrum": (1, 6, 100), "Gold": (1, 6, 100)}),
            (75, {"Gold": (2, 6, 100), "Platinum": (1, 6, 10)}),
            (100, {"Gold": (2, 6, 100), "Platinum": (2, 6, 10)}),
        )
        self.set_loot(loot_data)


class RankFourLoot(Loot):
    """ Monster CR 17+ """

    def __init__(self):
        super().__init__()
        loot_data = (
            (15, {"Electrum": (2, 6, 1000), "Gold": (8, 6, 100)}),
            (55, {"Gold": (1, 6, 1000), "Platinum": (1, 6, 100)}),
            (100, {"Gold": (1, 6, 1000), "Platinum": (2, 6, 100)})
        )
        self.set_loot(loot_data)


class RankOneHoardLoot(Loot):
    """ Hoard CR 0-4 """

    def __init__(self):
        super().__init__()
        self.coinage = {
            'Copper': dice(6, 6) * 100, 'Silver': dice(3, 6) * 100,
            'Electrum': 0, 'Gold': dice(2, 6) * 10, 'Platinum': 0,
            'Gems': 0, 'Jewels': 0
        }
        loot_data = (
            (6, {}),
            (16, {"Gems": (2, 6, 10)}),
            (26, {"Jewels": (2, 4, 25)}),
            (36, {"Gems": (2, 6, 50)}),
            (44, {"Gems": (2, 6, 10), "Magic_Items": [(magic_table_a, (1, 6))]}),
            (52, {"Jewels": (2, 4, 25), "Magic_Items": [(magic_table_a, (1, 6))]}),
            (60, {"Gems": (2, 6, 50), "Magic_Items": [(magic_table_a, (1, 6))]}),
            (65, {"Gems": (2, 6, 10), "Magic_Items": [(magic_table_b, (1, 4))]}),
            (70, {"Jewels": (2, 4, 25), "Magic_Items": [(magic_table_b, (1, 4))]}),
            (75, {"Gems": (2, 6, 50), "Magic_Items": [(magic_table_b, (1, 4))]}),
            (78, {"Gems": (2, 6, 10), "Magic_Items": [(magic_table_c, (1, 4))]}),
            (80, {"Jewels": (2, 4, 25), "Magic_Items": [(magic_table_c, (1, 4))]}),
            (85, {"Gems": (2, 6, 50), "Magic_Items": [(magic_table_c, (1, 4))]}),
            (92, {"Gems": (2, 4, 25), "Magic_Items": [(magic_table_f, (1, 4))]}),
            (97, {"Jewels": (2, 6, 50), "Magic_Items": [(magic_table_f, (1, 4))]}),
            (99, {"Gems": (2, 4, 25), "Magic_Items": [(magic_table_g, 1)]}),
            (100, {"Jewels": (2, 6, 50), "Magic_Items": [(magic_table_g, 1)]})
        )
        self.set_loot(loot_data)


class RankTwoHoardLoot(Loot):
    """ Hoard CR 5-10 """

    def __init__(self):
        super().__init__()
        self.coinage = {
            'Copper': dice(2, 6) * 100, 'Silver': dice(2, 6) * 1000,
            'Electrum': 0, 'Gold': dice(6, 6) * 100, 'Platinum': dice(3, 6) * 10,
            'Gems': 0, 'Jewels': 0
        }
        loot_data = (
            (4, {}),
            (10, {"Jewels": (2, 4, 25)}),
            (16, {"Gems": (3, 6, 50)}),
            (22, {"Gems": (3, 6, 100)}),
            (28, {"Jewels": (2, 4, 250)}),
            (32, {"Jewels": (2, 4, 25), "Magic_Items": [(magic_table_a, (1, 6))]}),
            (36, {"Gems": (3, 6, 50), "Magic_Items": [(magic_table_a, (1, 6))]}),
            (40, {"Gems": (3, 6, 100), "Magic_Items": [(magic_table_a, (1, 6))]}),
            (44, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_a, (1, 6))]}),
            (49, {"Jewels": (2, 4, 25), "Magic_Items": [(magic_table_b, (1, 4))]}),
            (54, {"Gems": (3, 6, 50), "Magic_Items": [(magic_table_b, (1, 4))]}),
            (59, {"Gems": (3, 6, 100), "Magic_Items": [(magic_table_b, (1, 4))]}),
            (63, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_b, (1, 4))]}),
            (66, {"Jewels": (2, 4, 25), "Magic_Items": [(magic_table_c, (1, 4))]}),
            (69, {"Gems": (3, 6, 50), "Magic_Items": [(magic_table_c, (1, 4))]}),
            (72, {"Gems": (3, 6, 100), "Magic_Items": [(magic_table_c, (1, 4))]}),
            (74, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_c, (1, 4))]}),
            (76, {"Jewels": (2, 4, 25), "Magic_Items": [(magic_table_d, 1)]}),
            (78, {"Gems": (3, 6, 50), "Magic_Items": [(magic_table_d, 1)]}),
            (79, {"Gems": (3, 6, 100), "Magic_Items": [(magic_table_d, 1)]}),
            (80, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_d, 1)]}),
            (84, {"Jewels": (2, 4, 25), "Magic_Items": [(magic_table_f, (1, 4))]}),
            (88, {"Gems": (3, 6, 50), "Magic_Items": [(magic_table_f, (1, 4))]}),
            (91, {"Gems": (3, 6, 100), "Magic_Items": [(magic_table_f, (1, 4))]}),
            (94, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_f, (1, 4))]}),
            (96, {"Gems": (2, 4, 100), "Magic_Items": [(magic_table_g, (1, 4))]}),
            (98, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_g, (1, 4))]}),
            (99, {"Gems": (3, 6, 100), "Magic_Items": [(magic_table_h, 1)]}),
            (100, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_h, 1)]})
        )
        self.set_loot(loot_data)


class RankThreeHoardLoot(Loot):
    """ Hoard CR 11-16 """

    def __init__(self):
        super().__init__()
        self.coinage = {
            'Copper': 0, 'Silver': 0, 'Electrum': 0,
            'Gold': dice(4, 6) * 1000, 'Platinum': dice(5, 6) * 100,
            'Gems': 0, 'Jewels': 0
        }
        loot_data = (
            (3, {}),
            (6, {"Jewels": (2, 4, 250)}),
            (9, {"Jewels": (2, 4, 750)}),
            (12, {"Gems": (3, 6, 500)}),
            (15, {"Gems": (3, 6, 1000)}),
            (19, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_a, (1, 4)), (magic_table_b, (1, 6))]}),
            (23, {"Jewels": (2, 4, 750), "Magic_Items": [(magic_table_a, (1, 4)), (magic_table_b, (1, 6))]}),
            (26, {"Gems": (3, 6, 500), "Magic_Items": [(magic_table_a, (1, 4)), (magic_table_b, (1, 6))]}),
            (29, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_a, (1, 4)), (magic_table_b, (1, 6))]}),
            (35, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_c, (1, 6))]}),
            (40, {"Jewels": (2, 4, 750), "Magic_Items": [(magic_table_c, (1, 6))]}),
            (45, {"Gems": (3, 6, 500), "Magic_Items": [(magic_table_c, (1, 6))]}),
            (50, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_c, (1, 6))]}),
            (54, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_d, (1, 4))]}),
            (58, {"Jewels": (2, 4, 750), "Magic_Items": [(magic_table_d, (1, 4))]}),
            (62, {"Gems": (3, 6, 500), "Magic_Items": [(magic_table_d, (1, 4))]}),
            (66, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_d, (1, 4))]}),
            (68, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_e, 1)]}),
            (70, {"Jewels": (2, 4, 750), "Magic_Items": [(magic_table_e, 1)]}),
            (72, {"Gems": (3, 6, 500), "Magic_Items": [(magic_table_e, 1)]}),
            (74, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_e, 1)]}),
            (76, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_g, (1, 4))]}),
            (78, {"Jewels": (2, 4, 750), "Magic_Items": [(magic_table_g, (1, 4))]}),
            (80, {"Gems": (3, 6, 500), "Magic_Items": [(magic_table_g, (1, 4))]}),
            (82, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_g, (1, 4))]}),
            (85, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_h, (1, 4))]}),
            (88, {"Jewels": (2, 4, 750), "Magic_Items": [(magic_table_h, (1, 4))]}),
            (90, {"Gems": (3, 6, 500), "Magic_Items": [(magic_table_h, (1, 4))]}),
            (92, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_h, (1, 4))]}),
            (94, {"Jewels": (2, 4, 250), "Magic_Items": [(magic_table_i, 1)]}),
            (96, {"Jewels": (2, 4, 750), "Magic_Items": [(magic_table_i, 1)]}),
            (98, {"Gems": (3, 6, 500), "Magic_Items": [(magic_table_i, 1)]}),
            (100, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_i, 1)]}),
        )
        self.set_loot(loot_data)


class RankFourHoardLoot(Loot):
    """ Hoard CR 17+ """

    def __init__(self):
        super().__init__()
        self.coinage = {
            'Copper': 0, 'Silver': 0, 'Electrum': 0,
            'Gold': dice(12, 6) * 1000, 'Platinum': dice(8, 6) * 1000,
            'Gems': 0, 'Jewels': 0
        }
        loot_data = (
            (2, {}),
            (5, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_c, (1, 8))]}),
            (8, {"Jewels": (1, 10, 2500), "Magic_Items": [(magic_table_c, (1, 8))]}),
            (11, {"Jewels": (1, 4, 7500), "Magic_Items": [(magic_table_c, (1, 8))]}),
            (14, {"Gems": (1, 8, 5000), "Magic_Items": [(magic_table_c, (1, 8))]}),
            (22, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_d, (1, 6))]}),
            (30, {"Jewels": (1, 10, 2500), "Magic_Items": [(magic_table_d, (1, 6))]}),
            (38, {"Jewels": (1, 4, 7500), "Magic_Items": [(magic_table_d, (1, 6))]}),
            (46, {"Gems": (1, 8, 5000), "Magic_Items": [(magic_table_d, (1, 6))]}),
            (52, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_e, (1, 6))]}),
            (58, {"Jewels": (1, 10, 2500), "Magic_Items": [(magic_table_e, (1, 6))]}),
            (63, {"Jewels": (1, 4, 7500), "Magic_Items": [(magic_table_e, (1, 6))]}),
            (68, {"Gems": (1, 8, 5000), "Magic_Items": [(magic_table_e, (1, 6))]}),
            (69, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_g, (1, 4))]}),
            (70, {"Jewels": (1, 10, 2500), "Magic_Items": [(magic_table_g, (1, 4))]}),
            (71, {"Jewels": (1, 4, 7500), "Magic_Items": [(magic_table_g, (1, 4))]}),
            (72, {"Gems": (1, 8, 5000), "Magic_Items": [(magic_table_g, (1, 4))]}),
            (74, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_h, (1, 4))]}),
            (76, {"Jewels": (1, 10, 2500), "Magic_Items": [(magic_table_h, (1, 4))]}),
            (78, {"Jewels": (1, 4, 7500), "Magic_Items": [(magic_table_h, (1, 4))]}),
            (80, {"Gems": (1, 8, 5000), "Magic_Items": [(magic_table_h, (1, 4))]}),
            (85, {"Gems": (3, 6, 1000), "Magic_Items": [(magic_table_i, (1, 4))]}),
            (90, {"Jewels": (1, 10, 2500), "Magic_Items": [(magic_table_i, (1, 4))]}),
            (95, {"Jewels": (1, 4, 7500), "Magic_Items": [(magic_table_i, (1, 4))]}),
            (100, {"Gems": (1, 8, 5000), "Magic_Items": [(magic_table_i, (1, 4))]})
        )
        self.set_loot(loot_data)


magic_table_a = CumulativeWeightedChoice((
    (50, "Potion of healing"),
    (60, lambda: f"Spell scroll (cantrip) {random_spell('cantrip')}"),
    (70, "Potion of climbing"),
    (90, lambda: f"Spell scroll (1st level) {random_spell('level_1')}"),
    (94, lambda: f"Spell scroll (2nd level) {random_spell('level_2')}"),
    (98, "Potion of greater healing"),
    (99, "Bag of holding"),
    (100, "Driftglobe")
))


magic_table_b = CumulativeWeightedChoice((
    (15, "Potion of greater healing"),
    (22, "Potion of fire breath"),
    (29, "Potion of resistance"),
    (34, lambda: f"Ammunition: {random_ammunition()} +1"),
    (39, "Potion of animal friendship"),
    (44, "Potion of hill giant strength"),
    (49, "Potion of growth"),
    (54, "Potion of water breathing"),
    (59, lambda: f"Spell scroll (2nd level) {random_spell('level_2')}"),
    (64, lambda: f"Spell scroll (3rd level) {random_spell('level_3')}"),
    (67, "Bag of holding"),
    (70, "Keoghtom's ointment"),
    (73, "Oil of slipperiness"),
    (75, "Dust of disappearance"),
    (77, "Dust of dryness"),
    (79, "Dust of sneezing and choking"),
    (81, "Elemental gem"),
    (83, "Philter of love"),
    (84, "Alchemy jug"),
    (85, "Cap of water breathing"),
    (86, "Cloak of the manta ray"),
    (87, "Driftglobe"),
    (88, "Goggles of night"),
    (89, "Helm of comprehending languages"),
    (90, "Immovable rod"),
    (91, "Lantern of revealing"),
    (92, "Mariner's armor"),
    (93, "Mithral armor"),
    (94, "Potion of poison"),
    (95, "Ring of swimming"),
    (96, "Robe of useful items"),
    (97, "Rope of climbing"),
    (98, "Saddle of the cavalier"),
    (99, "Wand of magic detection"),
    (100, "Wand of secrets")
))


magic_table_c = CumulativeWeightedChoice((
    (15, "Potion of superior healing"),
    (22, lambda: f"Spell scroll (4th level) {random_spell('level_4')}"),
    (27, lambda: f"Ammunition: {random_ammunition()} +2"),
    (32, "Potion of clairvoyance"),
    (37, "Potion of diminution"),
    (42, "Potion of gaseous form"),
    (47, "Potion of frost giant strength"),
    (52, "Potion of stone giant strength"),
    (57, "Potion of heroism"),
    (62, "Potion of invulnerability"),
    (67, "Potion of mind reading"),
    (72, lambda: f"Spell scroll (5th level) {random_spell('level_5')}"),
    (75, "Elixir of health"),
    (78, "Oil of etherealness"),
    (81, "Potion of fire giant strength"),
    (84, "Quaal's feather token"),
    (87, "Scroll of protection"),
    (89, "Bag of beans"),
    (91, "Bead of force"),
    (92, "Chime of opening"),
    (93, "Decanter of endless water"),
    (94, "Eyes of minute seeing"),
    (95, "Folding boat"),
    (96, "Heward's handy haversack"),
    (97, "Horseshoes of speed"),
    (98, "Necklace of fireballs"),
    (99, "Periapt of health"),
    (100, "Sending stones")
))


magic_table_d = CumulativeWeightedChoice((
    (20, "Potion of supreme healing"),
    (30, "Potion of invisibility"),
    (40, "Potion of speed"),
    (50, lambda: f"Spell scroll (6th level) {random_spell('level_6')}"),
    (57, lambda: f"Spell scroll (7th level) {random_spell('level_7')}"),
    (62, lambda: f"Ammunition: {random_ammunition()} +3"),
    (67, "Oil of sharpness"),
    (72, "Potion of flying"),
    (77, "Potion of cloud giant strength"),
    (82, "Potion of longevity"),
    (87, "Potion of vitality"),
    (92, lambda: f"Spell scroll (8th level) {random_spell('level_8')}"),
    (95, "Horseshoes of a zephyr"),
    (98, "Nolzur's marvelous pigments"),
    (99, "Bag of devouring"),
    (100, "Portable hole")
))


magic_table_e = CumulativeWeightedChoice((
    (30, lambda: f"Spell scroll (8th level) {random_spell('level_8')}"),
    (55, "Potion of storm giant strength"),
    (70, "Potion of supreme healing"),
    (85, lambda: f"Spell scroll (9th level) {random_spell('level_9')}"),
    (93, "Universal solvent"),
    (98, "Arrow of slaying"),
    (100, "Sovereign glue")
))


magic_table_f = CumulativeWeightedChoice((
    (15, lambda: f"{weapon_list()} +1"),
    (18, "Shield +1"),
    (21, "Sentinel shield"),
    (23, "Amulet of proof against detection and location"),
    (25, "Boots of elvenkind"),
    (27, "Boots of striding and springing"),
    (29, "Bracers of archery"),
    (31, "Brooch of shielding"),
    (33, "Broom of flying"),
    (35, "Cloak of elvenkind"),
    (37, "Cloak of protection"),
    (39, "Gauntlets of ogre power"),
    (41, "Hat of disguise"),
    (43, "Javelin of lightning"),
    (45, "Pearl of power"),
    (47, "Rod of the pact keeper +1"),
    (49, "Slippers of spider climbing"),
    (51, "Staff of the adder"),
    (53, "Staff of the python"),
    (55, "Sword of vengeance"),
    (57, "Trident of fish command"),
    (59, "Wand of magic missiles"),
    (61, "Wand of the war mage +1"),
    (63, "Wand of web"),
    (65, "Weapon of warning"),
    (66, "Adamantine armor (chain mail)"),
    (67, "Adamantine armor (chain shirt)"),
    (68, "Adamantine armor (scale mail)"),
    (69, "Bag of tricks (gray)"),
    (70, "Bag of tricks (rust)"),
    (71, "Bag of tricks (tan)"),
    (72, "Boots of the winterlands"),
    (73, "Circlet of blasting"),
    (74, "Deck of illusions"),
    (75, "Eversmoking bottle"),
    (76, "Eyes of charming"),
    (77, "Eyes of the eagle"),
    (78, "Figurine of wondrous power (silver raven)"),
    (79, "Gem of brightness"),
    (80, "Gloves of missile snaring"),
    (81, "Gloves of swimming and climbing"),
    (82, "Gloves of thievery"),
    (83, "Headband of intellect"),
    (84, "Helm of telepathy"),
    (85, "Instrument of the bards (Doss lute)"),
    (86, "Instrument of the bards (Fochlucan bandore)"),
    (87, "Instrument of the bards (Mac-Fuimidh cittern)"),
    (88, "Medallion of thoughts"),
    (89, "Necklace of adaptation"),
    (90, "Periapt of wound closure"),
    (91, "Pipes of haunting"),
    (92, "Pipes of the sewers"),
    (93, "Ring of jumping"),
    (94, "Ring of mind shielding"),
    (95, "Ring of warmth"),
    (96, "Ring of water walking"),
    (97, "Quiver of Ehlonna"),
    (98, "Stone of good luck"),
    (99, "Wind fan"),
    (100, "Winged boots")
))


magic_table_g = CumulativeWeightedChoice((
    (11, lambda: f"{weapon_list()} +2"),
    (14, lambda: f"Figurine of wondrous power: {fig_wondrous_power()}"),
    (15, "Adamantine armor (breastplate)"),
    (16, "Adamantine armor (splint)"),
    (17, "Amulet of health"),
    (18, "Armor of vulnerability"),
    (19, "Arrow-catching shield"),
    (20, "Belt of dwarvenkind"),
    (21, "Belt of hill giant strength"),
    (22, "Berserker axe"),
    (23, "Boots of levitation"),
    (24, "Boots of speed"),
    (25, "Bowl of commanding water elemental"),
    (26, "Bracers of defense"),
    (27, "Brazier of commanding fire elemental"),
    (28, "Cape of the mountebank"),
    (29, "Censer of controlling air elemental"),
    (30, "Armor +1 chain mail"),
    (31, "Armor of resistance (chain mail)"),
    (32, "Armor +1 chain shirt"),
    (33, "Armor of resistance (chain shirt)"),
    (34, "Cloak of displacement"),
    (35, "Cloak of the bat"),
    (36, "Cube of force"),
    (37, "Daern's instant fortress"),
    (38, "Dagger of venom"),
    (39, "Dimensional shackles"),
    (40, "Dragon slayer"),
    (41, "Elven chain"),
    (42, "Flame tongue"),
    (43, "Gem of seeing"),
    (44, "Giant slayer"),
    (45, "Clamoured studded leather"),
    (46, "Helm of teleportation"),
    (47, "Horn of blasting"),
    (48, "Horn of Valhalla (silver or brass)"),
    (49, "Instrument of the bards (Canaith mandolin)"),
    (50, "Instrument of the bards (Cii lyre)"),
    (51, "Ioun stone (awareness)"),
    (52, "Ioun stone (protection)"),
    (53, "Ioun stone (reserve)"),
    (54, "Ioun stone (sustenance)"),
    (55, "Iron bands of Bilarro"),
    (56, "Armor +1 leather"),
    (57, "Armor of resistance (leather)"),
    (58, "Mace of disruption"),
    (59, "Mace of smiting"),
    (60, "Mace of terror"),
    (61, "Mantle of spell resistance"),
    (62, "Necklace of prayer beads"),
    (63, "Periapt of proof against poison"),
    (64, "Ring of animal influence"),
    (65, "Ring of evasion"),
    (66, "Ring of feather falling"),
    (67, "Ring of free action"),
    (68, "Ring of protection"),
    (69, "Ring of resistance"),
    (70, "Ring of spell storing"),
    (71, "Ring of the ram"),
    (72, "Ring of X-ray vision"),
    (73, "Robe of eyes"),
    (74, "Rod of rulership"),
    (75, "Rod of the pact keeper +2"),
    (76, "Rope of entanglement"),
    (77, "Armor +1 scale mail"),
    (78, "Armor of resistance (scale mail)"),
    (79, "Shield +2"),
    (80, "Shield of missile attraction"),
    (81, "Staff of charming"),
    (82, "Staff of healing"),
    (83, "Staff of swarming insects"),
    (84, "Staff of the woodlands"),
    (85, "Staff of withering"),
    (86, "Stone of controlling earth elemental"),
    (87, "Sun blade"),
    (88, "Sword of life stealing"),
    (89, "Sword of wounding"),
    (90, "Tentacle rod"),
    (91, "Vicious weapon"),
    (92, "Wand of binding"),
    (93, "Wand of enemy detection"),
    (94, "Wand of fear"),
    (95, "Wand of fireballs"),
    (96, "Wand of lightning bolts"),
    (97, "Wand of paralysis"),
    (98, "Wand of the war mage +2"),
    (99, "Wand of wonder"),
    (100, "Wings of flying")
))


magic_table_h = CumulativeWeightedChoice((
    (10, lambda: f"{weapon_list()} +3"),
    (12, "Amulet of the planes"),
    (14, "Carpet of flying"),
    (16, "Crystal ball (very rare version)"),
    (18, "Ring of regeneration"),
    (20, "Ring of shooting stars"),
    (22, "Ring of telekinesis"),
    (24, "Robe of scintillating colors"),
    (26, "Robe of stars"),
    (28, "Rod of absorption"),
    (30, "Rod of alertness"),
    (32, "Rod of security"),
    (34, "Rod of the pact keeper +3"),
    (36, "Scimitar of speed"),
    (38, "Shield +3"),
    (40, "Staff of fire"),
    (42, "Staff of frost"),
    (44, "Staff of power"),
    (46, "Staff of striking"),
    (48, "Staff of thunder and lightning"),
    (50, "Sword of sharpness"),
    (52, "Wand of polymorph"),
    (54, "Wand of the war mage +3"),
    (55, "Adamantine armor (half plate)"),
    (56, "Adamantine armor (plate)"),
    (57, "Animated shield"),
    (58, "Belt of fire giant strength"),
    (59, "Belt of frost (or stone) giant strength"),
    (60, "Armor +1 breastplate"),
    (61, "Armor of resistance (breastplate)"),
    (62, "Candle of invocation"),
    (63, "Armor +2 chain mail"),
    (64, "Armor +2 chain shirt"),
    (65, "Cloak of arachnida"),
    (66, "Dancing sword"),
    (67, "Demon armor"),
    (68, "Dragon scale mail"),
    (69, "Dwarven plate"),
    (70, "Dwarven thrower"),
    (71, "Efreeti bottle"),
    (72, "Figurine of wondrous power (obsidian steed)"),
    (73, "Frost brand"),
    (74, "Helm of brilliance"),
    (75, "Horn of Valhalla (bronze)"),
    (76, "Instrument of the bards (Anstruth harp)"),
    (77, "Ioun stone (absorption)"),
    (78, "Ioun stone (agility)"),
    (79, "Ioun stone (fortitude)"),
    (80, "Ioun stone (insight)"),
    (81, "Ioun stone (intellect)"),
    (82, "Ioun stone (leadership)"),
    (83, "Ioun stone (strength)"),
    (84, "Armor +2 leather"),
    (85, "Manual of bodily health"),
    (86, "Manual of gainful exercise"),
    (87, "Manual of golems"),
    (88, "Manual of quickness of action"),
    (89, "Mirror of life trapping"),
    (90, "Nine lives stealer"),
    (91, "Oath bow"),
    (92, "Armor +2 scale mail"),
    (93, "Spellguard shield"),
    (94, "Armor +1 splint"),
    (95, "Armor of resistance (splint)"),
    (96, "Armor +1 studded leather"),
    (97, "Armor of resistance (studded leather)"),
    (98, "Tome of clear thought"),
    (99, "Tome of leadership and influence"),
    (100, "Tome of understanding")
))


magic_table_i = CumulativeWeightedChoice((
    (5, "Defender"),
    (10, "Hammer of thunderbolts"),
    (15, "Luck blade"),
    (20, "Sword of answering"),
    (23, "Holy avenger"),
    (26, "Ring of djinni summoning"),
    (29, "Ring of invisibility"),
    (32, "Ring of spell turning"),
    (35, "Rod of lordly might"),
    (38, "Staff of the magi"),
    (41, "Vorpal sword"),
    (43, "Belt of cloud giant strength"),
    (45, "Armor +2 breastplate"),
    (47, "Armor +3 chain mail"),
    (49, "Armor +3 chain shirt"),
    (51, "Cloak of invisibility"),
    (53, "Crystal ball (legendary version)"),
    (55, "Armor +1 half plate"),
    (57, "Iron flask"),
    (59, "Armor +3 leather"),
    (61, "Armor +1 plate"),
    (63, "Robe of the archmagi"),
    (65, "Rod of resurrection"),
    (67, "Armor +1 scale mail"),
    (69, "Scarab of protection"),
    (71, "Armor +2 splint"),
    (73, "Armor +2 studded leather"),
    (75, "Well of many worlds"),
    (76, lambda: f"Armor {magic_armor()}"),
    (77, "Apparatus of Kwalish"),
    (78, "Armor of invulnerability"),
    (79, "Belt of storm giant strength"),
    (80, "Cubic gate"),
    (81, "Deck of many things"),
    (82, "Efreeti chain"),
    (83, "Armor of resistance (half plate)"),
    (84, "Horn of Valhalla (iron)"),
    (85, "Instrument of the bards (Ollamh harp)"),
    (86, "Ioun stone (greater absorption)"),
    (87, "Ioun stone (mastery)"),
    (88, "Ioun stone (regeneration)"),
    (89, "Plate armor of etherealness"),
    (90, "Plate armor of resistance"),
    (91, "Ring of air elemental command"),
    (92, "Ring of earth elemental command"),
    (93, "Ring of fire elemental command"),
    (94, "Ring of three wishes"),
    (95, "Ring of water elemental command"),
    (96, "Sphere of annihilation"),
    (97, "Talisman of pure good"),
    (98, "Talisman of the sphere"),
    (99, "Talisman of ultimate evil"),
    (100, "Tome of the stilled tongue")
))


weapon_list = TruffleShuffle((
    'Battleaxe',
    'Flail',
    'Glaive',
    'Greataxe',
    'Greatsword',
    'Halberd',
    'Lance',
    'Longsword',
    'Maul',
    'Morningstar',
    'Pike',
    'Rapier',
    'Scimitar',
    'Shortsword',
    'Trident',
    'War Pick',
    'Warhammer',
    'Whip',
    'Blowgun',
    'Hand Crossbow',
    'Heavy Crossbow',
    'Longbow',
    'Net',
    'Club',
    'Dagger',
    'Greatclub',
    'Handaxe',
    'Javelin',
    'Light Hammer',
    'Mace',
    'Quarterstaff',
    'Sickle',
    'Spear',
    'Light Crossbow',
    'Dart',
    'Shortbow',
    'Sling'
))

fig_wondrous_power = CumulativeWeightedChoice((
    (1, "Bronze griffon"),
    (2, "Ebony fly"),
    (3, "Golden lion"),
    (4, "Ivory goat"),
    (5, "Marble elephant"),
    (7, "Onyx dog"),
    (8, "Serpentine owl"),
))

magic_armor = CumulativeWeightedChoice((
    (2, "+2 half plate"),
    (4, "+2 plate"),
    (6, "+3 studded leather"),
    (8, "+3 breastplate"),
    (10, "+3 splint"),
    (11, "+3 half plate"),
    (12, "+3 plate"),
))


random_ammunition = TruffleShuffle((
    lambda: f"Quiver of {d(3) * 10} arrows",
    lambda: f"Box of {d(3) * 10} crossbow bolts",
    lambda: f"Bag of {d(3) * 10} sling stones",
))


def career_loot(party_size=5, start_level=1, end_level=20):
    total_loot = Loot()
    room_start = start_level * 10
    room_end = end_level * 10
    num_rooms = 0
    for i in range(room_start, room_end):
        num_rooms += 1
        total_loot += get_loot(
            cr_adapter(num_players=party_size, average_level=i//10),
            is_villain=percent_true(20)
        )
    return total_loot


def no_coin(loot: Loot) -> Loot:
    new_loot = Loot()
    new_loot.magic_items = loot.magic_items.copy()
    return new_loot


if __name__ == '__main__':
    print()
    print(RankOneHoardLoot())
