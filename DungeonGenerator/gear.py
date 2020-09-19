from Fortuna import *
from DungeonGenerator.cr import CR
from DungeonGenerator.gear_lib import basic_gear


class BasicGear:
    gear_types = basic_gear.random_cat

    def __init__(self, cr):
        self.cr = smart_clamp(cr, -3, 30)
        self.id, self.item_type, self.price, self.cursed, self.magic = self.make_item(self.cr)
        self.name = f"{self.item_type}, Price: {self.price}"

    def __repr__(self):
        return self.name

    def identify(self):
        self.name = self.id

    def make_item(self, cr):
        item_type = self.gear_types()
        is_cursed = percent_true(cr / 3)
        if cr < 1:
            price = f"{50 + (cr * 10) + d(10)} Copper"
            magic_value = 0
        elif cr <= 4:
            price = f"{cr * 50 + d(100)} Copper"
            magic_value = 0
        elif cr <= 8:
            price = f"{cr * 50 + d(100)} Silver"
            if is_cursed:
                magic_value = -1
            else:
                magic_value = d(2) - 1
        elif cr <= 12:
            price = f"{cr * 50 + d(100)} Electrum"
            if is_cursed:
                magic_value = -d(2)
            else:
                magic_value = d(2)
        elif cr <= 16:
            price = f"{cr * 50 + d(100)} Gold"
            if is_cursed:
                magic_value = -d(2)
            else:
                magic_value = d(2)
        else:
            price = f"{cr * 50 + d(100)} Platinum"
            if is_cursed:
                magic_value = -d(3)
            else:
                magic_value = d(3)
        if magic_value == 0 or "Clothing" in item_type:
            item_good = percent_true(50)
            if item_good:
                item_quality = "exceptional"
            else:
                item_quality = "poor"
            item = f"{basic_gear(item_type)}, {item_quality} quality"
        elif magic_value > 0:
            item = f"{basic_gear(item_type)}, +{magic_value}"
        else:
            item = f"{basic_gear(item_type)}, {magic_value} Cursed"
        return item, item_type, price, is_cursed, magic_value


def random_gear(cr, identify=False):
    item = BasicGear(cr)
    if identify:
        item.identify()
    return item


class Potion:
    random_potion = FlexCat({
        "1": (
            "Potion case: 10 Potions of healing",
            "Potion of animal friendship",
            "Potion of water breathing",
            "Potion of hill giant strength",
            "Potion of cloud giant strength",
            "Potion of climbing",
            "Potion of poison",
            "Potion of speed",
            "Potion of growth",
            "Potion of fire breath",
            "Potion of diminution",
            "Potion of gaseous form",
        ),
        "2": (
            "Potion case: 10 Potions of greater healing",
            "Potion of frost giant strength",
            "Potion of fire giant strength",
            "Potion of clairvoyance",
            "Potion of vitality",
            "Potion of flying",
            "Potion of invisibility",
            "Potion of resistance",
        ),
        "3": (
            "Potion case: 10 Potions of superior healing",
            "Potion of stone giant strength",
            "Potion of mind reading",
            "Potion of heroism",
        ),
        "4": (
            "Potion case: 10 Potions of supreme healing",
            "Potion of storm giant strength",
            "Potion of longevity",
            "Potion of invulnerability",
        ),
    }, key_bias="front_linear", val_bias="truffle_shuffle")

    def __init__(self, cr):
        tier = d(CR(cr).tier)
        self.name = self.random_potion(str(tier))
        self.price = f"{dice(5, 100)} {('Silver', 'Electrum', 'Gold', 'Platinum')[tier - 1]}"

    def __repr__(self):
        return f"{self.name}, Price: {self.price}"


if __name__ == '__main__':
    print()
    for _ in range(10):
        p = Potion(1)
        print(f"{p}")
