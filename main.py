import random

def get_choices():

    player_choices = input("Select your input (Rock, Scissors, Papper) : ")
    options = ["rock", "scissors", "papper"]
    computer_choices = random.choice(options)
    choices = {"player": player_choices.lower(), "computer": computer_choices}
    return choices

def check_win(player, computer):

    print(f'You choice {player} and Computer choice {computer}')

    if player == computer:
        return "It's tie!"
    elif player == "rock" and computer == "papper":
        return "You lose!, Papper cover rock"
    elif player == "rock" and computer == "scissors":
        return "You win!, Rock smash Scissors"
    elif player == "scissors" and computer == "papper":
        return "You win!, Scissors cut Papper"
    elif player == "scissors" and computer == "rock":
        return "You lose!, Rock smash Scissors"
    elif player == "papper" and computer == "rock":
        return "You win!, Papper cover Rock"
    elif player == "papper" and computer == "scissors":
        return "You lose!, Scissors cut Papper"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)