import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    if level_chosen == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return
    
def check_answer(guessed_number, comps, attempts):
    if guessed_number < comps:
        print("Your guess is too low")
        return attempts - 1
    elif guessed_number > comps:
        print("Your guess is too high")
        return attempts - 1

    else:
        print(f"Your guess is right... The answer was {comps}")


def game():
    print("Guess a number game")
    print("Let me think of a number between 1 and 50")
    comps = random.randint(1, 50)
    print(comps)
    level = input("Choose level of difficulty... Type 'easy' or 'hard': ").lower()
    attempts = set_difficulty(level)
    if attempts != EASY_LEVEL_ATTEMPTS and attempts != HARD_LEVEL_ATTEMPTS:
        print("You have entered a wrong choice! Play Again!!!")
        return
    guessed_number = 0
    while guessed_number != comps:
        print(f"You have {attempts} remaining to guess the number")
        guessed_number = int(input("Guess a number: "))
        attempts = check_answer(guessed_number, comps, attempts)
        if attempts == 0:
            print("You are out of guesses... You lose!")
            return
        elif guessed_number != comps:
            print("Guess again")
            
game()