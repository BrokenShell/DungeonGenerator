from Fortuna import *
from DungeonGenerator.treasure import magic_table_i, magic_table_h


damage_type_cat = {
    "hacking": (
        "Hacking", "Axe", "Broken", "Horned One", "Battleaxe", "Greataxe", "Zweihänder",
        "Greatsword", "Halberd", "Scythe"
    ),
    "slashing": (
        "Slashing", "Blade", "Razor", "Glaive", "Sword", "Scimitar", "Longsword", "Falchion",
        "Gladius", "Saber", "Katana", "Poleaxe", "Whip", "Cleaver", "Bullwhip", "Boline", "Shortsword"
    ),
    "piercing": (
        "Piercing", "Hook", "Spike", "Barb", "Archer", "Ranger", "Horn", "Knife", "Knives", "Pick",
        "Javelin", "Dagger", "Longbow", "Crossbow", "Shortbow", "Spear", "Pilum", "Athame",
        "Sickle", "Rapier", "Lance", "Trident", "Dart", "Pike", "Rapier", "Pitchfork", "Shank", "Stake"
    ),
    "bludgeoning": (
        "Bludgeoning", "Hammer", "Fist", "Defender", "Guardian", "Mace", "Warhammer", "Sling",
        "Morningstar", "Flail", "Scepter", "Greatclub", "Club", "Quarterstaff", "Maul",
        "Shovel", "Tenderizer", "Pipe", "Bookends", "Rolling Pin", "Unarmed", "Cane"
    ),
    "fire": (
        "Fire", "Flame", "Magma", "Heat", "Red", "Ruby", "Burning", "Smoldering",
        "Lava", "Flaming", "Brazier",
    ),
    "frost": ("Frost", "Frozen", "Cold", "Ice", "Snow", "Water", "White", "Diamond", "Yeti"),
    "lightning": ("Lightning", "Electric", "Storm", "Blue", "Sapphire", "Cloud", "Thunder"),
    "acid": ("Acid", "Corrosion", "Bile", "Green", "Emerald"),
    "poison": ("Poison", "Toxic", "Assassin", "Viper"),
    "shadow": ("Shadow", "Darkness", "Negative", "Black", "Onyx", "Dark", "Displacer Beast"),
    "radiant": ("Radiant", "Sun", "Light", "Life", "Gold"),
    "unholy": ("Unholy", "Fallen", "Voodoo", "Devil", "Dark", "Grave", "Pestilence"),
    "necrotic": (
        "Necrotic", "Mummy", "Lich", "Demilich", "Zombie", "Vampire", "Banshee", "Ghost", "Reaper",
        "Corrupted", "Hell", "Necro", "Death", "Infect", "Corrupt", "Nightmare",
    ),
    "nature": ("Nature", "Druid", "Tree", "Rose"),
    "holy light": ("Holy", "Angel", "Celestial", "Heaven"),
    "crushing": ("Crushing", "Behemoth", "Giant", "Bone", "Shield"),
    "Physical": ("Fighter", "Barbarian", "Gladiator", "Rogue", "Pirate", "Beast", "Acrobat", "Valkyrie"),
    "Arcane": (
        "Arcane", "Wizard", "Warlock", "Sorcerer", "Sorceress", "Mage", "Enchantress", "Enchanter",
        "Alchemist", "Shaman", "Witch", "Tome", "Wand", "Rod", "Staff"
    ),
    "Divine": ("Cleric", "Priest", "Priestess", "Paladin", "Zealot", "Cult", "Acolyte", "Divine", "Inquisitor")
}

