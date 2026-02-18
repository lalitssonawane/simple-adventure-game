#!/usr/bin/env python3
"""
Simple Choose Your Own Adventure Game
A text-based adventure game with multiple decision points and endings.
"""

def print_welcome():
    """Display the game welcome message."""
    print("\n" + "="*60)
    print("WELCOME TO THE MYSTERIOUS FOREST ADVENTURE")
    print("="*60)
    print("\nYou wake up in a dense forest with no memory of how you got here.")
    print("The sun is beginning to set, and you need to find safety...")
    print()

def first_decision():
    """First decision point: Which path to take."""
    print("You stand at a crossroads with three paths:")
    print("1. Left path - You hear running water (river)")
    print("2. Middle path - You see smoke in the distance (camp)")
    print("3. Right path - You notice a small cabin")
    print()    
    while True:
        choice = input("Which path do you take? (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")

def river_path():
    """Path 1: Following the river."""
    print("\n" + "-"*60)
    print("You follow the sound of running water...")
    print("After a short walk, you find a beautiful river with fresh water.")
    print("You're very thirsty, but the water looks murky and questionable.")
    print()    
    while True:
        choice = input("Do you drink the water? (yes/no): ").strip().lower()
        if choice in ['yes', 'no']:
            if choice == 'yes':
                print("\n🎭 ENDING 1: MYSTERIOUS ILLNESS")
                print("You drink the water without hesitation.")
                print("Within hours, you fall ill. Days later, a search party finds")
                print("you delirious near the river. You survive but never fully recover.")
                return True
            else:
                print("\nYou resist the temptation and continue following the river...")
                print("Eventually, you find a small village downstream!")
                print("\n✨ ENDING 2: SAFE HAVEN")
                print("The villagers take you in and help you contact your family.")
                print("You later learn that the river water was contaminated.")
                print("You've made it to safety. Adventure complete!")
                return True
        print("Please answer 'yes' or 'no'.")

def camp_path():
    """Path 2: Following the smoke to a camp."""
    print("\n" + "-"*60)
    print("You cautiously approach the smoke...")
    print("As you get closer, you see a campfire and two figures sitting nearby.")
    print("One looks friendly, the other seems menacing.")
    print()    
    while True:
        choice = input("Do you approach them or hide and observe? (approach/hide): ").strip().lower()
        if choice in ['approach', 'hide']:
            if choice == 'approach':
                print("\nYou step into the clearing with your hands raised.")
                print("The friendly-looking person smiles and offers you food and shelter.")
                print("\n✨ ENDING 3: UNEXPECTED ALLIES")
                print("They turn out to be researchers studying the forest.")
                print("They help you return to civilization the next morning.")
                print("You've found friendly help. Adventure complete!")
                return True
            else:
                print("\nYou hide behind the trees and watch carefully...")
                print("You notice they're roasting wild game and look hospitable.")
                print("But as night falls, you get too cold hiding in the dark.")
                print("\n❄️ ENDING 4: LOST IN THE COLD")
                print("By morning, hypothermia has set in.")
                print("A ranger finds you barely conscious and takes you to medical care.")
                print("You survive but learn that caution can be dangerous too.")
                return True
        print("Please answer 'approach' or 'hide'.")

def cabin_path():
    """Path 3: Discovering the cabin."""
    print("\n" + "-"*60)
    print("You make your way toward the cabin...")
    print("The door is slightly ajar, and you can see a warm light inside.")
    print("There's also a woodshed to the side with plenty of firewood.")
    print()    
    while True:
        choice = input("Do you enter the cabin or stay outside? (enter/outside): ").strip().lower()
        if choice in ['enter', 'outside']:
            if choice == 'enter':
                print("\nYou push open the cabin door...")
                print("Inside, you find blankets, canned food, and a stocked fireplace.")
                print("It appears to be an abandoned ranger's cabin.")
                print("\n🏠 ENDING 5: COZY SHELTER")
                print("You spend a comfortable night in the cabin.")
                print("The next morning, you find a map and supplies.")
                print("You easily make your way back to civilization!")
                return True
            else:
                print("\nYou build a fire outside near the cabin...")
                print("The warmth of the fire keeps you safe through the night.")
                print("In the morning, you spot a search helicopter!")
                print("\n🚁 ENDING 6: RESCUED BY AIR")
                print("The helicopter spots your fire and rescues you.")
                print("You're taken to safety. Adventure complete!")
                return True
        print("Please answer 'enter' or 'outside'.")

def play_game():
    """Main game loop."""
    print_welcome()
    
    choice = first_decision()
    
    if choice == '1':
        river_path()
    elif choice == '2':
        camp_path()
    else:
        cabin_path()
    
    print("\n" + "="*60)
    print("Thanks for playing! Play again? (yes/no): ", end="")
    play_again = input().strip().lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Goodbye, adventurer!")
        print("="*60 + "\n")

if __name__ == "__main__":
    play_game()