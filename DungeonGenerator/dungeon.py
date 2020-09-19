from Fortuna import *
from DungeonGenerator.monsters import CampaignBoss
from DungeonGenerator.treasure import Loot
from DungeonGenerator.npc import random_city_npc
from DungeonGenerator.room_lib import MinionRoom, BossRoom, VillainRoom, Room, \
    WildArea


class Area:
    rooms = []

    def __getitem__(self, item):
        return self.rooms[item]

    def __repr__(self):
        return "\n".join(self.rooms)


random_cond = TruffleShuffle((
    "Destroyed",
    "Abandoned",
    "Haunted",
    "Corrupted",
    "Infested",
    "Blighted",
    "Shadow",
))

random_post_cond = TruffleShuffle((
    "Lost Soul",
    "Forgotten",
    "Mad Wizard",
    "Dark Mist",
    "Blood Queen",
    "Evil Genius",
))

random_dungeon_env = TruffleShuffle((
    "Mine",
    "Crypt",
    "Tower",
    "Sewers",
    "Palace",
    "Castle",
    "Mansion",
    "Labyrinth",
    "Prison",
    "Manor",
    "Lair",
    "Undercity",
))


class Dungeon(Area):
    random_name = TruffleShuffle((
        lambda: f"{rand_color()} {random_dungeon_env()}",
        lambda: f"{random_cond()} {random_dungeon_env()}",
        lambda: f"{random_dungeon_env()} of the {random_post_cond()}",
        lambda: f"{random_cond()} {random_dungeon_env()} of the {random_post_cond()}",
    ))

    def __init__(self, cr, dungeon_name=None, dungeon_levels=1,
                 rooms_per_level=10, make_traps=True):
        self.rooms = []
        self.rooms_per_level = rooms_per_level
        self.cr = smart_clamp(cr, -3, 30)
        self.name = dungeon_name if dungeon_name else f"{self.random_name()}"
        self.total_xp = 0
        self.dungeon_levels = dungeon_levels
        self.total_rooms = dungeon_levels * self.rooms_per_level
        room_number = 1
        first_room = MinionRoom(
            cr,
            room_name="Dungeon Entrance",
        )
        self.first_room_cr = first_room.threat.cr
        self.boss_cr = 0
        self.rooms.append(f'{first_room}')
        self.threats = [first_room]
        my_room = Room()
        for dun_level in range(dungeon_levels):
            if dun_level + 1 in (5, 10, 15, 20):
                self.cr = smart_clamp(self.cr + 1, -3, 30)
            for _ in range(self.rooms_per_level):
                room_number += 1
                if room_number == self.total_rooms:
                    my_room = BossRoom(dun_level + self.cr + 2, "Dungeon Heart")
                    self.boss_cr = my_room.threat.cr
                elif room_number < self.total_rooms:
                    if room_number % self.rooms_per_level == 0:
                        my_room = VillainRoom(dun_level + self.cr + 1)
                    elif room_number % self.rooms_per_level == 1:
                        my_room = MinionRoom(dun_level + self.cr)
                    elif room_number < self.total_rooms:
                        my_room = Room(dun_level + self.cr, make_traps=make_traps)
                else:
                    break
                self.rooms.append(f'Room {room_number}, {my_room}')
                self.threats.append(my_room)
                self.total_xp += my_room.xp
        self.total_treasure = self.get_treasures()

    def get_treasures(self):
        total = Loot()
        for room in self.threats:
            if room.threat.treasure:
                total += room.threat.treasure
        return total

    def __str__(self):
        output = (
            f"Dungeon: {self.name}\n",
            "\n".join(self.rooms),
            "\n",
        )
        return "\n".join(output)

    def print_room(self, room_number):
        print(self.rooms[room_number-1])


rand_color = TruffleShuffle((
    "Red",
    "Green",
    "Blue",
    "Black",
    "Shadow",
    "Ruby",
    "Emerald",
    "Jade",
    "Sapphire",
    "Diamond",
    "Onyx",
    "Golden",
    "Silver",
    "Purple",
))

rand_flavor = TruffleShuffle((
    "Rose",
    "Greenleaf",
    "Violet",
    "Lilac",
    "Flytrap",
    "Old Oak",
    "Poison",
    "Bitter",
    "Hard Candy",
    "Saffron",
    "Hot Pepper",
    "Garlic Spice",
    "Spoon",
    "Arcane",
))

random_wild = TruffleShuffle((
    TruffleShuffle(
        ("Lake", "Bay", "Swamp", "Marsh", "River", "Creek", "Island")),
    "Forest",
    "Dessert",
    "Tundra",
    "Mountain",
    "Valley",
    "Hills",
    "Cavern",
    "Canyon",
    "Swamp",
    "Wetlands",
))


