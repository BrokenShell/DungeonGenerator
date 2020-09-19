from Fortuna import *
from DungeonGenerator.traps import random_trap
from DungeonGenerator.monsters import Monster, MonsterGroup, MinionGroup, Boss, Villain, ItemEncounter
from DungeonGenerator.npc import random_dungeon_npc, random_city_npc
from DungeonGenerator.utilities import cr_adapter
from DungeonGenerator.treasure import magic_table_f


rand_color = TruffleShuffle((
    "blue",
    "red",
    "green",
    "yellow",
    "purple",
    "orange",
    "magenta",
    "indigo",
    "cyan",
    "pink",
    "golden",
))


class RoomJunk:
    rand_direction = TruffleShuffle((
        lambda: f"{'north' if percent_true(75) else 'north eastern'}",
        lambda: f"{'south' if percent_true(75) else 'south western'}",
        lambda: f"{'east' if percent_true(75) else 'south eastern'}",
        lambda: f"{'west' if percent_true(75) else 'north western'}",
    ))

    rand_container = TruffleShuffle((
        lambda: f"{rand_color()} bags",
        lambda: f"{rand_color()} baskets",
        lambda: f"{rand_color()} boxes",
        lambda: f"{rand_color()} crates",
        "bookshelves",
        "treasure chests",
        "coffins",
    ))

    rand_door_cond = QuantumMonty((
        "closed but unlocked",
        "closed and locked",
        "bared from the other side",
        "bared from this side",
        "open and unlocked",
        "magically sealed",
    ))

    rand_troop = TruffleShuffle((
        "Footman",
        "Soldier",
        "Archer",
        "Elite Guard",
        "Officer",
        "Siege Master",
        "War Mage",
        "War Priest",
        "Commander",
        "Knight"
    ))

    bridge_materials = QuantumMonty((
        "rope",
        "wooden",
        "stone",
        "rusty iron",
        "polished bronze",
        "gold wire",
        "petrified wood",
        "solid gold",
    ))


