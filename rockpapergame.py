# Rockpapergame
import random
import os
import re

os.system('cls' if os.name == 'nt' else 'clear')
while 1 < 2 :
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper.")
    # Echo the user's choice
    print("You chose: " + userChoice)
    choices = ['R', 'P', 'S']
    maChoice = random.choice(choices)
    print("I chose: " + maChoice)
    if maChoice == str.upper(userChoice):
        print("Tie! ")
    # if opponenetChoice == str("R") and str.upper(userChoice) == "P":
    elif maChoice == 'R' and userChoice.upper() == 'S':
        print("Scissors beats rock, I win! ")
        continue
    elif maChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper! I win! ")
        continue
    elif maChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beat rock, I win! ")
        continue
    elif userChoice != choices:
        print("Error")
    else:
        print("You win!")


