"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Bryce Bellerand
Date: 10/26/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import random
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    if character_class in ["Warrior", "Mage", "Rogue", "Cleric"]:
        strength, magic, health = calculate_stats(character_class, 1)
        character_stats = {
            "name": name,
            "class": character_class,
            "level": 1,
            "strength": strength,
            "magic": magic,
            "health": health,
            "gold": 100
        }
        return character_stats
    else:
        return None

    

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    warrior_stats = (15 + level * 2.5, 2 + level * 0.2, 12 + level * 8)
    mage_stats = (5 + level * 0.7, 18 + level * 3, 8 + level * 4)
    rogue_stats = (10 + level * 1.5, 8 + level * 1.5, 5 + level * 2.5)
    cleric_stats = (7 + level * 1.2, 15 + level * 2.5, 10 + level * 7)

    if character_class == "Warrior":
        return warrior_stats
    elif character_class == "Mage":
        return mage_stats
    elif character_class == "Rogue":
        return rogue_stats
    elif character_class == "Cleric":
        return cleric_stats
    else:
        return (0, 0, 0)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    with open(filename, 'w') as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    with open(filename, 'r') as file:
        lines = file.readlines()
        character_bio = {}
        for line in lines:
            key, value = line.strip().split(": ")
            if key == "Character Name":
                character_bio["name"] = value
            elif key == "Class":
                character_bio["class"] = value
            elif key == "Level":
                character_bio["level"] = int(value)
            elif key == "Strength":
                character_bio["strength"] = float(value)
            elif key == "Magic":
                character_bio["magic"] = float(value)
            elif key == "Health":
                character_bio["health"] = float(value)
            elif key == "Gold":
                character_bio["gold"] = int(value)
        return character_bio
    

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=========================\n")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character['level'] += 1
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health    
    return character

    # TODO: Implement this function
    # Remember to recalculate stats for the new level

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    char = create_character("TestHero", "Warrior")
    display_character(char)

    if save_character(char, "my_character.txt"):
        print("Character saved successfully!\n")

    loaded = load_character("my_character.txt")
    if loaded:
        print("Character loaded successfully!\n")
        display_character(loaded)

    # Level up demonstration
    level_up(loaded)
    print("After leveling up:")
    display_character(loaded)
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
