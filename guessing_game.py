"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

def welcome():
    print("Welcome to this cool game! Guess a number between 1 and 10: ")

def validate(userInput, randomNumber):
    try:
        if userInput == -1:
            return int(input())
        if userInput < randomNumber:
            return int(input("It's higher: "))
        elif userInput > randomNumber:
            return int(input("It's lower: "))
    except ValueError:
        print("That's a weird looking number. Try again.")


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    welcome()

    randomNumber = int(random.randint(1, 10))
    userInput = -1
    attempts = 1

    try:
        userInput = int(input())
    except ValueError:
        print("That's a weird looking number. Try again.")


    while userInput != randomNumber:
        attempts += 1
        userInput = validate(userInput, randomNumber)

    if attempts < 2:
        print("You got it in 1 try!")
    else:
        print("You got it in {} tries!".format(attempts))

    print("This epic game has reached completion!")

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()