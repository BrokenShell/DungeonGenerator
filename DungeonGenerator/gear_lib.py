from Fortuna import FlexCat, TruffleShuffle, d


fabric = TruffleShuffle(('Silk', 'Linen', 'Cotton', 'Wool', 'Leather'))

basic_gear = FlexCat({
    "Simple Melee Weapon": (
        "Dagger", "Club", "Hand Axe", "Light Hammer", "Mace",
        "Javelin", "Spear", "Quarterstaff", "Greatclub", "Sickle",
    ),
    "Simple Ranged Weapon": (
        "Light Crossbow", "Dart", "Sling", "Shortbow",
    ),
    "Martial Melee Weapon": (
        "Long Sword", "War Pick", "Morningstar", "Flail", "Battleaxe",
        "Warhammer", "Lance", "Trident", "Greatsword", "Greataxe", "Glaive",
        "Halberd", "Maul", "Pike", "Whip", "Scimitar", "Shortsword", "Rapier",
        "Bastard Sword",
    ),
    "Martial Ranged Weapon": (
        "Heavy Crossbow", "Hand Crossbow", "Blowgun", "Longbow",
    ),
    "Costume": (
        lambda: f"{fabric()} Lingerie",
        "Fancy Costume",  "Nun Costume", "Animal Costume", "Monster Costume",
        "Maid Costume", "Vampire Costume", "Beholder Costume", "Ninja Costume",
        "Pirate Costume", "Royal Knight Costume",
    ),
    "Clothing": (
        lambda: f"{fabric()} Robes",
        lambda: f"{fabric()} Hat",
        lambda: f"{fabric()} Gloves",
        lambda: f"{fabric()} Shirt",
        lambda: f"{fabric()} Pants",
        lambda: f"{fabric()} Boots",
        lambda: f"{fabric()} Overcoat",
        "Noble Garb", "Royal Robes", "Villager Garb", "Rag Shirt", "Ball Gown",
        "Highborn Garb", "Kilt", "Apron, Boots, Gloves and Goggles", "Crude Hide",
        "Leather Chaps", "Royal Garb", "Fancy Dress", "Peasant Garb",
    ),
    "Light Armor": (
        "Padded Gambeson", "Leather Jerkin", "Bone Splint Tunic", "Studded Doublet",
    ),
    "Medium Armor": (
        "Chain Mail Shirt", "Ring Mail Tunic", "Scale Mail Suit", "Brigandine",
    ),
    "Heavy Armor": (
        "Plate Mail Suit: Breastplate & Gambeson",
        "Quarter Plate Suit: Breastplate, Gambeson, Gauntlets & Sabatons",
        "Half Plate Suit: Breastplate, Gambeson, Visor Helm, Pauldrons, "
        "Gauntlets & Sabatons",
        "Field Plate Suit: Breastplate, Gambeson, Visor Helm, Gorget, "
        "Pauldrons, Vambraces, Gauntlets, Cuisses Leggings & Sabatons",
    ),
    "Shield": (
        "Tower Shield", "Kite Shield", "Jousting Shield", "Heater Shield",
        "Round Shield", "Buckler",
    ),
    "Ammunition": (
        lambda: f"Quiver of {d(3) * 10} Arrows",
        lambda: f"Quiver of {d(3) * 10} Bolts",
        lambda: f"Bag of {d(3) * 10} Sling Stones",
        lambda: f"Box of {d(3) * 10} Blowgun Darts",
    )
}, key_bias="truffle_shuffle", val_bias="truffle_shuffle")

villager_weapons = TruffleShuffle((
    "Bone Cleaver", "Bowie Knife", "Butcher Knife", "Timber Axe", "Jeweler's Hammer", "Sledge Hammer", "Smith's Hammer",
    "Hunting Spear", "Herb Knife", "Bullwhip", "Pitchfork", "Garden Shovel", "Meat Tenderizer", "Bent Lead Pipe",
    "Matching Bronze Bookends", "Rolling Pin", "Wooden Spoon", "Yard Rake", "Brass Candle Holder", "Camp Axe",
    "Iron Frying Pan", "Bronze Cauldron", "Walking Stick", "Trophy Longsword", "Letter Opener",
    "Broken Axe Handle", "Wooden Stake", "Rusty Shank", "Rake", "Shearing Blade",
))