class Wilderness:
    random_name = TruffleShuffle((
        lambda: f"{rand_color()} {random_wild()}",
        lambda: f"Redwood {random_wild()}",
        lambda: f"Cavalier {random_wild()}",
        lambda: f"Frozen {random_wild()}",
        lambda: f"{random_wild()} of the Nightmare",
        lambda: f"Apple {random_wild()}",
        lambda: f"Forgotten {random_wild()}",
        lambda: f"Stormy {random_wild()}",
        lambda: f"Raven {random_wild()}",
        lambda: f"Twin {random_wild()}",
        lambda: f"Twisted {random_wild()}",
        lambda: f"{random_wild()} of the Maelstrom",
        lambda: f"Titan {random_wild()}",
        lambda: f"Flaming Pitch {random_wild()}",
        lambda: f"Blighted {random_wild()}",
        lambda: f"Rainbow {random_wild()}",
        lambda: f"{rand_flavor()} {random_wild()}",
        lambda: f"Spiral {random_wild()}",
    ))

    def __init__(self, cr, name=None, num_levels=1, areas_per_level=10):
        self.cr = smart_clamp(cr - 1, -3, 30)
        self.name = name if name else f"{self.random_name()}"
        self.total_xp = 0
        rooms_per_level = areas_per_level
        self.total_rooms = num_levels * rooms_per_level
        room_number = 1
        self.rooms = []
        self.threats = []
        self.total_treasure = self.get_treasures()

        for dun_level in range(num_levels):
            for _ in range(rooms_per_level):
                my_room = WildArea(dun_level + self.cr, self.name)
                self.rooms.append(f"Area {room_number}, {self.name}\n{my_room}")
                self.threats.append(my_room)
                if my_room.xp:
                    self.total_xp += my_room.xp
                room_number += 1

    def get_treasures(self):
        total = Loot()
        for room in self.threats:
            if room.threat.treasure:
                total += room.threat.treasure
        return total

    def __repr__(self):
        output = (
            f"Wilderness: {self.name}\n",
            "\n".join(self.rooms),
            ""
        )
        return "\n".join(output)


random_civ = TruffleShuffle((
    "Orchard",
    "Farm",
    "Ranch",
    "Traveling Market",
    "Fairgrounds",
    "Outpost",
    "Hamlet",
    "Stronghold",
    "Village",
    "Township",
    "Castle",
    "Port",
    "City",
    "Citadel",
))

random_gem = TruffleShuffle((
    "Ruby",
    "Emerald",
    "Sapphire",
    "Smoky Quartz",
    "Jade",
    "Garnet",
    "Amber",
    "Pearl",
    "Moonstone",
    "Opal",
    "Topaz",
    "Sunstone",
    "Obsidian",
    "Onyx",
    "Jet",
    "Jasper",
    "Fire Agate",
    "Tiger's Eye",
    "Pyrite",
    "Moss Agate",
))

random_material = TruffleShuffle((
    "Golden",
    "Silver",
    "Iron",
    "Rusty",
    "Bronze",
    "Copper",
    "Brass",
    "Broken",
    "Glass",
    "Crystal",
    "Frozen",
    "Flaming",
))

random_thing = TruffleShuffle((
    "Sword",
    "Dagger",
    "Battleaxe",
    "Hammer",
    "Shield",
    "Saddle",
    "Lance",
    "Wand",
    "Staff",
    "Symbol",
    "Ring",
    "Amulet",
    "Suit of Armor",
    "Cannon",
    "Helm",
    "Coin",
))

random_dragon_aspect = TruffleShuffle((
    "Wing",
    "Claw",
    "Tooth",
    "Tongue",
    "Breath",
    "Tail",
    "Fist",
    "Bounty",
    "Landing",
))

random_university = TruffleShuffle((
    "Abjuration",
    "Conjuration",
    "Divination",
    "Enchantment",
    "Evocation",
    "Illusion",
    "Necromancy",
    "Transmutation",
    "War Magic",
))

random_church_type = TruffleShuffle((
    "Church",
    "Temple",
    "Shrine",
    "Cathedral",
    "Priory",
    "Chapel",
    "Altar",
    "Sanctuary",
    "Tent Revival",
))

random_light = TruffleShuffle((
    "Moon",
    "Sun",
    "Star",
    "Fire",
    "Bioluminescent",
))

random_domain = TruffleShuffle((
    "Knowledge",
    "Life",
    lambda: f"{random_light()} Light",
    "Natural Order",
    "the Tempest",
    "the Maelstrom",
    "the Jester",
    "Chivalry",
    "the Forge",
    "the Gravestone",
    "the Death Maiden",
))

random_college = TruffleShuffle((
    "Lore",
    "Valor",
    "Glamour",
    "Swords",
    "Whispers",
    "Alliteration",
))

random_monastery = TruffleShuffle((
    "the Open Hand",
    "the Four Elements",
    "Shadows",
    "the Drunken Master",
    "the Kensei Warrior",
    "the Divine Sun Soul",
    "the Crouching Tiger",
    "the Hidden Dragon",
))

random_place = TruffleShuffle((
    "Pissbottom",
    "Beggar's Hollow",
    "Rogue's Bluff",
    "Alphea",
    "Redwood",
    "Brightwater",
    "Brokenhilt",
    "Frozenleaf",
    "Riverdale",
    "Snowmelt",
    "Silverkeep",
    "Wellspring",
    "Willowdale",
    "Wolfden",
    "Shadowkeep",
))

