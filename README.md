# Dungeon Generator Beta

## Random Dungeon
```python
from DungeonGenerator import Dungeon

dungeon = Dungeon(cr=1, dungeon_levels=3, rooms_per_level=5)
print(dungeon)
```

```
Dungeon: The Corrupted Castle of the Mad King

Dungeon Entrance
Dimensions: rectangle, 36 x 21 hands
Details: This room appears empty except for blood dripping from the ceiling.
Minion Group: Novice Dark Paladin, CR 1/8
Number Appearing: 3
Abilities:
  STR 12 (+1)
  DEX 14 (+2)
  INT 14 (+2)
  WIS 16 (+3)
  CHA 18 (+4)
  CON 15 (+2)
Hit Points: 10 each
Armor Class: 9
Attack Bonus: 5
Attack Damage: 3x (1d4 + 2 shadow)
Save DC: 13
XP Value: 25

Wooden Door, closed and locked, north tunnel to the next room.

Room 2, Tormented Artist Studio
Dimensions: rectangle, 36 x 57 hands
Details: Garbage litters the floor of this room.
Monster: Xorn, CR 1
Abilities:
  STR 11 (0)
  DEX 12 (+1)
  INT 12 (+1)
  WIS 13 (+1)
  CHA 13 (+1)
  CON 17 (+3)
Hit Points: 79
Armor Class: 13
Attack Bonus: 3
Basic Attack: 1d6 + 2 holy light
Save DC: 13
XP Value: 200
Treasure: 6 Platinum Coins

Hidden Trapdoor in the floor, south tunnel to the next room.

Room 3, Archer's Barracks
Dimensions: octagon, 36 hands across
Details: The walls are covered in mold and mildew, someone has written 'HELP ME' in blood on the far wall.
Minion Group: Gnoll, CR 1/8
Number Appearing: 4
Abilities:
  STR 12 (+1)
  DEX 15 (+2)
  INT 11 (0)
  WIS 14 (+2)
  CHA 14 (+2)
  CON 13 (+1)
Hit Points: 6 each
Armor Class: 12
Attack Bonus: 2
Attack Damage: 4x (1d4 + 2 lightning)
Save DC: 13
XP Value: 25

Stone Archway, west hallway to the next room.

Room 4, Ritual Chamber
Dimensions: octagon, 36 hands across
Details: Murky indigo water, three hands deep, covers the floor in this room and the one beyond.
Animated Item: Wand of fear, CR 1
Hit Points: 82
Armor Class: 13
Attack Bonus: 3
Attack Damage: 1d6 + 2 fire
XP Value: 200
Treasure: Sentient Wand of fear

Etched Silver Door, closed and locked, north rope bridge to the next room.

Room 5, Officer's Training Room
Dimensions: circular, 60 hands across
Details: The walls are covered in mold and mildew, someone has written 'HELP ME' in blood on the far wall.
Villain: Fire Demon, CR 2
Motivation: Hiding from enemies
Background: Charlatan, Con-artist
Ideal: Fairness. I never target people who can't afford to lose a few coins.
Flaw: I can't resist a pretty face.
Abilities:
  STR 16 (+3)
  DEX 17 (+3)
  INT 18 (+4)
  WIS 18 (+4)
  CHA 18 (+4)
  CON 14 (+2)
Proficiency Bonus: 2
Hit Points: 87
Armor Class: 14
Attack Bonus: 2
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 1d8 + 2 fire
Special Attack Damage: 1d6 + 14 shadow
Special Ability: Shadow Step. Once per round as a bonus action, the villain can instantly teleport up to 30 feet. Usable 3 times per day.
Weakness: The villain is weakened in the presence of a particular magic item. Headband of intellect.
Save DC: 13
XP Value: 450
Treasure: 2000 Copper Coins, 613 Silver Coins, 80 Gold Coins, Gems 200 GP

Wooden Door, closed but unlocked, carved stone stairway to the next room.

Room 6, Mythical Beast Stable
Dimensions: rectangle, 60 x 69 hands
Details: This room is spotless, a clue about an up-coming villain might be found here: 25% chance.
Minion Group: Crawling Claw, CR 1/8
Number Appearing: 3
Abilities:
  STR 15 (+2)
  DEX 14 (+2)
  INT 17 (+3)
  WIS 17 (+3)
  CHA 16 (+3)
  CON 17 (+3)
Hit Points: 4 each
Armor Class: 11
Attack Bonus: 3
Attack Damage: 3x (1d4 + 2 slashing)
Save DC: 13
XP Value: 25

Wooden Door, closed but unlocked, north eastern hallway to the next room.

Room 7, Arboretum
Dimensions: hexagon, 24 hands across
Details: This room appears empty except for scattered bits of broken furniture.
Minion Group: Vampire Spawn, Gnome, CR 1/4
Number Appearing: 4
Abilities:
  STR 18 (+4)
  DEX 17 (+3)
  INT 11 (0)
  WIS 17 (+3)
  CHA 17 (+3)
  CON 16 (+3)
Hit Points: 12 each
Armor Class: 14
Attack Bonus: 1
Attack Damage: 4x (1d4 + 2 necrotic)
Save DC: 13
XP Value: 50

Carved Wooden Door, closed but unlocked, carved stone stairway to the next room.

Room 8, Crypt
Dimensions: rectangle, 36 x 33 hands
Details: Garbage litters the floor of this room.
Monster: Hobgoblin, CR 2
Abilities:
  STR 11 (0)
  DEX 12 (+1)
  INT 9 (-1)
  WIS 15 (+2)
  CHA 12 (+1)
  CON 18 (+4)
Hit Points: 98
Armor Class: 13
Attack Bonus: 3
Basic Attack: 1d6 + 2 bludgeoning
Save DC: 13
XP Value: 450
Treasure: 13 Gold Coins

Secret Door, south rope bridge to the next room.

Room 9, Prison Cell
Dimensions: rectangle, 36 x 21 hands
Details: The floors are covered in clusters of a cyan fungus.
Monster: Lycanthrope: Werecat, CR 2
Abilities:
  STR 6 (-2)
  DEX 11 (0)
  INT 10 (0)
  WIS 11 (0)
  CHA 11 (0)
  CON 12 (+1)
Hit Points: 90
Armor Class: 14
Attack Bonus: 2
Basic Attack: 1d6 + 2 acid
Save DC: 13
XP Value: 450
Treasure: 23 Copper Coins

Inscribed Wooden Door, closed but unlocked, carved stone stairway to the next room.

Room 10, Shrine of Fortuna
Dimensions: circular, 60 hands across
Details: There are a dozen or more humanoids hanging upside-down from the ceiling, writhing in unison.
Villain: Legendary Lycanthrope: Weretiger Sorcerer, CR 3
Motivation: Trying to contact a deceased lover
Background: Folk Hero, Hero of the People
Ideal: Might. If I become strong, I can take what I want—-what I deserve.
Flaw: Secretly, I believe that things would be better if I were a tyrant lording over the land.
Abilities:
  STR 14 (+2)
  DEX 9 (-1)
  INT 13 (+1)
  WIS 17 (+3)
  CHA 14 (+2)
  CON 18 (+4)
Proficiency Bonus: 2
Hit Points: 113
Armor Class: 15
Attack Bonus: 3
Number of Attacks: 2 basic attacks or 1 special per turn.
Basic Attack Damage: 1d8 + 2 radiant
Special Attack Damage: 1d6 + 20 bludgeoning
Special Ability: Mind Games. A random opponent is forced to solve a mental puzzle and is stunned for 3 rounds. Some say this is like playing a game with God, but she's playing chess and you're playing checkers. And still, you have no idea why you keep loosing. Usable 3 times per day.
Weakness: Susceptible to necrotic damage.
Save DC: 13
XP Value: 700
Treasure: 2100 Copper Coins, 1300 Silver Coins, 97 Gold Coins, Jewels 75 GP

Etched Silver Door, open and unlocked, south eastern hallway to the next room.

Room 11, Chamber of Summoning
Dimensions: square, 48 hands across
Details: This room appears empty except for a thick coat of dust on the floor.
Minion Group: Yeti, CR 1/4
Number Appearing: 2
Abilities:
  STR 18 (+4)
  DEX 18 (+4)
  INT 13 (+1)
  WIS 15 (+2)
  CHA 16 (+3)
  CON 16 (+3)
Hit Points: 20 each
Armor Class: 12
Attack Bonus: 3
Attack Damage: 2x (1d4 + 2 frost)
Save DC: 13
XP Value: 50

Wooden Door, closed but unlocked, north eastern tunnel to the next room.

Room 12, Iron Forge
Dimensions: octagon, 24 hands across
Details: This room reminds me of grandmother's house... before the 'accident'
Monster: Golem, CR 3
Abilities:
  STR 15 (+2)
  DEX 11 (0)
  INT 16 (+3)
  WIS 14 (+2)
  CHA 11 (0)
  CON 9 (-1)
Hit Points: 111
Armor Class: 15
Attack Bonus: 3
Basic Attack: 1d6 + 2 lightning
Save DC: 13
XP Value: 700
Treasure: 13 Copper Coins

Carved Wooden Door, closed but unlocked, south western tunnel to the next room.

Room 13, Lavatory
Dimensions: hexagon, 36 hands across
Details: This room appears empty except for scattered bits of broken furniture.
Minor Trap, CR 3: Exploding Mirror
Spot & Disarm DC 10
Save vs. WIS DC 11 for half damage.
Damage: 2d4 slashing
Disarm XP: 700

Studded Wooden Door, closed and locked, metal stairway to the next room.

Room 14, Carved Marble Great Hall
Dimensions: hexagon, 24 hands across
Details: Part of the ceiling is collapsing under its own weight.
Animated Item: Belt of hill giant strength, CR 1
Hit Points: 78
Armor Class: 12
Attack Bonus: 4
Attack Damage: 1d6 + 2 hacking
XP Value: 200
Treasure: Sentient Belt of hill giant strength

Hidden Trapdoor in the ceiling, north western rope bridge to the next room.

Room 15, Dungeon Heart
Dimensions: circular, 100 hands across
Details: This room was decorated years ago for a party or wedding that never happened.
Boss: Arch Devil of Blades, CR 5
Abilities:
  STR 13 (+1)
  DEX 15 (+2)
  INT 28 (+9)
  WIS 18 (+4)
  CHA 19 (+4)
  CON 20 (+5)
Hit Points: 143
Armor Class: 14
Attack Bonus: 6
Number of Attacks: 4 basic attacks or 1 special per turn.
Basic Attack: 1d10 + 3 slashing
Special Attack: 1d6 + 32 void
Special Ability: Legendary Resistance. If the villain fails a saving throw, they can choose to succeed instead.
Legendary Action. The boss may use one basic attack or move action at the end of every opponent's turn.
Save DC: 15
XP Value: 1800
Treasure: 2500 Copper Coins, 5000 Silver Coins, 20 Electrum Coins, 2200 Gold Coins, 60 Platinum Coins, Jewels 175 GP, Potion of greater healing, Potion of healing, Spell scroll (1st level) Shield, Spell scroll (cantrip) Light

Dungeon Exit: Solid Gold Gateway, magically sealed, magic portal leads out of the dungeon. 

```