motivation = TruffleShuffle((
    'Food',
    'Pride',
    'Revenge',
    'Anxiety',
    'Madness',
    'Jealousy',
    'Greed',
    'Survival',
    'Freedom',
    'Hatred and malice',
    'Delusions of grandeur',
    'Trying to take over the world',
    'Self loathing',
    'Trying to conquer the dungeon',
    lambda: f'Looking for a missing {"item: " + magic_table_h() if percent_true(50) else "NPC"}',
    'Trying to slay a rival',
    'Hiding from enemies',
    'Recovering from battle',
    'Avoiding danger',
    'Seeking wealth',
    'Defending its lair',
    'Trying to hibernate',
    'Setting a trap for the party',
    'Trying to remember a magic word',
    'Fear of superficial differences',
    lambda: f'{"Paid" if percent_true(50) else "Coerced"} to assassinate the party',
    'Preparing to ambush the party',
    lambda: f'Trying to protect an {"item: " + magic_table_i() if percent_true(25) else "NPC"}',
    lambda: f'Trying to contact a deceased {"family member" if percent_true(30) else "lover"}',
    "Recently and almost by chance this creature suddenly realized that life is just a game of dice "
    "and decided to go on a murderous rampage starting with you.",
    'Under the effects of a charm spell or love potion.',
    'Still trying to makeup for past choices and come to terms with this whole "be an adult" thing.',
    'Schizophrenia with suicidal tenancies and a twist of too much testosterone, mix well serve with ice.',
    'General paranoia and mild depression, no family, symptoms exhibited during the study include '
    'sporadic outbursts of senseless violence and random acts of brilliant poetry to no one listening. '
    'Patient often refuses medication and has shown no desire to cooperate. Perfect candidate for the program!',
    'Obsessed with puppet shows about cats',
    'Conviction in a false or dieing faith',
    'Brainwashed to believe the media is the enemy and foreigners are evil',
    'Feelings of impedance or inadequacy among peers',
    'Sexual frustration',
    'Rare mating ritual',
    "Trying to impress an unavailable parental figure who can't be bothered to pay attention to anything but "
    "ogre ball and that damn political puppet show.",
))

rand_elemental = TruffleShuffle((
    "Fire",
    "Water",
    "Lightning",
    "Smoke",
    "Mud",
    "Steam",
    "Ice",
    "Magma",
    "Dust",
))

rand_color = FlexCat({
    "chromatic": (
        "Red",
        "Green",
        "Blue",
        "Black",
        "White",
        "Shadow",
    ),
    "crystal": (
        "Ruby",
        "Emerald",
        "Sapphire",
        "Quartz",
        "Diamond",
        "Onyx",
    ),
    "metal": (
        "Brass",
        "Copper",
        "Bronze",
        "Silver",
        "Gold",
        "Platinum",
    )
}, key_bias="front_gauss", val_bias="front_linear")

rand_knight = TruffleShuffle((
    "Flaming Tongue",
    "Frozen Waste",
    "Drunken Monkey",
    "Hidden Rose",
    "Thunderbolts",
    "Shadows",
    "Broken Lance",
    "Grim Reaper",
    "Three-eyed Raven",
))

rand_adventurer = TruffleShuffle((
    lambda: f"Fighter",
    lambda: f"Rogue",
    lambda: f"Beast Master",
    lambda: f"Archer",
    lambda: f"Cleric",
    lambda: f"Wizard",
    lambda: f"Warlock" if percent_true(50) else f"Witch",
    lambda: f"Sorceress" if percent_true(50) else f"Sorcerer",
    lambda: f"Barbarian" if percent_true(50) else f"Valkyrie",
    lambda: f"Dark Paladin",
    lambda: f"Demonic Summoner",
    lambda: f"Enchantress" if percent_true(50) else f"Enchanter",
    lambda: f"Voodoo Witch Doctor",
    lambda: f"Wild Mage",
    lambda: f"Knight of the {rand_knight()}",
    lambda: f"Defender",
    lambda: f"Acolyte",
    lambda: f"Priestess" if percent_true(50) else f"Priest",
    lambda: f"Zealot",
    lambda: f"Cultist",
    lambda: f"Gladiator",
    lambda: f"Pirate",
    lambda: f"Ninja",
    lambda: f"Alchemist",
    lambda: f"Artificer",
    lambda: f"Shaman",
    lambda: f"Blood Witch",
    lambda: f"Necromancer",
    lambda: f"Arcane Trickster",
    lambda: f"Acrobat",
    lambda: f"Assassin",
    lambda: f"Inquisitor",
))


rand_giant = TruffleShuffle((
    'Hill',
    'Stone',
    'Cloud',
    'Frost',
    'Fire',
    'Storm',
    'Two-headed',
))

rand_race = QuantumMonty((
    "Human",
    "Dwarf",
    "Halfling",
    "Gnome",
    "Elf",
    "Half-elf",
    "Drow",
    "Tiefling",
    "Dragonborn",
    "Half-orc",
    "Goblin",
    "Orc",
    "Half-giant",
    "Half-dragon",
)).front_linear


rand_devil = TruffleShuffle((
    "Flames",
    "Ice",
    "Barbs",
    "Bones",
    "Chains",
    "Blades",
    "Hooks",
    "the Horned One",
))