random_school_name = TruffleShuffle((
    "Nottingham",
    "Yorkshire",
    "Bale",
    "Banford",
    "Barvard",
    "Minster & Roth",
    "Wordshire",
    "Mantisrite",
    "Alacrat",
    "Ellendale",
    "Maybereal",
    "Maybeknot",
    "Franken",
    "Nobel",
    "Daubie",
    "Kent",
    "Black Cat",
    "Canonical",
    "Spiral Tower",
))


class Settlement:
    random_name = TruffleShuffle((
        lambda: f"{random_civ()} of the {random_material()} {random_thing()}",
        lambda: f"{random_gem()} {random_civ()}",
        lambda: f"{random_place()} {random_civ()}",
        lambda: f"Monastery of {random_monastery()}",
        lambda: f"{random_school_name()} Campus: Bardic School of {random_college()}",
        lambda: f"{random_church_type()} of {random_domain()}",
        lambda: f"{random_school_name()}: University of {random_university()}",
        lambda: f"Dragon {random_dragon_aspect()} {random_civ()}",
    ))

    def __init__(self, cr, name=None, num_people=10):
        self.cr = smart_clamp(cr - 1, -3, 30)
        self.num_people = num_people
        self.name = name if name else f"{self.random_name()}"
        self.rooms = []
        self.threats = []
        for room_num in range(1, self.num_people + 1):
            this_room = random_city_npc(self.cr)
            self.rooms.append(
                f"Area {room_num}, {self.name.split(', ')[0]}\n{this_room}")
            self.threats.append(this_room)
        self.total_treasure = self.get_treasures()

    def get_treasures(self):
        total = Loot()
        for room in self.threats:
            if room.treasure:
                total += room.treasure
        return total

    def __str__(self):
        output = (
            f"Settlement: {self.name}\n",
            "\n".join(self.rooms),
            ""
        )
        return "\n".join(output)


class AdventureSet:

    def __init__(self, *areas):
        self.areas = areas

    def summary(self):
        return '\n'.join(f"{area.name}, CR {area.cr}" for area in self.areas)

    def __str__(self):
        return ''.join(str(area) for area in self.areas)


def make_clichea():
    clichea = AdventureSet(
        Settlement(1, "Old Town"),
        Wilderness(1, "Gondar"),
        Dungeon(1, "Mines of Gondor"),
        Settlement(2, "Lionguard Castle"),
        Wilderness(2, "River Bridge"),
        Wilderness(3, "The Great River"),
        Wilderness(3, "Kingwood Forest"),
        Settlement(4, "Northern Shire"),
        Wilderness(4, "The Great Plain"),
        Wilderness(4, "Massive Wall"),
        Wilderness(5, "The Breach"),
        Wilderness(6, "Badlands"),
        Wilderness(7, "Land's End"),
        Wilderness(8, "World Scar"),
        Settlement(8, "Rajashi"),
        Wilderness(9, "Bandit Camp"),
        Wilderness(9, "The Reach"),
        Wilderness(10, "Dragon Tail Islands"),
        Dungeon(11, "Dragon's Lair"),
        Wilderness(11, "Frozen North Wastes"),
        Settlement(11, "Azgard"),
        Wilderness(12, "Mt. Kazzakrad"),
        Wilderness(13, "Mountains of Mist"),
        Settlement(13, "Forgehold"),
        Dungeon(14, "Vikingheim"),
        Wilderness(14, "The Maelstorm"),
        Wilderness(15, "Storm Bay"),
        Wilderness(15, "The Pass"),
        Wilderness(16, "Elvenhome"),
        Settlement(16, "Yggdraseal"),
        Settlement(17, "Lithdinlor"),
        Wilderness(17, "Star Lake"),
        Dungeon(18, "The Stones of Prophecy"),
        Wilderness(19, "Gothmor"),
        Wilderness(20, "The Dark Forest"),
        Wilderness(21, "Blackwater"),
        Wilderness(22, "Shadow Mountains"),
        Dungeon(23, "Mount Death"),
        Dungeon(24, "Dark Tower"),
        CampaignBoss(25, "The Prince of Lies"),
    )
    return clichea


if __name__ == "__main__":
    print()
    # adventure = AdventureSet(
    #     Settlement(0, "Pissbottom Village"),
    #     Wilderness(1, "Ever Wood Glade"),
    #     Dungeon(2, "Obsidian Deep Mines"),
    #     Settlement(2, "Moonville"),
    #     Wilderness(3, "Gray Moore Swamp"),
    #     Dungeon(4, "The Sunken Temple"),
    #     Settlement(4, "Sunny Vale"),
    #     Wilderness(5, "Mount Climax"),
    #     Dungeon(6, "Halls of Mystery"),
    #     CampaignBoss(7, "Damien"),
    # )
    # print(adventure)
    d = Dungeon(3, dungeon_levels=10)
    d.print_room(1)
