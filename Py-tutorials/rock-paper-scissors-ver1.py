import random

options = ("rock", "paper", "scissors")
count = []
while True:
    option = random.choice(options)
    user_input = str(input("Rock, Paper, Scissors: ")).lower()
    print("-------------------------------")
    print()
    print(f"The bot chose: {option}")
    if user_input not in options:
        break
    elif option == 'rock':
        if user_input == 'rock':
            print("Draw!")
        elif user_input == 'paper':
            print("You won!")
        elif user_input == 'scissors':
            print("You lose!")
    elif option == 'paper':
        if user_input == 'rock':
            print("You lose!")
        elif user_input == 'paper':
            print("Draw!")
        elif user_input == 'scissors':
            print("You won!")
    elif option == 'scissors':
        if user_input == 'rock':
            print("You won!")
        elif user_input == 'paper':
            print("You lose!")
        elif user_input == 'scissors':
            print("Draw!")
    print()
    print("-------------------------------")