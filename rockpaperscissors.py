#rock paper scissors game

import random

user_choice = int(input("Enter your choice: Tyoe 0 for rock, 1 for paer and 2 for scisscors. "))
if user_choice >= 3 or user_choice < 0:
    print("You entered invalid number, you lose")
else:
    computer_choice = random.randint(0, 2)
    print(f"Computer choice: {computer_choice}")

    if computer_choice == user_choice:
        print("it's a draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
