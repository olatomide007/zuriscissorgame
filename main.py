
import random

def display_game():
    print("Welcome to scissor-rock-game")
    option = ["R for rock", "P for paper", "S for scissor"]
    return option

# Rule = R > S, S > P, P > R


def game():
    choice_ans = ["R","P","S"]
    user = input(f"Pick your choice from {choice_ans}").upper()
    while not (user == "R" or user == "P" or user == "S"):
        user = input(f"oppphhs! make your choice well from {choice_ans} ").upper()

    computer = random.choice(choice_ans)
    
    print(f"Computer:  {computer}")
    if computer == user:
        print("It's a tie")
    
    elif user == "R":
        if computer == "P":
            print("computer wins")
        if computer == "S":
            print("You win")

    elif user == "P":
        if computer == "S":
            print("computer wins")
        if computer == "R":
            print("You win")

    elif user == "S":
        if computer == "R":
            return("computer wins")
        if computer == "P":
            return("You win")
    return user
    

def gameon_choice():
    user ="wrong"

    while user not in ["Y","N"]:
        user = input("would you like to keep playing? ").upper()


    if user == "Y":
        return True
    else:
        print("Thanks for playing. Bye")
        return False

###### putting the logic together
game_on = True

while game_on:
    print(display_game())

    print(game())

    game_on= print(gameon_choice())
    print(game_on)