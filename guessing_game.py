# This program is a implementation of the number guessing game.

# Features of this game are as follows:
# This game chooses a random number between 1 and 100 inclusive.
# You have to guess the number.
# This game gives you the option to quit in between by entering -1.
# Also you can continue to play until you choose not to.


import random

# This is the main part of the program
def main():
    print_introduction()

    should_continue = 'y'

    while should_continue == 'y':
        print('\nGame Start')
        game_body()
        should_continue = input("\nDo you want to play again(y for yes, anything else for no): ")

# Function is the implementation of the game.
def game_body():

    choosen_number = random.randint(1, 100)

    total_guesses = 1

    guess_number = get_guess()

    while guess_number != choosen_number:
        if guess_number == -1:
            break
        elif guess_number > choosen_number:
            print("Guessed number is too high.")
        elif guess_number < choosen_number:
            print("Guessed number is too low.")
        

        guess_number = get_guess()
        total_guesses += 1

    if guess_number == -1:
        print("The number to guess was " + str(choosen_number) + '.')
        # Have to use total_guesses - 1, since we over count when we enter -1.
        print("You tried with", total_guesses - 1, "guesses.")
    elif guess_number == choosen_number:
        print("You guessed the right number!")
        print("You took", total_guesses, "to get it right.")
    
# Function is used for getting the guessed number from the user.
# Exception handling.
def get_guess():
    incorrect_input = True

    while incorrect_input:
        try:
            number = int(input("Enter number: "))
            incorrect_input = False
        except ValueError:
            print("Error, Invalid Input!")
            print("Try Again!")

    return number

# This function prints the heading of the game.
def print_introduction():
    print()
    print("#"*10 + "GUESSING GAME" + "#" * 10)
    print()
    print("Rules:")
    print("1. You have to enter a number between 1 and 100.")
    print("2. If you have choosen the right number you win!")
    print("3. If the number is lower the computer will tell you.")
    print("4. If the number is higher the computer will tell you.")
    print()
    print("To quit enter -1")
    print()

# Calling the main function.
main()