class Room:
    _names = TruffleShuffle((
        lambda: f"{RoomJunk.rand_troop()}'s Armory",
        lambda: f"Hatchery",
        TruffleShuffle(("Religious Library", "Arcane Library", "Mundane Library", "Royal Archives")),
        lambda: f"{RoomJunk.rand_troop()}'s Training Room",
        lambda: f"Treasury",
        lambda: f"Tormented Artist Studio",
        lambda: f"Backstage Dressing Room",
        lambda: f"Haunted Auditorium",
        lambda: f"Abandoned Ballroom",
        lambda: f"Carved Marble Great Hall",
        lambda: f"Gnomish Workshop",
        lambda: f"Goblin Casino",
        lambda: f"Guard Room",
        lambda: f"Bestiary",
        lambda: f"Prison Cell",
        lambda: f"Prison Workout Room",
        lambda: f"Torture Chamber",
        lambda: f"Crypt",
        lambda: f"Combat Pit {'Arena' if percent_true(75) else 'Bleachers'}",
        lambda: f"Shrine of Fortuna",
        lambda: f"Desecrated Altar of Light",
        lambda: f"Unholy Temple",
        lambda: f"Desecrated Chapel",
        lambda: f"Kitchen",
        lambda: f"Dinning Hall",
        lambda: f"{RoomJunk.rand_troop()}'s Barracks",
        lambda: f"Hot Spring Bath",
        lambda: f"Horse Stable",
        lambda: f"Mythical Beast Stable",
        lambda: f"Wizard Spire",
        lambda: f"Wizard's Component Pantry",
        lambda: f"Scribe's Hall of Many Desks",
        lambda: f"Artificer's Workshop",
        lambda: f"Alchemy Lab",
        lambda: f"Iron Forge",
        lambda: f"Chamber of Summoning",
        lambda: f"Lavish Bedroom",
        lambda: f"Sewer Tunnel Junction",
        lambda: f"Arboretum",
        lambda: f"Storage Room",
        lambda: f"Wine Cellar",
        lambda: f"Ritual Chamber",
        lambda: f"Observatory",
        lambda: f"Lavatory",
        lambda: f"Game Room",
        lambda: f"Scientific Laboratory",
        lambda: f"Embalming Room",
        lambda: f"Panic Room",
    ))

    _exits = QuantumMonty((
        lambda: f"{RoomJunk.rand_direction()} hallway to the next room.",
        lambda: f"{RoomJunk.rand_direction()} tunnel to the next room.",
        lambda: f"{RoomJunk.rand_direction()} {RoomJunk.bridge_materials.front_linear()} bridge to the next room.",
        lambda: f"wooden stairway to the next room.",
        lambda: f"metal stairway to the next room.",
        lambda: f"carved stone stairway to the next room.",
        lambda: f"{rand_color()} inlaid tile stairway to the next room.",
        lambda: f"magic portal to the next room.",
    ))

    _doors = QuantumMonty((
        lambda: f"Wooden Door, {RoomJunk.rand_door_cond.front_gauss()}",
        lambda: f"Heavy Wooden Door, {RoomJunk.rand_door_cond.front_linear()}",
        lambda: f"Carved Wooden Door, {RoomJunk.rand_door_cond.front_linear()}",
        lambda: f"Studded Wooden Door, {RoomJunk.rand_door_cond.front_linear()}",
        lambda: f"Stone Archway",
        lambda: f"Bronze Portcullis, {RoomJunk.rand_door_cond.quantum_monty()}",
        lambda: f"Solid Iron Gate, {RoomJunk.rand_door_cond.quantum_monty()}",
        lambda: f"Ornate Iron Gate, {RoomJunk.rand_door_cond.quantum_monty()}",
        lambda: f"Inscribed Wooden Door, {RoomJunk.rand_door_cond.quantum_monty()}",
        lambda: f"Hidden Trapdoor in the floor",
        lambda: f"Hidden Trapdoor in the ceiling",
        lambda: f"Secret Door",
        lambda: f"Gold Inlaid Wooden Door, {RoomJunk.rand_door_cond.back_linear()}",
        lambda: f"Etched Silver Door, {RoomJunk.rand_door_cond.back_linear()}",
        lambda: f"Solid Gold Gateway, {RoomJunk.rand_door_cond.back_gauss()}",
    ))

    _sizes = QuantumMonty((
        lambda: f"rectangle, {d(6) * 12} x {-3 + d(6) * 12} hands",
        lambda: f"square, {d(6) * 12} hands across",
        lambda: f"hexagon, {d(6) * 12} hands across",
        lambda: f"octagon, {d(6) * 12} hands across",
        lambda: f"decagon, {d(6) * 12} hands across",
        lambda: f"dodecagon, {d(8) * 8} hands across",
        lambda: f"circular, {dice(2, 5) * 10} hands across",
    ))

    _details = QuantumMonty((
        lambda: f"This room appears empty except for a thick coat of dust on the floor.",
        lambda: f"This room appears empty except for various broken bones scattered around the room.",
        lambda: f"This room appears empty except for blood dripping from the ceiling.",
        lambda: f"This room appears empty except for scattered bits of broken furniture.",
        lambda: f"Empty {RoomJunk.rand_container()} line the walls of this room.",
        lambda: f"Garbage litters the floor of this room.",
        lambda: f"Garbage litters the floor, a clue about an up-coming villain might be found here: 10% chance.",
        lambda: f"The walls are covered in patches of {rand_color()} mold.",
        lambda: f"The floors are covered in clusters of a {rand_color()} fungus.",
        lambda: f"This room is spotless, a clue about an up-coming villain might be found here: 25% chance.",
        lambda: f"Small woodland creatures live in the piles of garbage scattered throughout this room.",
        lambda: f"This room is under construction, woodworking tools are scattered about.",
        lambda: f"Part of the floor is collapsing under its own weight.",
        lambda: f"Part of the ceiling is collapsing under its own weight.",
        lambda: f"{rand_color().title()} coins are scattered on the floor. "
                f"Upon further inspection one would find them glued in place.",
        lambda: f"The room is lined with magical runes carved into the walls.",
        lambda: f"Everything in this room has been painted a strange {rand_color()} color.",
        lambda: f"This room has a large 'x' painted on the floor in black tar.",
        lambda: f"The walls are covered in mold and mildew, someone has written 'HELP ME' in blood on the far wall.",
        lambda: f"Murky {rand_color()} water, three hands deep, "
                f"covers the floor in this room and the one beyond.",
        lambda: f"Small piles of red dust can be found in this room.",
        lambda: f"The walls of this room are covered in highly advanced mathematical formulae.",
        lambda: f"A diabolic monster once used this room to butcher wayward adventurers.",
        lambda: f"An illusion appears in this room, possibly revealing a clue about the Boss: 25% chance.",
        lambda: f"This room is decorated to look like the inside of a ship at sea.",
        lambda: f"At first this room looks like it was decorated for a grand party, but on closer inspection "
                f"the decorations are actually bits of trash hung around the room by rusty wire.",
        lambda: f"This room was decorated years ago for a party or wedding that never happened.",
        lambda: f"This room has a giant map painted in the center of the floor, "
                f"a significant portion of the map is missing.",
        lambda: f"Murky black water covers the floor in this room. A feral kitten is stranded on floating debris.",
        lambda: f"Mid-century modern with a bi-friendly open relationship floor plan.",
        lambda: f"Empty {RoomJunk.rand_container()} line the walls of this room. "
                f"A narcoleptic rune cat is sleeping in the corner.",
        lambda: f"This room reminds me of grandmother's house... before the 'accident'",
        lambda: f"Empty {RoomJunk.rand_container()} line the walls of this room. "
                f"An invisible tome might be found here: 25% chance.",
        lambda: f"Empty {RoomJunk.rand_container()} line the walls of this room. "
                f"A magic item might be found here: 25% chance. {magic_table_f()}.",
        lambda: f"There are a dozen or more humanoids hanging upside-down from the ceiling, writhing in unison.",
    ))
    random_threat = RelativeWeightedChoice((
        (62, Monster),
        (5, MinionGroup),
        (10, MonsterGroup),
        (3, ItemEncounter),
        (5, Villain),
        (5, random_dungeon_npc),
        (10, random_trap),
    ))
    random_threat_no_traps = RelativeWeightedChoice((
        (62, Monster),
        (5, MinionGroup),
        (10, MonsterGroup),
        (5, Villain),
        (5, random_dungeon_npc),
    ))

    def __init__(self, cr=1, room_name="Any", make_traps=True):
        self.cr = cr
        self.name = self._names() if room_name == "Any" else room_name
        self.detail = self._details.front_linear()
        self.size = self._sizes.front_linear()
        if make_traps:
            self.threat = self.random_threat(self.cr, room_name=self.name)
        else:
            self.threat = self.random_threat_no_traps(self.cr, room_name=self.name)
        self.door = self._doors.front_linear()
        self.exit = self._exits.front_linear()
        if hasattr(self.threat, 'xp'):
            self.xp = self.threat.xp
        else:
            self.xp = 0

    def __repr__(self):
        self.output = (
            f"{self.name}",
            f"Dimensions: {self.size}",
            f"Details: {self.detail}",
            f"{self.threat}",
            f"{self.door}, {self.exit}",
            ""
        )
        return "\n".join(self.output)


