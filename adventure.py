# Complete Adventure Game

def start_game():
    print("Welcome to the Adventure Game!")
    print("You are in a dark room. You can go left or right.")
    choose_direction()


def choose_direction():
    while True:
        direction = input("Which direction will you go? (left/right): ").lower()
        if direction == 'left':
            enter_forest()
            break
        elif direction == 'right':
            enter_castle()
            break
        else:
            print("Invalid input. Please choose 'left' or 'right'.")


def enter_forest():
    print("You have entered a dark forest.")
    print("There is a bear here. Would you like to (fight/run)?")
    while True:
        action = input().lower()
        if action == 'fight':
            print("You fight the bear and win!")
            end_game()
            break
        elif action == 'run':
            print("You run back to the starting point.")
            choose_direction()
            break
        else:
            print("Invalid action. Please choose 'fight' or 'run'.")


def enter_castle():
    print("You are in a spooky castle.")
    print("There is a ghost here. Would you like to (talk/run)?")
    while True:
        action = input().lower()
        if action == 'talk':
            print("The ghost tells you a secret and vanishes!")
            end_game()
            break
        elif action == 'run':
            print("You run back to the starting point.")
            choose_direction()
            break
        else:
            print("Invalid action. Please choose 'talk' or 'run'.")


def end_game():
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == 'yes':
        start_game()
    elif replay == 'no':
        print("Thanks for playing!")
    else:
        print("Invalid input. Please choose 'yes' or 'no'.")
        end_game()


# Start the adventure game
start_game()