random_material = TruffleShuffle((
    "Platinum", "Golden", "Silver", "Bronze", "Copper", "Mithral", "Vorpal",
    "Ruby", "Emerald", "Diamond", "Amethyst", "Onyx", "Topaz", "Moonstone", "Sun Stone",
    "Quartz", "Tiger Eye", "Magic", "Broken", "Cursed", "Abyssal",
    "Flame", "Frost", "Storm", "Stone",
))

caster_weapons = TruffleShuffle((  # mage weapons
    "Ceremonial Athame", "Harvester's Boline", "Ritual Scepter", "Gnarled Walking Staff",
    "Garden Sickle", "Incense Brazier", "Ceremonial Spear", "Rune Sword",
    "Reaper Scythe", "Skull on a Chain", "Spirit Totem", "Ritual Doll",
    "Stolen Spell Book", "Iron Bond Tome", "Magical Tome", "Magical Rug",
    lambda: f"{random_material()} Wand",
    lambda: f"{random_material()} Staff",
    lambda: f"{random_material()} Necklace",
    lambda: f"{random_material()} Ring",
    lambda: f"{random_material()} Bottle",
    lambda: f"{random_material()} Sword",
    lambda: f"{random_material()} Chalice",
    lambda: f"{random_material()} Rod",
))

main_hand_weapons = TruffleShuffle((  # one-handed, Fighters
    "Rapier", "Longsword", "Falchion", "Saber", "Pick", "Flail", "Gladius", "Axe", "Hammer", "Mace",
    "Bastard Sword", "Battleaxe", "War Pick", "Morningstar", "Warhammer", "Spear",
))

off_hand_weapons = TruffleShuffle((  # typically dual wielded, Rogues, dex
    "Dagger", "Axe", "Hammer", "Mace", "Sickle", "Scimitar", "Gladius", "Flail", "Sword", "Cat-of-nine-tails",
    "Blackjack", "Club", "Broken Bottle",
))

off_hand_shield = TruffleShuffle((
    "Tower Shield", "Kite Shield", "Jousting Shield", "Heater Shield", "Round Shield", "Buckler", "Duelist Cloak",
))

versatile_weapons = TruffleShuffle((  # typically used with a shield, Fighters
    "Bastard Sword", "Battleaxe", "War Pick", "Morningstar", "Warhammer", "Spear",
))

two_hand_weapons = TruffleShuffle((  # two-handed only, Fighters or Knights
    "Greatsword", "Greataxe", "Great Warhammer", "Executioner's Axe", "Zweihänder", "Claymore",
    "Spiked Greatclub", "Double-sided Scimitar", "War Scythe", "Blade Staff",
))

pole_weapons = TruffleShuffle((  # Knight's lance
    "Lance", "War Spear", "Halberd", "Pike", "Poleaxe", "Trident", "Glaive", "Dragon Lance",
))

thrown_weapons = TruffleShuffle((  # archer main weapons
    "Throwing Knives", "Throwing Axes", "Pilum", "Javelin", "Spear",
))

bow_weapons = TruffleShuffle((
    "Heavy Crossbow", "Longbow", "Elven Bow", "Pair of Hand-crossbows", "Scorpion Batista",
))

favorite_str_weapon = TruffleShuffle((
    pole_weapons,
    two_hand_weapons,
    versatile_weapons,
    main_hand_weapons,
))

favorite_dex_weapon = TruffleShuffle((
    thrown_weapons,
    versatile_weapons,
    main_hand_weapons,
    off_hand_weapons
))

armor_by_ac = {
    5: (
        "Costume", "Noble", "Royal", "Gown", "Dress", "Fancy", "Highborn",
    ),
    8: (
        "Naked", "Lingerie", "Monk", "Rag", "Peasant", "Cotton", "Linen",
    ),
    9: (
        "Villager", "Kilt", "Apron", "Silk", "Wool",
    ),
    10: (
        "Hide", "Leather", "Padded",
    ),
    11: (
        "Jerkin", "Splint", "Studded",
    ),
    12: (
        "Chain", "Ring", "Scale",
    ),
    13: (
        "Plate Mail", "Brigandine",
    ),
    14: (
        "Quarter Plate",
    ),
    15: (
        "Half Plate",
    ),
    16: (
        "Field Plate",
    ),
}

armor_bonus_gear = {
    "Visor Helm", "Gorget", "Pauldrons", "Vambraces", "Gauntlets", "Cuisses Leggings", "Sabatons",
    "Tower Shield", "Kite Shield", "Jousting Shield", "Heater Shield", "Round Shield", "Shield",
    "Buckler", "Duelist Cloak",
}


if __name__ == "__main__":
    print(basic_gear.cat_keys)