rand_lycanthrope = QuantumMonty((
    "Werewolf",
    "Wererat",
    "Werecat",
    "Wereboar",
    "Werebear",
    "Werecheetah",
    "Werepanther",
    "Weretiger",
    "Werelion",
)).front_linear

hydra_heads = QuantumMonty((
    "Three",
    "Four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
))

random_monster = FlexCat({
    'minion': (
        lambda: f"Novice {rand_adventurer()}",
        lambda: f"{rand_elemental()} Mephit",
        lambda: f"Zombie {rand_race()}",
        lambda: f"Troll",
        lambda: f"Ogre",
        lambda: f"Jackalope",
        lambda: f"Imp",
        lambda: f"Skeleton {rand_adventurer()}",
        lambda: f"Quasit",
        lambda: f"Gremlin",
        lambda: f"Kobold",
        lambda: f"Gnoll",
        lambda: f"Gelatinous Cube",
        lambda: f"Drider",
        lambda: f"Tasmanian Devil",
        lambda: f"Crawling Claw",
        lambda: f"Vampire Spawn, {rand_race()}",
        lambda: f"Gargoyle",
        lambda: f"Hell Hound",
        lambda: f"Gelatinous Spores",
        lambda: f"Sasquatch",
        lambda: f"Yeti",
        lambda: f"{rand_color()} Dragon Hatchling",
    ),
    'monster': (
        lambda: f"Goblin {rand_adventurer()}",
        lambda: f"{rand_elemental()} Elemental",
        lambda: f"{rand_giant()} Giant",
        lambda: f"Chimera",
        lambda: f"Demon Cat",
        lambda: f"Basilisk",
        lambda: f"Lycanthrope: {rand_lycanthrope()}",
        lambda: f"Hobgoblin",
        lambda: f"Cyclops",
        lambda: f"Umber Hulk",
        lambda: f"Bugbear",
        lambda: f"Owlbear",
        lambda: f"Winged Kobold",
        lambda: f"Cave Troll",
        lambda: f"Ghost: {rand_race()}",
        lambda: f"Displacer Beast",
        lambda: f"Gelatinous Sphere",
        lambda: f"Golem",
        lambda: f"Shield Guardian",
        lambda: f"Wyvern",
        lambda: f"Wraith",
        lambda: f"Intellect Devourer",
        lambda: f"Ghoul",
        lambda: f"Shadow",
        lambda: f"Rust Monster",
        lambda: f"Vampire, {rand_race()}",
        lambda: f"Worg",
        lambda: f"Hook Horror",
        lambda: f"Mimic",
        lambda: f"Flameskull",
        lambda: f"Xorn",
        lambda: f"Bafu",
        lambda: f"Chupacabra",
        lambda: f"Skeletal Monstrosity",
        lambda: f"Young {rand_color()} Dragon",
        lambda: f"Nightmare",
        lambda: f"Bile Demon",
    ),
    'villain': (
        lambda: f"{rand_race()} {rand_adventurer()}",
        lambda: f"{rand_elemental()} Demon",
        lambda: f"Incubus" if percent_true(30) else f"Succubus",
        lambda: f"Doppelganger: {rand_race()} {rand_adventurer()}",
        lambda: f"Wailing Banshee",
        lambda: f"{'Goblin' if percent_true(50) else 'Gnomish'} War Tank",
        lambda: f"Devil of {rand_devil()}",
        lambda: f"Legendary Lycanthrope: {rand_lycanthrope()} {rand_adventurer()}",
        lambda: f"Efreeti",
        lambda: f"Mummy",
        lambda: f"Elder Vampire, {rand_race()}",
        lambda: f"Death Tyrant",
        lambda: f"Demilich",
        lambda: f"Mind Flayer",
        lambda: f"Adult {rand_color()} Dragon",
        lambda: f"Legendary {rand_race()} {rand_adventurer()}",
    ),
    'boss': (
        lambda: f"Hydra with {hydra_heads()} heads",
        lambda: f"The Rat King",
        lambda: f"Behemoth",
        lambda: f"Cerberus",
        lambda: f"Arch Devil of {rand_devil()}",
        lambda: f"Poltergeist",
        lambda: f"Death Knight",
        lambda: f"Pit Lord",
        lambda: f"Vampire Lord, {rand_race()}",
        lambda: f"Mummy Lord",
        lambda: f"Beholder",
        lambda: f"Ancient {rand_color()} Dragon",
        lambda: f"Ancient Dracolich",
    ),
    'campaign boss': (
        lambda: f"Elemental Lord of {rand_elemental()}",
        lambda: f"Goblin King",
        lambda: f"Balor",
        lambda: f"Legendary Devil of {rand_devil()}",
        lambda: f"Mummy Pharaoh",
        lambda: f"Lich King",
        lambda: f"Beholder Overseer",
        lambda: f"Legendary Vampire: {rand_race()} {rand_adventurer()}",
        lambda: f"Lord of the Pit",
        lambda: f"Grim Reaper",
        lambda: f"Flying Spaghetti Monster",
        lambda: f"Legendary {rand_color()} Dragon",
        lambda: f"The Nameless One",
    ),
})


