from character import Character
from encounter import Encounter
from equipment import Equipment
from gem import Gem
import json


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

def run_encounter(player, encounter_config):
    pass

def get_user_input(txt):
    user_input = input(txt + "\n Type 'Q' to abort.")

def new_char(existing_characters):
    invalid_name = True
    abort = False
    c = None
    while invalid_name and not abort:
        char_name = input("Stranger: Tell me your name ('Q' to abort)")
        if char_name.upper() == "Q":
            abort = True
            c = None
        else:
            if len(char_name) > 2:
                if char_name not in existing_characters:
                    c = Character(char_name)
                    invalid_name = False
                else:
                    print("Stranger: I already know a '" + char_name + ". \nWhat is your real name?")
            else:
                print("Stranger: That is a very short name. \nWhat is your real name?")
    return c


def player_selection_menu(available_characters):
    selection_id = 1
    valid_selection = False
    c = None
    while not valid_selection:
        for i in available_characters:
            print(str(selection_id) + "  - " + i["name"] + " - Level " + str(i["level"]))
            selection_id += 1
        print(str(selection_id) + "  - New Character")
        print("Q  - Abort")
        user_selection = input("Enter the character number.")
        if user_selection.upper() == "Q":
            c = None
            valid_selection = True
        else:
            try:
                val = int(user_selection)
                if val == selection_id:
                    c = new_char(available_characters)
                    valid_selection = True
                elif 1 <= int(val) <= selection_id - 1:
                    c = Character(available_characters[val - 1])
                    valid_selection = True
                else:
                    print("Invalid Selection. Try Again.")
            except ValueError:
                print("Invalid Selection. Try Again.")
    return c


def character_selection():
    # Read Characters Data file
    file = open('./data/characters.json')
    chars = json.load(file)
    c = None
    if len(chars) == 0:
        c = new_char({})
    else:
        c = player_selection_menu(chars["characters"])
    return c


def main():
    print("RUNA")
    player = character_selection()


if __name__ == '__main__':
    main()
