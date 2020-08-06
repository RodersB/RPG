def get_base_stats():
    return {
        "base_stats": {
            "hp": 100,
            "mp": 100,
            "hp_regen": 5,
            "mp_regen": 2,
            "hp_leech": 0,
            "mp_leech": 0,
            "base_attack_speed": 100,
            "critical_chance": 0,
            "dodge_chance": 0,
            "block_chance": 0,
            "block_dmg_reduction": 0,
            "armor": 10,
            "magic_resist": 10
        },
        "modded_stats": {
            "hp": 100,
            "mp": 100,
            "hp_regen": 5,
            "mp_regen": 2,
            "hp_leech": 0,
            "mp_leech": 0,
            "base_attack_speed": 100,
            "critical_chance": 0,
            "dodge_chance": 0,
            "block_chance": 0,
            "block_dmg_reduction": 0,
            "armor": 10,
            "magic_resist": 10
        }
    }


def get_base_gear():
    return {
        "helm": None,
        "body_armor": None,
        "main_hand": None,
        "off_hand": None,
        "gloves": None,
        "boots": None,
        "ring1": None,
        "ring2": None,
        "amulet": None
    }


class Character:
    def __init__(self, name, stats=get_base_stats(), play_time=0, gear=get_base_gear(), inventory=[]):
        self.name = name
        self.stats = stats
        self.play_time = play_time
        self.gear = gear
        self.inventory = inventory

    @classmethod
    def init_from_json(cls, c):
        return cls(name=c["name"], stats=c["stats"], play_time=c["play_time"], gear=c["gear"], inventory=c["inventory"])

    def equip_item(self, equipment):
        if self.gear.get(equipment.slot, None) is not None:
            self.inventory.append(self.gear.pop(equipment.slot))

        self.gear[equipment.slot] = equipment
        self.calculate_stats()

    def calculate_stats(self):
        pass
