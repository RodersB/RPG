from character import Character
from encounter import Encounter
from equipment import Equipment
from gem import Gem


def get_items():
    helm = Equipment(1, 'Leather Cap', 'head', 1, {'armor': 5})
    sword = Equipment(1, 'Rusted Sword', 'main_hand', 1, {'attack_speed': 1, 'damage_range': [5, 10]})
    ring = Equipment(1, 'Iron Ring', 'finger', 1, {"hp": 10})
    amulet = Equipment(1, 'Bronze Amulet', 'neck', 1, {'increased_attack_speed': 5})
    return [helm, sword, ring, amulet]


def get_gems():
    life_gem = Gem(1, 'Gem of Life', {'flat_hp': 10})
    mana_gem = Gem(1, 'Gem of Mana', {'flat_mana': 10})
    as_gem = Gem(1, 'Gem of Speed', {'increased_attack_speed': 5})


def get_character():
    base_stats = {
        'hp': 100,
        'mana': 100,
        'level': 1,
        'current_xp': 0,
    }

    items = get_items()

    player = Character('TestChar', base_stats)
    player.equip_item(items[0])
    player.equip_item(items[1])
    player.equip_item(items[2])
    player.equip_item(items[3])



def run_encounter(player, encounter_config):
    pass