random_undead = FlexCat({
    'minion': (
        lambda: f"Grave Robber",
        lambda: f"Zombie {rand_race()}",
        lambda: f"Crawling Claw",
        lambda: f"Vampire Spawn {rand_race()}",
        lambda: f"Gargoyle",
        lambda: f"Hell Hound",
        lambda: f"Mimic",
        lambda: f"Shadow",
        lambda: f"Pestilence Rat",
        lambda: f"Skeleton {rand_adventurer()}",
    ),
    'monster': (
        lambda: f"Ghost: {rand_race()} {rand_adventurer()}",
        lambda: f"Displacer Beast",
        lambda: f"Wraith",
        lambda: f"Ghoul",
        lambda: f"Shadow",
        lambda: f"Worg",
        lambda: f"Demon Cat",
        lambda: f"Skeletal Monstrosity",
        lambda: f"Vampire: {rand_race()}",
    ),
    'villain': (
        lambda: f"Doppelganger: {rand_race()} {rand_adventurer()}",
        lambda: f"Legendary Ghost: {rand_race()} {rand_adventurer()}",
        lambda: f"Corrupted Nun",
        lambda: f"Dark Summoner",
        lambda: f"Banshee",
        lambda: f"Nightmare",
        lambda: f"Mummy",
        lambda: f"Hook Horror",
        lambda: f"Flameskull",
        lambda: f"Grave Dust Elemental",
        lambda: f"Shadow Elemental",
        lambda: f"Lich",
        lambda: f"Elder Vampire, {rand_race()}",
    ),
    'boss': (
        lambda: f"Death Tyrant",
        lambda: f"Demilich",
        lambda: f"Poltergeist",
        lambda: f"Death Knight",
        lambda: f"Shadow Fiend",
        lambda: f"Dracolich",
        lambda: f"Mummy Lord",
        lambda: f"Vampire Lord {rand_race()}",
    ),
    'campaign boss': (
        lambda: f"Legendary Devil of {rand_devil()}",
        lambda: f"Mummy Pharaoh",
        lambda: f"Lich King",
        lambda: f"Lord of the Pit",
        lambda: f"Grim Reaper",
        lambda: f"Shadow Demon",
        lambda: f"Shadow Dragon",
        lambda: f"Legendary Vampire: {rand_race()} {rand_adventurer()}",
    ),
})


corporeal_undead = FlexCat({
    'minion': (
        "Zombie",
        "Crawling Claw",
        "Vampire Spawn",
        "Pestilence Rat",
        "Skeleton",
    ),
    'monster': (
        "Flameskull",
        "Ghoul",
        "Frozen Walker",
        "Skeletal Monstrosity",
        "Fledgling Vampire",
    ),
    'villain': (
        "Mummy",
        "Lich",
        "Vampire",
        "Mummy Lord",
        "Death Knight",
    ),
    'boss': (
        "Death Tyrant",
        "Ancient Vampire",
        "Demilich",
    ),
    'campaign boss': (
        "Mummy Pharaoh",
        "Lich King",
        "Dracolich",
    )
})


incorporeal_undead = FlexCat({
    'minion': (
        "Ghostly Villager",
        "Crawling Mist",
        "Willow-the-wisp",
        "Specter",
    ),
    'monster': (
        "Spectral Beast",
        "Lost Soul",
        "Weeping Apparition",
        "Ghost",
    ),
    'villain': (
        "Tortured Spirit",
        "Shade",
        "Wraith",
        "Banshee",
        "Spectral Giant",
    ),
    'boss': (
        "Wight",
        "Nightmare",
        "Haunted Horror",
    ),
    'campaign boss': (
        "Soul Reaper",
        "Poltergeist",
        "Spectral Dragon",
    ),
}, val_bias="front_linear")