class WildArea(Room):
    random_threat = RelativeWeightedChoice((
        (50, Monster),
        (30, MinionGroup),
        (2, MonsterGroup),
        (3, ItemEncounter),
        (1, Villain),
        (10, random_city_npc),
        (1, random_dungeon_npc),
        (1, random_trap),
    ))

    def __repr__(self):
        return f"{self.threat}"


class MinionRoom(Room):
    def __init__(self, cr, room_name="Any", make_traps=True):
        super().__init__(cr, room_name, make_traps)
        self.detail = self._details.front_gauss()
        self.size = self._sizes.front_gauss()
        self.door = self._doors.front_gauss()
        self.exit = self._exits.front_gauss()
        self.threat = MinionGroup(self.cr, self.name)


class VillainRoom(Room):
    def __init__(self, cr, room_name="Any", make_traps=True):
        super().__init__(cr, room_name, make_traps)
        self.detail = self._details.quantum_monty()
        self.size = self._sizes.quantum_monty()
        self.door = self._doors.quantum_monty()
        self.exit = self._exits.quantum_monty()
        self.threat = Villain(self.cr, self.name)


class BossRoom(Room):
    def __init__(self, cr, room_name="Any", make_traps=True):
        super().__init__(cr, room_name, make_traps)
        self.name = "Dungeon Heart" if room_name == "Any" else room_name
        self.detail = self._details.back_linear()
        self.size = self._sizes.back_gauss()
        self.door = self._doors.back_gauss()
        self.exit = self._exits.back_gauss()
        self.threat = Boss(self.cr, self.name)

    def __repr__(self):
        self.output = (
            f"{self.name}",
            f"Dimensions: {self.size}",
            f"Details: {self.detail}",
            f"{self.threat}",
            f"Dungeon Exit: {self.door}, {self.exit.replace('to the next room', 'leads out of the dungeon')} "
        )
        return "\n".join(self.output)


if __name__ == '__main__':
    print()
    staring_cr = cr_adapter(num_players=5, average_level=10, difficulty=2)
    haunted_mansion = (
        MinionRoom(staring_cr, room_name="Entrance"),
        Room(staring_cr),
        Room(staring_cr),
        Room(staring_cr),
        VillainRoom(staring_cr + 1),
        MinionRoom(staring_cr),
        Room(staring_cr),
        Room(staring_cr),
        Room(staring_cr),
        BossRoom(staring_cr + 2),
    )
    for room in haunted_mansion:
        print(room)
