from Fortuna import *


def cr_adapter(num_players, average_level, difficulty=0):
    average_level = smart_clamp(average_level, 1, 20)
    num_players = smart_clamp(num_players, 1, 9) - 5
    magic_bonus = (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4)[average_level]
    diff_modifier = smart_clamp(difficulty, -5, 5)
    return smart_clamp(num_players + average_level + magic_bonus + diff_modifier, -3, 30)


def cr_str(cr):
    if type(cr) == int:
        return ("1/16", "1/8", "1/4", "1/2")[cr + 3] if cr < 1 else str(cr)
    else:
        return cr.string


damage_types = FlexCat({
    "Physical": ('slashing', 'bludgeoning', 'piercing', 'hacking', 'crushing'),
    "Arcane": ('fire', 'lightning', 'frost', 'acid', 'shadow', 'radiant'),
    "Unholy": ('necrotic', 'hell fire', 'corruption', 'void', 'negative energy'),
    "Holy": ('holy fire', 'thunderbolt', 'holy light', 'divine force', 'positive energy'),
    "Nature": (lambda: damage_types("Arcane"), lambda: damage_types("Physical")),
    "Divine": (lambda: damage_types("Holy"), lambda: damage_types("Nature"), lambda: damage_types("Unholy")),
}, key_bias="front_linear", val_bias="truffle_shuffle")


if __name__ == "__main__":
    print()
    for _ in range(20):
        print(damage_types())
