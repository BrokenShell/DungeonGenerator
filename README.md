# Dungeon Generator Beta

## 100 Room Dungeon
```python
from DungeonGenerator import Dungeon


dungeon = Dungeon(cr=3, dungeon_levels=10)
print(dungeon)
```

```
Dungeon: Manor of the Evil Genius

Dungeon Entrance
Dimensions: rectangle, 12 x 69 hands
Details: This room appears empty except for blood dripping from the ceiling.
Minion Group: Jackalope, CR 1/2
Number Appearing: 2
STR 15 (+2), DEX 15 (+2), INT 12 (+1), WIS 15 (+2), CHA 16 (+3), CON 15 (+2)
Hit Points: 34 each
Armor Class: 13
Attack Bonus: 3
Attack Damage: 2x (1d4 + 2 bludgeoning)
Save DC: 13
XP Value: 100

Heavy Wooden Door, closed and locked, south hallway to the next room.

Room 2, Kitchen
Dimensions: decagon, 72 hands across
Details: Garbage litters the floor of this room.
Monster: Wraith, CR 3
STR 10 (0), DEX 11 (0), INT 10 (0), WIS 12 (+1), CHA 17 (+3), CON 13 (+1)
Hit Points: 114
Armor Class: 13
Attack Bonus: 5
Basic Attack: 1d6 + 2 holy light
Save DC: 13
XP Value: 700
Treasure: 14 Electrum Coins

Ornate Iron Gate, open and unlocked, west polished bronze bridge to the next room.

Room 3, Scientific Laboratory
Dimensions: hexagon, 24 hands across
Details: The floors are covered in clusters of a pink fungus.
Animated Item: Armor +1 plate, CR 3
Hit Points: 106
Armor Class: 14
Attack Bonus: 4
Attack Damage: 1d6 + 2 bludgeoning
XP Value: 700
Treasure: Sentient Armor +1 plate

Ornate Iron Gate, closed and locked, south hallway to the next room.

Room 4, Desecrated Chapel
Dimensions: hexagon, 24 hands across
Details: An illusion appears in this room, possibly revealing a clue about the Boss: 25% chance.
NPC: Poet
Race: Rock Gnome
Appearance: Tattoos
Mannerism: Whispers
STR 13 (+1), INT 10 (0), DEX 9 (-1), WIS 11 (0), CON 20 (+5), CHA 11 (0)
Hit Points: 9
Armor Class: 9
Background: Charlatan, Forgery
Ideal: Friendship. Material goods come and go. Bonds of friendship last forever.
Flaw: I can't resist swindling people who are more powerful than me.

Stone Archway, north eastern hallway to the next room.

Room 5, Dinning Hall
Dimensions: rectangle, 48 x 45 hands
Details: Garbage litters the floor, a clue about an up-coming villain might be found here: 10% chance.
Monster: Goblin Warlock, CR 3
STR 9 (-1), DEX 13 (+1), INT 12 (+1), WIS 12 (+1), CHA 10 (0), CON 12 (+1)
Hit Points: 107
Armor Class: 13
Attack Bonus: 5
Basic Attack: 1d6 + 2 acid
Save DC: 13
XP Value: 700
Treasure: 15 Copper Coins

Studded Wooden Door, closed but unlocked, south eastern rope bridge to the next room.

Room 6, Guard Room
Dimensions: square, 72 hands across
Details: This room is spotless, a clue about an up-coming villain might be found here: 25% chance.
NPC: Adventurer
Class: Fighter, Eldritch Knight
Level: 3
Race: Human: Villager
Appearance: Piercings
STR 13 (+1), DEX 14 (+2), CON 14 (+2), INT 12 (+1), WIS 11 (0), CHA 15 (+2)
Proficiency Bonus: 2
Preferred Weapon: Pick
Hit Points: 28
Armor Class: 17
Attack Bonus: 4
Attack Damage: 1d10 + 2 piercing
Special Attack: 1d6 + 20 crushing and fire
Save DC: 11
Save Proficiencies: STR, CON
Save Modifiers: STR +3, DEX +2, CON +4, INT +1, WIS 0, CHA +2
Skills: Religion INT 3, Insight WIS 2, Athletics STR 3, Sleight of Hand DEX 4
Talent: Great at solving puzzles
Personal Goal: Communicate with the dead
Background: Acolyte, Shelter of the Faithful
Ideal: Change. We must help bring about the changes the gods are constantly working in the world.
Flaw: I am suspicious of strangers and expect the worst of them.
Inventory: Gloves of missile snaring, Quiver of Ehlonna, Wand of fear

Heavy Wooden Door, closed but unlocked, south western hallway to the next room.

Room 7, Goblin Casino
Dimensions: square, 36 hands across
Details: This room appears empty except for various broken bones scattered around the room.
Monster: Mimic, CR 3
STR 13 (+1), DEX 17 (+3), INT 15 (+2), WIS 11 (0), CHA 14 (+2), CON 9 (-1)
Hit Points: 101
Armor Class: 14
Attack Bonus: 4
Basic Attack: 1d6 + 2 void
Save DC: 13
XP Value: 700
Treasure: 2500 Copper Coins, 1316 Silver Coins, 40 Gold Coins, Gems 80 GP

Wooden Door, closed but unlocked, wooden stairway to the next room.

Room 8, Arboretum
Dimensions: hexagon, 48 hands across
Details: An illusion appears in this room, possibly revealing a clue about the Boss: 25% chance.
Monster: Xorn, CR 3
STR 14 (+2), DEX 9 (-1), INT 12 (+1), WIS 12 (+1), CHA 6 (-2), CON 14 (+2)
Hit Points: 109
Armor Class: 13
Attack Bonus: 5
Basic Attack: 1d6 + 2 hacking
Save DC: 13
XP Value: 700
Treasure: 15 Gold Coins

Inscribed Wooden Door, bared from the other side, north tunnel to the next room.

Room 9, Crypt
Dimensions: square, 24 hands across
Details: This room appears empty except for scattered bits of broken furniture.
Monster: Dust Elemental, CR 3
STR 12 (+1), DEX 6 (-2), INT 13 (+1), WIS 13 (+1), CHA 10 (0), CON 10 (0)
Hit Points: 103
Armor Class: 15
Attack Bonus: 3
Basic Attack: 1d6 + 2 negative energy
Save DC: 13
XP Value: 700
Treasure: 9 Silver Coins

Heavy Wooden Door, closed but unlocked, north western tunnel to the next room.

Room 10, Unholy Temple
Dimensions: decagon, 72 hands across
Details: This room appears empty except for scattered bits of broken furniture.
Villain: Doppelganger: Gnome Knight of the Shadows, CR 4
Motivation: Delusions of grandeur
STR 17 (+3), DEX 17 (+3), INT 21 (+5), WIS 17 (+3), CHA 17 (+3), CON 16 (+3)
Proficiency Bonus: 2
Hit Points: 123
Armor Class: 14
Attack Bonus: 5
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 1d8 + 2 shadow
Special Attack Damage: 1d6 + 26 crushing
Special Ability: Stone Gaze. The villain will attempt to turn an opponent in to stone. Usable 3 times per day.
Weakness: Susceptible to positive energy damage.
Save DC: 14
XP Value: 1100
Treasure: 2114 Copper Coins, 1500 Silver Coins, 90 Gold Coins

Solid Gold Gateway, magically sealed, north polished bronze bridge to the next room.

Room 11, Horse Stable
Dimensions: square, 12 hands across
Details: Garbage litters the floor of this room.
Minion Group: Kobold, CR 1/2
Number Appearing: 2
STR 16 (+3), DEX 13 (+1), INT 18 (+4), WIS 17 (+3), CHA 10 (0), CON 12 (+1)
Hit Points: 31 each
Armor Class: 12
Attack Bonus: 4
Attack Damage: 2x (1d4 + 2 hacking)
Save DC: 13
XP Value: 100

Heavy Wooden Door, closed but unlocked, east hallway to the next room.

Room 12, Iron Forge
Dimensions: decagon, 60 hands across
Details: The floors are covered in clusters of a blue fungus.
Monster: Ghost: Gnome, CR 4
STR 9 (-1), DEX 14 (+2), INT 13 (+1), WIS 10 (0), CHA 13 (+1), CON 11 (0)
Hit Points: 119
Armor Class: 16
Attack Bonus: 3
Basic Attack: 1d6 + 2 necrotic
Save DC: 14
XP Value: 1100
Treasure: 12 Silver Coins

Wooden Door, closed but unlocked, green inlaid tile stairway to the next room.

Room 13, Embalming Room
Dimensions: decagon, 60 hands across
Details: The room is lined with magical runes carved into the walls.
Monster: Cyclops, CR 4
STR 12 (+1), DEX 12 (+1), INT 9 (-1), WIS 13 (+1), CHA 12 (+1), CON 7 (-2)
Hit Points: 117
Armor Class: 14
Attack Bonus: 5
Basic Attack: 1d6 + 2 bludgeoning
Save DC: 14
XP Value: 1100
Treasure: 13 Silver Coins

Carved Wooden Door, closed and locked, west tunnel to the next room.

Room 14, Tormented Artist Studio
Dimensions: rectangle, 72 x 33 hands
Details: This room appears empty except for various broken bones scattered around the room.
Minor Trap, CR 4: Electric Trip Wire
Spot & Disarm DC 10
Save vs. WIS DC 11 for half damage.
Damage: 2d4 lightning
Disarm XP: 1100

Carved Wooden Door, closed and locked, metal stairway to the next room.

Room 15, Alchemy Lab
Dimensions: rectangle, 60 x 45 hands
Details: The walls of this room are covered in highly advanced mathematical formulae.
Minion Group: Red Dragon Hatchling, CR 1
Number Appearing: 4
STR 16 (+3), DEX 16 (+3), INT 14 (+2), WIS 14 (+2), CHA 11 (0), CON 17 (+3)
Hit Points: 19 each
Armor Class: 14
Attack Bonus: 2
Attack Damage: 4x (1d4 + 2 fire)
Save DC: 13
XP Value: 200

Wooden Door, closed but unlocked, metal stairway to the next room.

Room 16, Prison Cell
Dimensions: rectangle, 60 x 33 hands
Details: Garbage litters the floor of this room.
Monster: Demon Cat, CR 4
STR 9 (-1), DEX 10 (0), INT 9 (-1), WIS 12 (+1), CHA 8 (-1), CON 13 (+1)
Hit Points: 125
Armor Class: 16
Attack Bonus: 3
Basic Attack: 1d6 + 2 corruption
Save DC: 14
XP Value: 1100
Treasure: 12 Silver Coins

Heavy Wooden Door, closed but unlocked, metal stairway to the next room.

Room 17, Hatchery
Dimensions: square, 60 hands across
Details: Part of the floor is collapsing under its own weight.
Monster: Cave Troll, CR 4
STR 13 (+1), DEX 14 (+2), INT 11 (0), WIS 12 (+1), CHA 16 (+3), CON 12 (+1)
Hit Points: 126
Armor Class: 16
Attack Bonus: 3
Basic Attack: 1d6 + 2 bludgeoning
Save DC: 14
XP Value: 1100
Treasure: 24 Copper Coins

Inscribed Wooden Door, bared from this side, south hallway to the next room.

Room 18, Desecrated Altar of Light
Dimensions: octagon, 12 hands across
Details: This room reminds me of grandmother's house... before the 'accident'
Minion Group: Gremlin, CR 1
Number Appearing: 3
STR 15 (+2), DEX 15 (+2), INT 14 (+2), WIS 14 (+2), CHA 14 (+2), CON 13 (+1)
Hit Points: 27 each
Armor Class: 12
Attack Bonus: 4
Attack Damage: 3x (1d4 + 2 frost)
Save DC: 13
XP Value: 200

Stone Archway, east tunnel to the next room.

Room 19, Torture Chamber
Dimensions: rectangle, 12 x 69 hands
Details: Cyan coins are scattered on the floor. Upon further inspection one would find them glued in place.
Minor Trap, CR 4: Deep Pit
Spot & Disarm DC 10
Save vs. DEX DC 11 for half damage.
Damage: 2d4 falling
Disarm XP: 1100

Solid Iron Gate, magically sealed, wooden stairway to the next room.

Room 20, Wizard Spire
Dimensions: square, 36 hands across
Details: The walls of this room are covered in highly advanced mathematical formulae.
Villain: Demilich, CR 5
Motivation: Defending its lair
STR 11 (0), DEX 10 (0), INT 23 (+6), WIS 15 (+2), CHA 11 (0), CON 15 (+2)
Proficiency Bonus: 3
Hit Points: 137
Armor Class: 14
Attack Bonus: 6
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 1d8 + 3 necrotic
Special Attack Damage: 1d6 + 32 bludgeoning
Special Ability: Magical Shield. Immune to one damage type of choice for 3 rounds. Usable 3 times per day.
Weakness: Susceptible to hacking damage.
Save DC: 15
XP Value: 1800
Treasure: 1800 Copper Coins, 4000 Silver Coins, 40 Electrum Coins, 2300 Gold Coins, 100 Platinum Coins, Gems 500 GP

Carved Wooden Door, closed but unlocked, magic portal to the next room.

Room 21, Storage Room
Dimensions: rectangle, 36 x 21 hands
Details: This room is under construction, woodworking tools are scattered about.
Minion Group: Gelatinous Cube, CR 1
Number Appearing: 4
STR 18 (+4), DEX 16 (+3), INT 18 (+4), WIS 16 (+3), CHA 17 (+3), CON 12 (+1)
Hit Points: 20 each
Armor Class: 14
Attack Bonus: 2
Attack Damage: 4x (1d4 + 2 hell fire)
Save DC: 13
XP Value: 200

Wooden Door, closed but unlocked, south tunnel to the next room.

Room 22, Lavatory
Dimensions: decagon, 12 hands across
Details: Empty purple crates line the walls of this room.
Monster: Bugbear, CR 5
STR 7 (-2), DEX 13 (+1), INT 14 (+2), WIS 10 (0), CHA 10 (0), CON 11 (0)
Hit Points: 131
Armor Class: 13
Attack Bonus: 7
Basic Attack: 1d6 + 3 corruption
Save DC: 15
XP Value: 1800
Treasure: 110 Gold Coins

Inscribed Wooden Door, bared from the other side, east hallway to the next room.

Room 23, Guard Room
Dimensions: hexagon, 12 hands across
Details: The room is lined with magical runes carved into the walls.
Animated Item: Ring of invisibility, CR 4
Hit Points: 128
Armor Class: 14
Attack Bonus: 5
Attack Damage: 1d6 + 2 holy fire
XP Value: 1100
Treasure: Sentient Ring of invisibility

Ornate Iron Gate, open and unlocked, west hallway to the next room.

Room 24, Crypt
Dimensions: octagon, 60 hands across
Details: The room is lined with magical runes carved into the walls.
Monster: Fire Elemental, CR 5
STR 14 (+2), DEX 14 (+2), INT 8 (-1), WIS 15 (+2), CHA 10 (0), CON 13 (+1)
Hit Points: 145
Armor Class: 14
Attack Bonus: 6
Basic Attack: 1d6 + 3 fire
Save DC: 15
XP Value: 1800
Treasure: 160 Gold Coins

Studded Wooden Door, bared from this side, carved stone stairway to the next room.

Room 25, Treasury
Dimensions: octagon, 60 hands across
Details: Part of the floor is collapsing under its own weight.
Monster: Chimera, CR 5
STR 14 (+2), DEX 10 (0), INT 13 (+1), WIS 10 (0), CHA 13 (+1), CON 13 (+1)
Hit Points: 132
Armor Class: 14
Attack Bonus: 6
Basic Attack: 1d6 + 3 radiant
Save DC: 15
XP Value: 1800
Treasure: 800 Copper Coins, 7500 Silver Coins, 1850 Gold Coins, 120 Platinum Coins, Jewels 1000 GP

Hidden Trapdoor in the ceiling, south western tunnel to the next room.

Room 26, Commander's Armory
Dimensions: rectangle, 36 x 69 hands
Details: This room appears empty except for various broken bones scattered around the room.
Monster: Hook Horror, CR 5
STR 15 (+2), DEX 16 (+3), INT 16 (+3), WIS 11 (0), CHA 6 (-2), CON 14 (+2)
Hit Points: 145
Armor Class: 13
Attack Bonus: 7
Basic Attack: 1d6 + 3 piercing
Save DC: 15
XP Value: 1800
Treasure: 170 Gold Coins

Inscribed Wooden Door, closed and locked, east tunnel to the next room.

Room 27, Iron Forge
Dimensions: square, 36 hands across
Details: The floors are covered in clusters of a magenta fungus.
Minor Trap, CR 5: Cloud of Daggers
Spot & Disarm DC 10
Save vs. CON DC 11 for half damage.
Damage: 3d4 slashing
Disarm XP: 1800

Stone Archway, west tunnel to the next room.

Room 28, Backstage Dressing Room
Dimensions: rectangle, 24 x 21 hands
Details: This room appears empty except for blood dripping from the ceiling.
Monster: Basilisk, CR 5
STR 10 (0), DEX 9 (-1), INT 17 (+3), WIS 12 (+1), CHA 10 (0), CON 13 (+1)
Hit Points: 135
Armor Class: 13
Attack Bonus: 7
Basic Attack: 1d6 + 3 shadow
Save DC: 15
XP Value: 1800
Treasure: 120 Gold Coins

Stone Archway, south tunnel to the next room.

Room 29, Wine Cellar
Dimensions: square, 72 hands across
Details: Small piles of red dust can be found in this room.
Monster: Nightmare, CR 5
STR 15 (+2), DEX 12 (+1), INT 12 (+1), WIS 13 (+1), CHA 14 (+2), CON 12 (+1)
Hit Points: 139
Armor Class: 14
Attack Bonus: 6
Basic Attack: 1d6 + 3 necrotic
Save DC: 15
XP Value: 1800
Treasure: 2100 Silver Coins, 90 Gold Coins

Solid Iron Gate, bared from this side, east hallway to the next room.

Room 30, Tormented Artist Studio
Dimensions: decagon, 48 hands across
Details: A diabolic monster once used this room to butcher wayward adventurers.
Villain: Death Tyrant, CR 6
Motivation: Setting a trap for the party
STR 13 (+1), DEX 16 (+3), INT 14 (+2), WIS 18 (+4), CHA 16 (+3), CON 15 (+2)
Proficiency Bonus: 3
Hit Points: 147
Armor Class: 15
Attack Bonus: 6
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 2d8 + 3 necrotic
Special Attack Damage: 1d6 + 40 thunderbolt
Special Ability: Mind Games. A random opponent is forced to solve a mental puzzle and is stunned for 2 rounds. Some say this is like playing a game with God, but she's playing chess and you're playing checkers. And still, you have no idea why you keep loosing. Usable 3 times per day.
Weakness: The villain is weakened if its true name is spoken aloud within the villain's range of hearing.
Save DC: 15
XP Value: 2300
Treasure: 300 Copper Coins, 10400 Silver Coins, 1660 Gold Coins, 150 Platinum Coins, Gems 450 GP, Philter of love, Potion of greater healing, Potion of resistance

Bronze Portcullis, closed but unlocked, north gold wire bridge to the next room.

Room 31, Prison Cell
Dimensions: hexagon, 72 hands across
Details: This room appears empty except for scattered bits of broken furniture.
Minion Group: Imp, CR 2
Number Appearing: 2
STR 17 (+3), DEX 13 (+1), INT 14 (+2), WIS 9 (-1), CHA 14 (+2), CON 16 (+3)
Hit Points: 43 each
Armor Class: 12
Attack Bonus: 4
Attack Damage: 2x (1d4 + 2 bludgeoning)
Save DC: 13
XP Value: 450

Heavy Wooden Door, closed but unlocked, east hallway to the next room.

Room 32, Hatchery
Dimensions: square, 36 hands across
Details: Everything in this room has been painted a strange orange color.
Villain: Succubus, CR 6
Motivation: Fear of superficial differences
STR 18 (+4), DEX 14 (+2), INT 10 (0), WIS 15 (+2), CHA 16 (+3), CON 16 (+3)
Proficiency Bonus: 3
Hit Points: 160
Armor Class: 16
Attack Bonus: 5
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 2d8 + 3 piercing
Special Attack Damage: 1d6 + 40 divine force
Special Ability: Shadow Step. Once per round as a bonus action, the villain can instantly teleport up to 30 feet. Usable 3 times per day.
Weakness: A hidden object in this room holds the villain's soul.
Save DC: 15
XP Value: 2300
Treasure: 1100 Copper Coins, 9200 Silver Coins, 2350 Gold Coins, 120 Platinum Coins, Jewels 75 GP, Potion of longevity

Studded Wooden Door, closed but unlocked, wooden stairway to the next room.

Room 33, Observatory
Dimensions: square, 36 hands across
Details: This room appears empty except for a thick coat of dust on the floor.
Monster: Worg, CR 6
STR 12 (+1), DEX 14 (+2), INT 16 (+3), WIS 10 (0), CHA 14 (+2), CON 7 (-2)
Hit Points: 149
Armor Class: 15
Attack Bonus: 6
Basic Attack: 2d6 + 3 holy light
Save DC: 15
XP Value: 2300
Treasure: 2100 Silver Coins, 110 Gold Coins

Wooden Door, closed but unlocked, metal stairway to the next room.

Room 34, Prison Workout Room
Dimensions: hexagon, 36 hands across
Details: Part of the ceiling is collapsing under its own weight.
Monster: Cave Troll, CR 6
STR 8 (-1), DEX 15 (+2), INT 13 (+1), WIS 13 (+1), CHA 9 (-1), CON 17 (+3)
Hit Points: 148
Armor Class: 14
Attack Bonus: 7
Basic Attack: 2d6 + 3 slashing
Save DC: 15
XP Value: 2300
Treasure: 150 Gold Coins

Heavy Wooden Door, closed and locked, south western hallway to the next room.

Room 35, Game Room
Dimensions: rectangle, 36 x 21 hands
Details: This room has a giant map painted in the center of the floor, a significant portion of the map is missing.
NPC: Fool
Race: Human: Peasant
Appearance: Birthmark
Mannerism: Stares into the distance
STR 9 (-1), INT 13 (+1), DEX 8 (-1), WIS 8 (-1), CON 9 (-1), CHA 8 (-1)
Hit Points: 3
Armor Class: 9
Background: Folk Hero, Hero of the People
Ideal: Might. If I become strong, I can take what I want—-what I deserve.
Flaw: The tyrant who rules my land will stop at nothing to see me killed.

Heavy Wooden Door, open and unlocked, east hallway to the next room.

Room 36, Mythical Beast Stable
Dimensions: octagon, 72 hands across
Details: This room appears empty except for various broken bones scattered around the room.
Dangerous Trap, CR 6: Spiked Pit
Spot & Disarm DC 12
Save vs. INT DC 15 for half damage.
Damage: 3d6 piercing
Disarm XP: 2300

Wooden Door, closed but unlocked, north western tunnel to the next room.

Room 37, Officer's Barracks
Dimensions: dodecagon, 8 hands across
Details: Small woodland creatures live in the piles of garbage scattered throughout this room.
Monster: Skeletal Monstrosity, CR 6
STR 14 (+2), DEX 11 (0), INT 9 (-1), WIS 8 (-1), CHA 14 (+2), CON 12 (+1)
Hit Points: 156
Armor Class: 16
Attack Bonus: 5
Basic Attack: 2d6 + 3 bludgeoning
Save DC: 15
XP Value: 2300
Treasure: 1000 Copper Coins, 30 Electrum Coins

Stone Archway, carved stone stairway to the next room.

Room 38, Wizard Spire
Dimensions: hexagon, 24 hands across
Details: The walls are covered in mold and mildew, someone has written 'HELP ME' in blood on the far wall.
Monster: Chupacabra, CR 6
STR 15 (+2), DEX 12 (+1), INT 15 (+2), WIS 15 (+2), CHA 13 (+1), CON 8 (-1)
Hit Points: 149
Armor Class: 14
Attack Bonus: 7
Basic Attack: 2d6 + 3 negative energy
Save DC: 15
XP Value: 2300
Treasure: 1600 Silver Coins, 60 Gold Coins

Stone Archway, south tunnel to the next room.

Room 39, Chamber of Summoning
Dimensions: square, 24 hands across
Details: This room appears empty except for blood dripping from the ceiling.
NPC: Acrobat
Race: Human: Peasant
Appearance: Missing teeth
Mannerism: Enunciates overly clearly
STR 6 (-2), INT 11 (0), DEX 8 (-1), WIS 16 (+3), CON 5 (-3), CHA 8 (-1)
Hit Points: 1
Armor Class: 9
Background: Entertainer, Instrumentalist
Ideal: Beauty. When I perform, I make the world better than it was.
Flaw: I'll do anything to win fame and renown.

Hidden Trapdoor in the ceiling, carved stone stairway to the next room.

Room 40, Scientific Laboratory
Dimensions: octagon, 24 hands across
Details: This room has a giant map painted in the center of the floor, a significant portion of the map is missing.
Villain: Legendary Lycanthrope: Werewolf Artificer, CR 7
Motivation: Recovering from battle
STR 15 (+2), DEX 11 (0), INT 14 (+2), WIS 21 (+5), CHA 15 (+2), CON 16 (+3)
Proficiency Bonus: 3
Hit Points: 161
Armor Class: 16
Attack Bonus: 5
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 2d8 + 3 lightning
Special Attack Damage: 1d6 + 45 piercing
Special Ability: Diabolic Genius. The villain fights with an unnatural offensive advantage for the next 3 turns. Usable 3 times per day.
Weakness: An unsolvable riddle reveals how the villain can be defeated.
Save DC: 15
XP Value: 2900
Treasure: 1000 Copper Coins, 14500 Silver Coins, 1540 Gold Coins, 50 Platinum Coins, Gems 800 GP

Solid Iron Gate, bared from the other side, metal stairway to the next room.

Room 41, Lavish Bedroom
Dimensions: rectangle, 24 x 21 hands
Details: This room appears empty except for a thick coat of dust on the floor.
Minion Group: Gnoll, CR 3
Number Appearing: 3
STR 18 (+4), DEX 16 (+3), INT 12 (+1), WIS 14 (+2), CHA 12 (+1), CON 15 (+2)
Hit Points: 36 each
Armor Class: 15
Attack Bonus: 3
Attack Damage: 3x (1d4 + 2 radiant)
Save DC: 13
XP Value: 700

Heavy Wooden Door, bared from this side, north eastern tunnel to the next room.

Room 42, Dinning Hall
Dimensions: octagon, 48 hands across
Details: This room appears empty except for various broken bones scattered around the room.
Animated Item: Rod of lordly might, CR 8
Hit Points: 180
Armor Class: 16
Attack Bonus: 7
Attack Damage: 2d6 + 3 shadow
XP Value: 3900
Treasure: Sentient Rod of lordly might

Hidden Trapdoor in the ceiling, north western rope bridge to the next room.

Room 43, Elite Guard's Training Room
Dimensions: square, 24 hands across
Details: The walls are covered in patches of blue mold.
Epic Trap, CR 8: Putrid Spores
Spot & Disarm DC 18
Save vs. WIS DC 22 for half damage.
Damage: 3d10 necrotic
Disarm XP: 3900

Wooden Door, closed but unlocked, south rope bridge to the next room.

Room 44, Panic Room
Dimensions: decagon, 12 hands across
Details: The walls are covered in mold and mildew, someone has written 'HELP ME' in blood on the far wall.
Monster: Bafu, CR 8
STR 13 (+1), DEX 14 (+2), INT 15 (+2), WIS 7 (-2), CHA 12 (+1), CON 15 (+2)
Hit Points: 181
Armor Class: 15
Attack Bonus: 8
Basic Attack: 2d6 + 3 divine force
Save DC: 16
XP Value: 3900
Treasure: 2500 Silver Coins, 80 Gold Coins

Studded Wooden Door, closed but unlocked, metal stairway to the next room.

Room 45, Arboretum
Dimensions: dodecagon, 56 hands across
Details: At first this room looks like it was decorated for a grand party, but on closer inspection the decorations are actually bits of trash hung around the room by rusty wire.
Monster Group: Young Green Dragon, CR 8
Number Appearing: 3
STR 16 (+3), DEX 9 (-1), INT 12 (+1), WIS 13 (+1), CHA 14 (+2), CON 9 (-1)
Hit Points: 60 each
Armor Class: 17
Attack Bonus: 6
Attack Damage: 3x (2d6 + 3 acid)
Save DC: 16
XP Value: 3900
Treasure: 3500 Copper Coins, 19000 Silver Coins, 40 Electrum Coins, 6970 Gold Coins, 380 Platinum Coins, Gems 1200 GP, Jewels 175 GP, Alchemy jug, Cloak of the manta ray, Potion of resistance, Potion of water breathing

Stone Archway, east hallway to the next room.

Room 46, Unholy Temple
Dimensions: hexagon, 36 hands across
Details: This room is spotless, a clue about an up-coming villain might be found here: 25% chance.
Monster: Golem, CR 8
STR 18 (+4), DEX 8 (-1), INT 13 (+1), WIS 9 (-1), CHA 9 (-1), CON 6 (-2)
Hit Points: 184
Armor Class: 18
Attack Bonus: 5
Basic Attack: 2d6 + 3 corruption
Save DC: 16
XP Value: 3900
Treasure: 1300 Copper Coins, 30 Electrum Coins

Solid Iron Gate, bared from the other side, west tunnel to the next room.

Room 47, Treasury
Dimensions: rectangle, 72 x 21 hands
Details: Yellow coins are scattered on the floor. Upon further inspection one would find them glued in place.
Monster: Two-headed Giant, CR 8
STR 14 (+2), DEX 16 (+3), INT 11 (0), WIS 16 (+3), CHA 14 (+2), CON 8 (-1)
Hit Points: 189
Armor Class: 16
Attack Bonus: 7
Basic Attack: 2d6 + 3 crushing
Save DC: 16
XP Value: 3900
Treasure: 600 Copper Coins, 11400 Silver Coins, 2590 Gold Coins, 80 Platinum Coins, Gems 1000 GP

Carved Wooden Door, closed but unlocked, south rope bridge to the next room.

Room 48, Haunted Auditorium
Dimensions: rectangle, 72 x 57 hands
Details: Garbage litters the floor, a clue about an up-coming villain might be found here: 10% chance.
Monster: Basilisk, CR 8
STR 14 (+2), DEX 12 (+1), INT 11 (0), WIS 13 (+1), CHA 17 (+3), CON 14 (+2)
Hit Points: 190
Armor Class: 16
Attack Bonus: 7
Basic Attack: 2d6 + 3 piercing
Save DC: 16
XP Value: 3900
Treasure: 40 Electrum Coins, 60 Gold Coins

Wooden Door, closed but unlocked, north hallway to the next room.

Room 49, Iron Forge
Dimensions: rectangle, 60 x 9 hands
Details: An illusion appears in this room, possibly revealing a clue about the Boss: 25% chance.
Monster Group: Intellect Devourer, CR 8
Number Appearing: 2
STR 7 (-2), DEX 9 (-1), INT 11 (0), WIS 15 (+2), CHA 17 (+3), CON 13 (+1)
Hit Points: 94 each
Armor Class: 17
Attack Bonus: 6
Attack Damage: 2x (2d6 + 3 divine force)
Save DC: 16
XP Value: 3900
Treasure: 800 Copper Coins, 80 Electrum Coins, 90 Gold Coins

Carved Wooden Door, bared from this side, east tunnel to the next room.

Room 50, Gnomish Workshop
Dimensions: rectangle, 60 x 45 hands
Details: The walls are covered in mold and mildew, someone has written 'HELP ME' in blood on the far wall.
Villain: Legendary Human Blood Witch, CR 9
Motivation: Self loathing
STR 17 (+3), DEX 13 (+1), INT 16 (+3), WIS 16 (+3), CHA 15 (+2), CON 13 (+1)
Proficiency Bonus: 4
Hit Points: 202
Armor Class: 15
Attack Bonus: 8
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 3d8 + 4 acid
Special Attack Damage: 1d6 + 65 radiant
Special Ability: Necromancy. The villain will attempt to raise undead champions to fight the party. Usable 3 times per day.
Weakness: Weapons found in this dungeon deal double damage when used against this villain.
Save DC: 16
XP Value: 5000
Treasure: 200 Copper Coins, 7000 Silver Coins, 1920 Gold Coins, 117 Platinum Coins, Jewels 1250 GP, Eyes of minute seeing, Potion of frost giant strength, Potion of superior healing

Hidden Trapdoor in the floor, south hallway to the next room.

Room 51, Wine Cellar
Dimensions: rectangle, 72 x 69 hands
Details: This room appears empty except for a thick coat of dust on the floor.
Minion Group: Drider, CR 4
Number Appearing: 2
STR 18 (+4), DEX 13 (+1), INT 16 (+3), WIS 17 (+3), CHA 15 (+2), CON 16 (+3)
Hit Points: 63 each
Armor Class: 16
Attack Bonus: 3
Attack Damage: 2x (1d4 + 2 acid)
Save DC: 14
XP Value: 1100

Wooden Door, closed but unlocked, east hallway to the next room.

Room 52, Abandoned Ballroom
Dimensions: square, 60 hands across
Details: Part of the floor is collapsing under its own weight.
Monster: Demon Cat, CR 9
STR 10 (0), DEX 10 (0), INT 8 (-1), WIS 10 (0), CHA 17 (+3), CON 9 (-1)
Hit Points: 199
Armor Class: 16
Attack Bonus: 7
Basic Attack: 3d6 + 4 hacking
Save DC: 16
XP Value: 5000
Treasure: 2200 Silver Coins, 50 Gold Coins

Carved Wooden Door, bared from the other side, metal stairway to the next room.

Room 53, Wizard's Component Pantry
Dimensions: rectangle, 24 x 33 hands
Details: Small woodland creatures live in the piles of garbage scattered throughout this room.
NPC: Adventurer
Class: Barbarian, Path of the Berserker
Level: 9
Race: Human: Peasant
Appearance: Missing fingers
STR 19 (+4), DEX 17 (+3), CON 7 (-2), INT 9 (-1), WIS 12 (+1), CHA 15 (+2)
Proficiency Bonus: 4
Preferred Weapon: Greataxe
Hit Points: 50
Armor Class: 13
Attack Bonus: 9
Attack Damage: 2d10 + 5 hacking
Special Attack: 1d6 + 65 piercing
Save DC: 16
Save Proficiencies: STR, CON
Save Modifiers: STR +8, DEX +3, CON +2, INT -1, WIS +1, CHA +2
Skills: Sleight of Hand DEX 7, Medicine WIS 5, Deception CHA 6, Athletics STR 8
Talent: Knows thieves' cant
Personal Goal: Recover stolen artwork or heirloom
Background: Charlatan, Disguises
Ideal: Independence. I am a free spirit— no one tells me what to do.
Flaw: I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough.
Inventory: Elemental gem, Potion of fire breath, Potion of greater healing, Potion of healing

Ornate Iron Gate, bared from this side, magic portal to the next room.

Room 54, Sewer Tunnel Junction
Dimensions: decagon, 72 hands across
Details: The walls of this room are covered in highly advanced mathematical formulae.
Monster: Vampire, Gnome, CR 9
STR 9 (-1), DEX 15 (+2), INT 10 (0), WIS 6 (-2), CHA 9 (-1), CON 15 (+2)
Hit Points: 192
Armor Class: 16
Attack Bonus: 7
Basic Attack: 3d6 + 4 necrotic
Save DC: 16
XP Value: 5000
Treasure: 160 Gold Coins

Studded Wooden Door, closed but unlocked, north western stone bridge to the next room.

Room 55, Observatory
Dimensions: square, 36 hands across
Details: This room appears empty except for various broken bones scattered around the room.
Monster: Bile Demon, CR 9
STR 8 (-1), DEX 12 (+1), INT 16 (+3), WIS 14 (+2), CHA 13 (+1), CON 14 (+2)
Hit Points: 204
Armor Class: 17
Attack Bonus: 6
Basic Attack: 3d6 + 4 acid
Save DC: 16
XP Value: 5000
Treasure: 150 Gold Coins

Stone Archway, north polished bronze bridge to the next room.

Room 56, Prison Workout Room
Dimensions: rectangle, 72 x 57 hands
Details: This room is under construction, woodworking tools are scattered about.
Villain: Mind Flayer, CR 9
Motivation: Conviction in a false or dieing faith
STR 15 (+2), DEX 13 (+1), INT 7 (-2), WIS 24 (+7), CHA 15 (+2), CON 16 (+3)
Proficiency Bonus: 4
Hit Points: 201
Armor Class: 15
Attack Bonus: 8
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 3d8 + 4 hacking
Special Attack Damage: 1d6 + 65 crushing
Special Ability: Puppet Master. The villain will attempt to control an opponent. The target's body will obey the master in every way for 4 turns. Usable 3 times per day.
Weakness: The villain falls when an ancient enemy forgives them.
Save DC: 16
XP Value: 5000
Treasure: 200 Copper Coins, 11000 Silver Coins, 2490 Gold Coins, 100 Platinum Coins, Gems 1000 GP

Heavy Wooden Door, bared from the other side, east rusty iron bridge to the next room.

Room 57, Desecrated Altar of Light
Dimensions: rectangle, 72 x 45 hands
Details: Everything in this room has been painted a strange green color.
Monster: Mimic, CR 9
STR 13 (+1), DEX 16 (+3), INT 15 (+2), WIS 17 (+3), CHA 14 (+2), CON 14 (+2)
Hit Points: 194
Armor Class: 16
Attack Bonus: 7
Basic Attack: 3d6 + 4 corruption
Save DC: 16
XP Value: 5000
Treasure: 800 Copper Coins, 8800 Silver Coins, 2640 Gold Coins, 120 Platinum Coins, Gems 1400 GP, Brooch of shielding, Pearl of power, Rod of the pact keeper +1, Sword of vengeance

Carved Wooden Door, closed and locked, west stone bridge to the next room.

Room 58, Mythical Beast Stable
Dimensions: hexagon, 60 hands across
Details: This room appears empty except for scattered bits of broken furniture.
Monster: Smoke Elemental, CR 9
STR 12 (+1), DEX 12 (+1), INT 13 (+1), WIS 8 (-1), CHA 13 (+1), CON 9 (-1)
Hit Points: 199
Armor Class: 17
Attack Bonus: 6
Basic Attack: 3d6 + 4 necrotic
Save DC: 16
XP Value: 5000
Treasure: 1400 Copper Coins, 30 Electrum Coins

Hidden Trapdoor in the ceiling, south western tunnel to the next room.

Room 59, Torture Chamber
Dimensions: hexagon, 24 hands across
Details: Cyan coins are scattered on the floor. Upon further inspection one would find them glued in place.
Monster: Chimera, CR 9
STR 9 (-1), DEX 15 (+2), INT 11 (0), WIS 16 (+3), CHA 6 (-2), CON 11 (0)
Hit Points: 199
Armor Class: 17
Attack Bonus: 6
Basic Attack: 3d6 + 4 lightning
Save DC: 16
XP Value: 5000
Treasure: 1400 Silver Coins, 50 Gold Coins

Stone Archway, north hallway to the next room.

Room 60, Scribe's Hall of Many Desks
Dimensions: rectangle, 36 x 57 hands
Details: Mid-century modern with a bi-friendly open relationship floor plan.
Villain: Efreeti, CR 10
Motivation: Trying to take over the world
STR 16 (+3), DEX 17 (+3), INT 15 (+2), WIS 16 (+3), CHA 16 (+3), CON 21 (+5)
Proficiency Bonus: 4
Hit Points: 213
Armor Class: 18
Attack Bonus: 6
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 3d8 + 4 void
Special Attack Damage: 1d6 + 70 crushing
Special Ability: Reflective Carapace. Any time the villain is targeted by a magic missile, or any spell that requires a ranged attack roll, roll a d6. On a roll of 1 to 5, the villain is unaffected, and the spell is safely deflected away. On a roll of 6, the villain is still unaffected, but the spell is reflected back at the caster. Usable 3 times per day.
Weakness: The villain is weakened if the entire party laughs at the villain for a full round.
Save DC: 16
XP Value: 5900
Treasure: 1900 Copper Coins, 5000 Silver Coins, 40 Electrum Coins, 1900 Gold Coins, 90 Platinum Coins, Jewels 50 GP, Oil of slipperiness, Wand of magic detection

Secret Door, carved stone stairway to the next room.

Room 61, Combat Pit Arena
Dimensions: square, 72 hands across
Details: This room appears empty except for various broken bones scattered around the room.
Minion Group: Tasmanian Devil, CR 4
Number Appearing: 3
STR 16 (+3), DEX 18 (+4), INT 5 (-3), WIS 14 (+2), CHA 15 (+2), CON 11 (0)
Hit Points: 43 each
Armor Class: 14
Attack Bonus: 5
Attack Damage: 3x (1d4 + 2 unholy)
Save DC: 14
XP Value: 1100

Wooden Door, closed but unlocked, north eastern hallway to the next room.

Room 62, Scientific Laboratory
Dimensions: octagon, 60 hands across
Details: This room appears empty except for a thick coat of dust on the floor.
NPC: Storyteller
Race: Human: Peasant
Appearance: Formal, clean clothes
Mannerism: Makes constant jokes or puns
STR 13 (+1), INT 6 (-2), DEX 17 (+3), WIS 8 (-1), CON 10 (0), CHA 13 (+1)
Hit Points: 4
Armor Class: 13
Background: Sailor, Ship's Passage
Ideal: Aspiration. Someday I'll own my own ship and chart my own destiny.
Flaw: My pride will probably lead to my destruction.

Inscribed Wooden Door, closed but unlocked, metal stairway to the next room.

Room 63, Desecrated Chapel
Dimensions: dodecagon, 64 hands across
Details: The walls of this room are covered in highly advanced mathematical formulae.
Monster: Cyclops, CR 10
STR 8 (-1), DEX 13 (+1), INT 14 (+2), WIS 15 (+2), CHA 10 (0), CON 13 (+1)
Hit Points: 215
Armor Class: 16
Attack Bonus: 8
Basic Attack: 3d6 + 4 fire
Save DC: 16
XP Value: 5900
Treasure: 1900 Silver Coins, 40 Gold Coins

Solid Iron Gate, open and unlocked, north western polished bronze bridge to the next room.

Room 64, Lavatory
Dimensions: square, 72 hands across
Details: This room has a large 'x' painted on the floor in black tar.
Minion Group: Gelatinous Spores, CR 5
Number Appearing: 4
STR 14 (+2), DEX 18 (+4), INT 17 (+3), WIS 14 (+2), CHA 14 (+2), CON 16 (+3)
Hit Points: 36 each
Armor Class: 13
Attack Bonus: 7
Attack Damage: 4x (1d4 + 3 hacking)
Save DC: 15
XP Value: 1800

Hidden Trapdoor in the ceiling, south western tunnel to the next room.

Room 65, Guard Room
Dimensions: dodecagon, 8 hands across
Details: This room is under construction, woodworking tools are scattered about.
Dangerous Trap, CR 10: Hail Storm
Spot & Disarm DC 12
Save vs. CON DC 15 for half damage.
Damage: 3d6 cold
Disarm XP: 5900

Bronze Portcullis, magically sealed, north eastern hallway to the next room.

Room 66, Goblin Casino
Dimensions: hexagon, 12 hands across
Details: Small piles of red dust can be found in this room.
Monster: Worg, CR 10
STR 15 (+2), DEX 13 (+1), INT 12 (+1), WIS 9 (-1), CHA 15 (+2), CON 17 (+3)
Hit Points: 209
Armor Class: 18
Attack Bonus: 6
Basic Attack: 3d6 + 4 shadow
Save DC: 16
XP Value: 5900
Treasure: 1400 Silver Coins, 70 Gold Coins

Bronze Portcullis, bared from this side, east rope bridge to the next room.

Room 67, Hot Spring Bath
Dimensions: octagon, 48 hands across
Details: Murky purple water, three hands deep, covers the floor in this room and the one beyond.
Minion Group: Jackalope, CR 5
Number Appearing: 4
STR 17 (+3), DEX 17 (+3), INT 16 (+3), WIS 14 (+2), CHA 15 (+2), CON 17 (+3)
Hit Points: 35 each
Armor Class: 14
Attack Bonus: 6
Attack Damage: 4x (1d4 + 3 piercing)
Save DC: 15
XP Value: 1800

Solid Iron Gate, closed but unlocked, metal stairway to the next room.

Room 68, Crypt
Dimensions: rectangle, 36 x 33 hands
Details: The walls are covered in mold and mildew, someone has written 'HELP ME' in blood on the far wall.
Monster: Cave Troll, CR 10
STR 14 (+2), DEX 11 (0), INT 12 (+1), WIS 18 (+4), CHA 10 (0), CON 11 (0)
Hit Points: 220
Armor Class: 15
Attack Bonus: 9
Basic Attack: 3d6 + 4 fire
Save DC: 16
XP Value: 5900
Treasure: 1200 Copper Coins, 60 Electrum Coins

Wooden Door, closed but unlocked, north western hallway to the next room.

Room 69, Bestiary
Dimensions: octagon, 24 hands across
Details: This room is under construction, woodworking tools are scattered about.
Monster Group: Wraith, CR 10
Number Appearing: 2
STR 15 (+2), DEX 12 (+1), INT 12 (+1), WIS 11 (0), CHA 9 (-1), CON 15 (+2)
Hit Points: 108 each
Armor Class: 18
Attack Bonus: 6
Attack Damage: 2x (2d6 + 4 radiant)
Save DC: 16
XP Value: 5900
Treasure: 130 Electrum Coins, 210 Gold Coins

Bronze Portcullis, bared from this side, south tunnel to the next room.

Room 70, Horse Stable
Dimensions: octagon, 72 hands across
Details: This room appears empty except for blood dripping from the ceiling.
Villain: Adult Red Dragon, CR 11
Motivation: Food
STR 12 (+1), DEX 15 (+2), INT 24 (+7), WIS 11 (0), CHA 13 (+1), CON 14 (+2)
Proficiency Bonus: 4
Hit Points: 231
Armor Class: 18
Attack Bonus: 7
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 3d8 + 4 fire
Special Attack Damage: 1d8 + 75 radiant
Special Ability: Horrific Intent. This villain will attempt to cause intense fear, preferring to target casters. A horrified victim is paralyzed with fear for up to 4 rounds. While horrified, a victim develops a speech impediment and can do little more than wet themselves. The paralysis can be negated if an non-fearful ally takes one full turn to snap them out of it. Even so, the victim will be fearful and attack with disadvantage until the Horrify duration ends. Usable 3 times per day.
Weakness: The villain loses its special ability if a mystic bargain it struck long ago is satisfied.
Save DC: 17
XP Value: 7200
Treasure: 20700 Gold Coins, 1660 Platinum Coins, Gems 10000 GP, Ammunition: Box of 20 crossbow bolts +1, Potion of fire breath, Potion of healing, Spell scroll (1st level) Thunderwave, Wand of magic detection

Ornate Iron Gate, bared from the other side, north western hallway to the next room.

Room 71, Carved Marble Great Hall
Dimensions: rectangle, 12 x 21 hands
Details: This room appears empty except for various broken bones scattered around the room.
Minion Group: Kobold, CR 5
Number Appearing: 4
STR 18 (+4), DEX 18 (+4), INT 17 (+3), WIS 18 (+4), CHA 13 (+1), CON 18 (+4)
Hit Points: 33 each
Armor Class: 15
Attack Bonus: 5
Attack Damage: 4x (1d4 + 3 slashing)
Save DC: 15
XP Value: 1800

Wooden Door, closed but unlocked, south eastern tunnel to the next room.

Room 72, Haunted Auditorium
Dimensions: octagon, 12 hands across
Details: Small woodland creatures live in the piles of garbage scattered throughout this room.
Monster: Bugbear, CR 11
STR 9 (-1), DEX 7 (-2), INT 8 (-1), WIS 13 (+1), CHA 6 (-2), CON 8 (-1)
Hit Points: 232
Armor Class: 15
Attack Bonus: 10
Basic Attack: 3d6 + 4 acid
Save DC: 17
XP Value: 7200
Treasure: 600 Gold Coins, 20 Platinum Coins

Ornate Iron Gate, closed and locked, metal stairway to the next room.

Room 73, Backstage Dressing Room
Dimensions: hexagon, 12 hands across
Details: This room appears empty except for various broken bones scattered around the room.
Monster: Displacer Beast, CR 11
STR 11 (0), DEX 8 (-1), INT 7 (-2), WIS 11 (0), CHA 14 (+2), CON 13 (+1)
Hit Points: 228
Armor Class: 18
Attack Bonus: 7
Basic Attack: 3d6 + 4 shadow
Save DC: 17
XP Value: 7200
Treasure: 600 Gold Coins, 30 Platinum Coins

Inscribed Wooden Door, closed and locked, west tunnel to the next room.

Room 74, Shrine of Fortuna
Dimensions: octagon, 36 hands across
Details: This room is under construction, woodworking tools are scattered about.
Deadly Trap, CR 11: Guillotine
Spot & Disarm DC 16
Save vs. INT DC 20 for half damage.
Damage: 4d8 slashing
Disarm XP: 7200

Hidden Trapdoor in the ceiling, south western tunnel to the next room.

Room 75, Tormented Artist Studio
Dimensions: hexagon, 12 hands across
Details: The walls are covered in patches of golden mold.
Monster: Mimic, CR 11
STR 12 (+1), DEX 17 (+3), INT 15 (+2), WIS 12 (+1), CHA 14 (+2), CON 8 (-1)
Hit Points: 229
Armor Class: 17
Attack Bonus: 8
Basic Attack: 3d6 + 4 divine force
Save DC: 17
XP Value: 7200
Treasure: 14700 Gold Coins, 2080 Platinum Coins, Gems 8000 GP, Potion of supreme healing

Hidden Trapdoor in the ceiling, north eastern petrified wood bridge to the next room.

Room 76, Wizard's Component Pantry
Dimensions: square, 48 hands across
Details: This room appears empty except for blood dripping from the ceiling.
Monster: Wyvern, CR 11
STR 14 (+2), DEX 14 (+2), INT 9 (-1), WIS 10 (0), CHA 12 (+1), CON 7 (-2)
Hit Points: 234
Armor Class: 16
Attack Bonus: 9
Basic Attack: 3d6 + 4 holy fire
Save DC: 17
XP Value: 7200
Treasure: 1400 Silver Coins, 600 Gold Coins

Studded Wooden Door, bared from this side, pink inlaid tile stairway to the next room.

Room 77, Observatory
Dimensions: hexagon, 12 hands across
Details: This room appears empty except for scattered bits of broken furniture.
Monster: Chimera, CR 11
STR 12 (+1), DEX 18 (+4), INT 12 (+1), WIS 11 (0), CHA 9 (-1), CON 11 (0)
Hit Points: 233
Armor Class: 17
Attack Bonus: 8
Basic Attack: 3d6 + 4 radiant
Save DC: 17
XP Value: 7200
Treasure: 600 Gold Coins, 10 Platinum Coins

Gold Inlaid Wooden Door, magically sealed, carved stone stairway to the next room.

Room 78, Prison Workout Room
Dimensions: square, 12 hands across
Details: Everything in this room has been painted a strange yellow color.
Monster: Hook Horror, CR 11
STR 10 (0), DEX 14 (+2), INT 14 (+2), WIS 15 (+2), CHA 10 (0), CON 9 (-1)
Hit Points: 235
Armor Class: 16
Attack Bonus: 9
Basic Attack: 3d6 + 4 piercing
Save DC: 17
XP Value: 7200
Treasure: 200 Electrum Coins, 600 Gold Coins

Carved Wooden Door, bared from the other side, east hallway to the next room.

Room 79, Mythical Beast Stable
Dimensions: decagon, 48 hands across
Details: This room appears empty except for scattered bits of broken furniture.
Monster: Lycanthrope: Werecat, CR 11
STR 6 (-2), DEX 15 (+2), INT 15 (+2), WIS 9 (-1), CHA 12 (+1), CON 16 (+3)
Hit Points: 227
Armor Class: 16
Attack Bonus: 9
Basic Attack: 3d6 + 4 slashing
Save DC: 17
XP Value: 7200
Treasure: 600 Gold Coins, 30 Platinum Coins

Solid Iron Gate, open and unlocked, west tunnel to the next room.

Room 80, Torture Chamber
Dimensions: circular, 80 hands across
Details: Murky black water covers the floor in this room. A feral kitten is stranded on floating debris.
Villain: Wailing Banshee, CR 12
Motivation: Sexual frustration
STR 17 (+3), DEX 16 (+3), INT 17 (+3), WIS 12 (+1), CHA 24 (+7), CON 13 (+1)
Proficiency Bonus: 4
Hit Points: 243
Armor Class: 19
Attack Bonus: 6
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 4d8 + 4 necrotic
Special Attack Damage: 1d8 + 80 positive energy
Special Ability: Whirlwind of bludgeoning. Usable 3 times per day.
Weakness: The villain is weakened in the presence of a particular magic item. Shortbow +1.
Save DC: 17
XP Value: 8400
Treasure: 20900 Gold Coins, 1750 Platinum Coins, Jewels 3750 GP, Mantle of spell resistance, Wand of paralysis

Studded Wooden Door, open and unlocked, wooden stairway to the next room.

Room 81, Kitchen
Dimensions: hexagon, 60 hands across
Details: This room appears empty except for a thick coat of dust on the floor.
Minion Group: Gargoyle, CR 5
Number Appearing: 3
STR 16 (+3), DEX 13 (+1), INT 15 (+2), WIS 15 (+2), CHA 13 (+1), CON 16 (+3)
Hit Points: 45 each
Armor Class: 13
Attack Bonus: 7
Attack Damage: 3x (1d4 + 3 shadow)
Save DC: 15
XP Value: 1800

Carved Wooden Door, bared from the other side, east hallway to the next room.

Room 82, Scientific Laboratory
Dimensions: rectangle, 60 x 33 hands
Details: The floors are covered in clusters of a red fungus.
Monster: Umber Hulk, CR 12
STR 11 (0), DEX 8 (-1), INT 11 (0), WIS 16 (+3), CHA 10 (0), CON 9 (-1)
Hit Points: 248
Armor Class: 18
Attack Bonus: 7
Basic Attack: 4d6 + 4 void
Save DC: 17
XP Value: 8400
Treasure: 500 Electrum Coins, 600 Gold Coins

Heavy Wooden Door, closed but unlocked, metal stairway to the next room.

Room 83, Desecrated Chapel
Dimensions: hexagon, 12 hands across
Details: The floors are covered in clusters of a magenta fungus.
Monster: Skeletal Monstrosity, CR 12
STR 13 (+1), DEX 15 (+2), INT 9 (-1), WIS 16 (+3), CHA 11 (0), CON 14 (+2)
Hit Points: 242
Armor Class: 16
Attack Bonus: 9
Basic Attack: 4d6 + 4 acid
Save DC: 17
XP Value: 8400
Treasure: 500 Gold Coins, 90 Platinum Coins

Solid Iron Gate, magically sealed, west hallway to the next room.

Room 84, Lavish Bedroom
Dimensions: octagon, 24 hands across
Details: This room appears empty except for scattered bits of broken furniture.
Monster Group: Goblin Priestess, CR 12
Number Appearing: 3
STR 16 (+3), DEX 12 (+1), INT 13 (+1), WIS 13 (+1), CHA 7 (-2), CON 15 (+2)
Hit Points: 78 each
Armor Class: 17
Attack Bonus: 8
Attack Damage: 3x (3d6 + 4 radiant)
Save DC: 17
XP Value: 8400
Treasure: 300 Electrum Coins, 1800 Gold Coins, 80 Platinum Coins

Wooden Door, closed but unlocked, south rusty iron bridge to the next room.

Room 85, Lavatory
Dimensions: rectangle, 36 x 21 hands
Details: Murky golden water, three hands deep, covers the floor in this room and the one beyond.
NPC: Sentry
Race: Human: Villager
Appearance: Nervous eye twitch
Mannerism: Paces
STR 13 (+1), INT 10 (0), DEX 11 (0), WIS 8 (-1), CON 13 (+1), CHA 9 (-1)
Hit Points: 5
Armor Class: 10
Background: Outlander, Outcast
Ideal: Change. Life is like the seasons, in constant change, and we must change with it.
Flaw: I am too enamored of ale, wine, and other intoxicants.

Heavy Wooden Door, open and unlocked, east tunnel to the next room.

Room 86, Panic Room
Dimensions: hexagon, 48 hands across
Details: A diabolic monster once used this room to butcher wayward adventurers.
Monster: Bile Demon, CR 12
STR 17 (+3), DEX 8 (-1), INT 7 (-2), WIS 16 (+3), CHA 9 (-1), CON 8 (-1)
Hit Points: 240
Armor Class: 19
Attack Bonus: 6
Basic Attack: 4d6 + 4 acid
Save DC: 17
XP Value: 8400
Treasure: 1700 Silver Coins, 200 Gold Coins

Bronze Portcullis, magically sealed, indigo inlaid tile stairway to the next room.

Room 87, Arboretum
Dimensions: hexagon, 72 hands across
Details: This room has a giant map painted in the center of the floor, a significant portion of the map is missing.
Dangerous Trap, CR 12: Acidic Bile
Spot & Disarm DC 12
Save vs. WIS DC 15 for half damage.
Damage: 4d6 acid
Disarm XP: 8400

Wooden Door, closed but unlocked, wooden stairway to the next room.

Room 88, Bestiary
Dimensions: hexagon, 48 hands across
Details: The walls are covered in patches of pink mold.
Monster: Displacer Beast, CR 12
STR 15 (+2), DEX 13 (+1), INT 11 (0), WIS 16 (+3), CHA 11 (0), CON 13 (+1)
Hit Points: 240
Armor Class: 18
Attack Bonus: 7
Basic Attack: 4d6 + 4 shadow
Save DC: 17
XP Value: 8400
Treasure: 900 Gold Coins, 80 Platinum Coins

Wooden Door, closed but unlocked, south hallway to the next room.

Room 89, Treasury
Dimensions: square, 72 hands across
Details: At first this room looks like it was decorated for a grand party, but on closer inspection the decorations are actually bits of trash hung around the room by rusty wire.
Monster: Shield Guardian, CR 12
STR 17 (+3), DEX 11 (0), INT 18 (+4), WIS 8 (-1), CHA 16 (+3), CON 10 (0)
Hit Points: 237
Armor Class: 16
Attack Bonus: 9
Basic Attack: 4d6 + 4 bludgeoning
Save DC: 17
XP Value: 8400
Treasure: 8800 Gold Coins, 1790 Platinum Coins

Hidden Trapdoor in the floor, north rope bridge to the next room.

Room 90, Archer's Armory
Dimensions: decagon, 60 hands across
Details: A diabolic monster once used this room to butcher wayward adventurers.
Villain: Elf Inquisitor, CR 13
Motivation: Revenge
STR 12 (+1), DEX 14 (+2), INT 17 (+3), WIS 14 (+2), CHA 13 (+1), CON 16 (+3)
Proficiency Bonus: 5
Hit Points: 252
Armor Class: 19
Attack Bonus: 7
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 4d8 + 5 holy fire
Special Attack Damage: 1d8 + 85 hacking
Special Ability: Stone Gaze. The villain will attempt to turn an opponent in to stone. Usable 3 times per day.
Weakness: Susceptible to slashing damage.
Save DC: 18
XP Value: 10000
Treasure: 16900 Gold Coins, 2210 Platinum Coins, Jewels 1000 GP, Potion of climbing, Potion of fire breath, Potion of healing, Spell scroll (1st level) Disguise Self

Solid Iron Gate, bared from the other side, yellow inlaid tile stairway to the next room.

Room 91, Gnomish Workshop
Dimensions: rectangle, 60 x 9 hands
Details: This room appears empty except for various broken bones scattered around the room.
Minion Group: Green Dragon Hatchling, CR 6
Number Appearing: 4
STR 17 (+3), DEX 13 (+1), INT 14 (+2), WIS 16 (+3), CHA 16 (+3), CON 11 (0)
Hit Points: 39 each
Armor Class: 14
Attack Bonus: 7
Attack Damage: 4x (1d4 + 3 acid)
Save DC: 15
XP Value: 2300

Heavy Wooden Door, bared from the other side, south hallway to the next room.

Room 92, Tormented Artist Studio
Dimensions: rectangle, 12 x 69 hands
Details: Empty cyan boxes line the walls of this room. An invisible tome might be found here: 25% chance.
Monster: Rust Monster, CR 14
STR 14 (+2), DEX 11 (0), INT 15 (+2), WIS 15 (+2), CHA 13 (+1), CON 13 (+1)
Hit Points: 266
Armor Class: 17
Attack Bonus: 9
Basic Attack: 4d6 + 5 lightning
Save DC: 18
XP Value: 11500
Treasure: 800 Gold Coins, 50 Platinum Coins

Gold Inlaid Wooden Door, open and unlocked, north tunnel to the next room.

Room 93, Abandoned Ballroom
Dimensions: dodecagon, 64 hands across
Details: Garbage litters the floor of this room.
Minion Group: Crawling Claw, CR 7
Number Appearing: 3
STR 14 (+2), DEX 15 (+2), INT 18 (+4), WIS 13 (+1), CHA 8 (-1), CON 18 (+4)
Hit Points: 54 each
Armor Class: 16
Attack Bonus: 5
Attack Damage: 3x (1d4 + 3 bludgeoning)
Save DC: 15
XP Value: 2900

Hidden Trapdoor in the ceiling, east hallway to the next room.

Room 94, Sewer Tunnel Junction
Dimensions: octagon, 72 hands across
Details: Empty purple baskets line the walls of this room.
Monster: Golem, CR 14
STR 12 (+1), DEX 4 (-3), INT 18 (+4), WIS 16 (+3), CHA 15 (+2), CON 15 (+2)
Hit Points: 277
Armor Class: 17
Attack Bonus: 9
Basic Attack: 4d6 + 5 positive energy
Save DC: 18
XP Value: 11500
Treasure: 1200 Gold Coins, 40 Platinum Coins

Secret Door, west wooden bridge to the next room.

Room 95, Hatchery
Dimensions: rectangle, 36 x 21 hands
Details: This room was decorated years ago for a party or wedding that never happened.
Monster: Hook Horror, CR 14
STR 14 (+2), DEX 7 (-2), INT 12 (+1), WIS 11 (0), CHA 15 (+2), CON 13 (+1)
Hit Points: 278
Armor Class: 18
Attack Bonus: 8
Basic Attack: 4d6 + 5 piercing
Save DC: 18
XP Value: 11500
Treasure: 400 Gold Coins, 50 Platinum Coins

Gold Inlaid Wooden Door, closed and locked, wooden stairway to the next room.

Room 96, Observatory
Dimensions: hexagon, 72 hands across
Details: Everything in this room has been painted a strange magenta color.
NPC: Adventurer
Class: Warlock, Fiend Pact of the Chain
Level: 14
Race: Human: Peasant
Appearance: Braided beard or hair
STR 15 (+2), DEX 17 (+3), CON 18 (+4), INT 16 (+3), WIS 11 (0), CHA 23 (+6)
Proficiency Bonus: 5
Preferred Weapon: Saber
Hit Points: 129
Armor Class: 15
Attack Bonus: 14
Attack Damage: 3d10 + 9 slashing
Special Attack: 1d8 + 90 fire
Save DC: 19
Save Proficiencies: CHA, WIS
Save Modifiers: STR +2, DEX +3, CON +4, INT +3, WIS +5, CHA +11
Skills: Deception CHA 11, Stealth DEX 8, Endurance CON 9, Fortitude CON 9, Religion INT 8, Persuasion CHA 11, Athletics STR 7, Medicine WIS 5, Reflex DEX 8
Talent: Expert dart thrower and rock skipper
Personal Goal: Recover a legendary artifact
Background: Hermit, Communing with Nature
Ideal: Free Thinking. Inquiry and curiosity are the pillars of progress.
Flaw: I let my need to win arguments overshadow friendships and harmony.
Inventory: Armor +1 plate, Demon armor, Ioun stone (insight)

Heavy Wooden Door, closed and locked, carved stone stairway to the next room.

Room 97, Prison Workout Room
Dimensions: hexagon, 72 hands across
Details: This room appears empty except for a thick coat of dust on the floor.
Monster: Stone Giant, CR 14
STR 16 (+3), DEX 11 (0), INT 16 (+3), WIS 11 (0), CHA 9 (-1), CON 8 (-1)
Hit Points: 278
Armor Class: 17
Attack Bonus: 9
Basic Attack: 4d6 + 5 crushing
Save DC: 18
XP Value: 11500
Treasure: 700 Gold Coins, 30 Platinum Coins

Solid Iron Gate, closed but unlocked, wooden stairway to the next room.

Room 98, Desecrated Altar of Light
Dimensions: rectangle, 36 x 9 hands
Details: Mid-century modern with a bi-friendly open relationship floor plan.
Villain: Doppelganger: Dwarf Archer, CR 14
Motivation: Madness
STR 21 (+5), DEX 16 (+3), INT 16 (+3), WIS 13 (+1), CHA 9 (-1), CON 13 (+1)
Proficiency Bonus: 5
Hit Points: 269
Armor Class: 17
Attack Bonus: 9
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 4d8 + 5 piercing
Special Attack Damage: 1d8 + 90 lightning
Special Ability: Oracle of War. The villain fights with an unnatural defensive advantage. Usable 3 times per day.
Weakness: The villain is weakened if its true name is spoken aloud within the villain's range of hearing.
Save DC: 18
XP Value: 11500
Treasure: 19600 Gold Coins, 2260 Platinum Coins, Gems 5000 GP

Etched Silver Door, open and unlocked, wooden stairway to the next room.

Room 99, Artificer's Workshop
Dimensions: rectangle, 60 x 57 hands
Details: Part of the ceiling is collapsing under its own weight.
Monster Group: Nightmare, CR 14
Number Appearing: 2
STR 15 (+2), DEX 9 (-1), INT 13 (+1), WIS 14 (+2), CHA 15 (+2), CON 12 (+1)
Hit Points: 134 each
Armor Class: 18
Attack Bonus: 8
Attack Damage: 2x (3d6 + 5 necrotic)
Save DC: 18
XP Value: 11500
Treasure: 1500 Silver Coins, 1400 Gold Coins, 10 Platinum Coins

Studded Wooden Door, closed but unlocked, south hallway to the next room.

Room 100, Dungeon Heart
Dimensions: circular, 70 hands across
Details: An illusion appears in this room, possibly revealing a clue about the Boss: 25% chance.
Boss: Behemoth, CR 16
STR 12 (+1), DEX 20 (+5), INT 24 (+7), WIS 13 (+1), CHA 17 (+3), CON 22 (+6)
Hit Points: 296
Armor Class: 18
Attack Bonus: 9
Number of Attacks: 4 basic attacks or 1 special per turn.
Basic Attack: 5d10 + 5 crushing
Special Attack: 1d10 + 100 shadow
Special Ability: Breath Weapon. Cone of fire.
Legendary Actions. The boss may use one basic attack or move action at the end of every opponent's turn.
Save DC: 18
XP Value: 15000
Treasure: 800 Silver Coins, 16200 Gold Coins, 1800 Platinum Coins, Jewels 750 GP, Horseshoes of a zephyr, Potion of greater healing, Potion of healing, Potion of invisibility, Potion of resistance, Potion of vitality, Spell scroll (3rd level) Sleet Storm, Spell scroll (6th level) Contingency

Dungeon Exit: Solid Gold Gateway, magically sealed, magic portal leads out of the dungeon. 

```
