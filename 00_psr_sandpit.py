
# imports
import random


def rps_checker():
    error = "Please choose rock, paper or scissor (r / p / s) "

    valid = False
    while not valid:

        # asks question and puts answer in lowercase
        response = input("Rock / Paper / Scissors: ").lower()
        print()

        if response == "rock" or response == "r":
            return "Rock"
        elif response == "paper" or response == "p":
            return "Paper"
        elif response == "scissors" or response == "s":
            return "Scissors"

        else:
            print(error)
            print()


# intcheck code
def intcheck(question, low, high):
    valid = False
    error = "Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)
            print()


# hl(pretty stuff around some outputs) code
def hl_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()
    return ""


sop = hl_statement("--- Rock / Paper / Scissors - Instructions ---", "-")
print("Welcome!")
print("For each game either choose the number of ")
print("rounds or press <enter> for continuous mode.")
print("For both modes, You can end a game early by ")
print("pressing xxx")
print()
print("When promoted choose Rock / Paper / Scissors")
print("At the end of each game, you will see a game")
print("summary. At that point you can either play")
print("again (Press <enter> when promoted) or quit")
print("by pressing any other key.")
print()
print("----------------------------------------------")

losses = 0
wins = 0
tie = 0

play_again = ""
while play_again == "":

    WORDS = ("Paper", "Scissors", "Rock")
    word = random.choice(WORDS)
    correct = word
    print(word)

    chosen_item = rps_checker()
    print(chosen_item)

    if word == chosen_item:
        tie = hl_statement("=== It's a Tie ===", "=")
        tie += 1

    elif word == "Paper" and chosen_item == "Scissors":
        loss_1 = hl_statement("K/ Scissors cut Paper, You lose K/", "K")
        losses += 1

    elif word == "Scissors" and chosen_item == "Rock":
        loss_2 = hl_statement("#K Rock smashes Scissors, You lose #K", "#")
        losses += 1

    elif word == "Rock" and chosen_item == "Paper":
        loss_3 = hl_statement("/# Paper covers Rock, You Lose /#", "/")
        losses += 1

    elif word == "Scissors" and chosen_item == "Paper":
        won_1 = hl_statement("K/ Scissors cut Paper, You Win K/", "K")
        wins += 1

    elif word == "Rock" and chosen_item == "Scissors":
        won_2 = hl_statement("#K Rock smashes Scissors, You lose #K", "#")
        wins += 1

    elif word == "Paper" and chosen_item == "Rock":
        won_3 = hl_statement("/# Paper covers Rock, You Lose /#", "/")
        wins += 1

    else:
        print("nope")

    print(losses)
    print(wins)
    print(tie)

    play_again = (input("Push <enter> to play again or any other key to quit"))
