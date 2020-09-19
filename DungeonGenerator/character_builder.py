from DungeonGenerator.player_lib import *
from Fortuna import MultiChoice


get_archetype = MultiChoice(
    "\nChoose an archetype:",
    options=("Apprentice", "Caster", "Melee", "Ranged", "Healer"),
    strict=True,
)
get_caster = MultiChoice(
    "\nWhat type of caster?",
    options=("Wizard", "Sorcerer", "Warlock", "Cleric", "Druid", "Bard"),
    strict=True,
)
get_melee = MultiChoice(
    "\nWhat type of melee?",
    options=("Fighter", "Barbarian", "Knight", "Rogue", "Monk", "Paladin", "Bard"),
    strict=True,
)
get_ranged = MultiChoice(
    "\nWhat type of ranged?",
    options=("Ranger", "Rogue", "Fighter", "Bard"),
    strict=True,
)
get_healer = MultiChoice(
    "\nWhat type of healer?",
    options=("Cleric", "Druid", "Paladin", "Bard"),
    strict=True,
)

class_hierarchy = {
    "Apprentice": lambda: "Apprentice",
    "Caster": get_caster,
    "Melee": get_melee,
    "Ranged": get_ranged,
    "Healer": get_healer,
}

get_race = MultiChoice(
    "\nChoose a race:",
    options=(
        "Human", "Mountain Dwarf", "Hill Dwarf", "Shout Halfling",
        "Lightfoot Halfling", "Forest Gnome", "Rock Gnome", "High Elf",
        "Wood Elf", "Half-elf", "Drow", "Half-orc", "Dragonborn", "Tiefling",
    ),
    strict=True,
)


class PickNumber:

    def __init__(self, query=None, target_range=None, default=None):
        target = target_range or range(1, 101)
        que = query or "Pick a number"
        self.query = f"{que}: {target[0]}-{target[-1]}"
        self.target_range = target
        self.default = default
        self.cursor = ">>> "
        self.choice_pack = (
            self.query,
            self.cursor,
        )

    def _get_answer(self):
        return input('\n'.join(self.choice_pack)) or self.default

    def __call__(self):
        answer = self._get_answer()
        if not answer:
            return random_value(self.target_range)
        elif int(answer) in self.target_range:
            return int(answer)
        else:
            return self()


def make_character():
    my_race = get_race()
    get_class = class_hierarchy[get_archetype()]
    my_class = get_class()
    get_level = PickNumber("\nChoose a level", range(1, 21))
    level = get_level() if my_class != 'Apprentice' else 1
    return Player(eval(my_class), race=my_race, level=level)


if __name__ == '__main__':
    print(f"\n{make_character()}")
