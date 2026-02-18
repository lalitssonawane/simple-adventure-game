def get_user_choice(options):
    while True:
        choice = input(f"Please choose one of the following options: {', '.join(options)} ").strip()  # Strip whitespace
        if choice in options:
            return choice  # Valid choice
        elif choice == '':
            print("Error: You must not enter an empty string. Please try again.")
        else:
            print(f"Error: '{choice}' is not a valid option. Please try again.")

# Example usage:
if __name__ == '__main__':
    choices = ['explore', 'rest', 'fight']
    user_choice = get_user_choice(choices)
    print(f"You chose to: {user_choice}")