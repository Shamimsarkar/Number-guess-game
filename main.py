from random import randint
from art import logo

EASY_LEVEL_GAME = 10
HARD_LEVEL_GAME = 5


def check_answer(user_guess, actual_numer, turns):
    if user_guess < actual_numer:
        print("Too low.")
        return turns - 1
    elif user_guess > actual_numer:
        print("Too high.")
        return turns - 1
    else:
        print(f"You hit the right numer. The number was {actual_numer}")




def set_difficulty():

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL_GAME
    else:
        return HARD_LEVEL_GAME


def game():

    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")

    right_number = randint(1, 100)

    print(f"The number to be guess is {right_number}")

    turns = set_difficulty()

    guess = 0

    while guess != right_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))


        turns = check_answer(guess,right_number,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != right_number:
            print("Guess again.")

game()