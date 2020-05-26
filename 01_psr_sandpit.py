
# imports
import random

# rock, paper, scissors check


def rps_checker():
    error = "Please choose rock, paper or scissors (r / p / s) "

    valid = False
    while not valid:

        # asks question and puts answer in lowercase (with capital starting letter)
        response = input("Rock (r)/ Paper (p)/ Scissors (s): ").lower()
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


# rps (pretty stuff around some outputs) code
def rps_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()
    return ""

# instructions and welcome
rps_instructions = rps_statement("--- Rock / Paper / Scissors - Instructions ---", "-")
print("Welcome!")
print("For each game you can choose how many rounds")
print("you would like to play.")
print("When promoted choose Rock / Paper / Scissors")
print("At the end of each game, you will see a game")
print("summary. At that point you can either play")
print("again (Press <enter> when promoted) or quit")
print("by pressing any other key(and then enter).")
print()
print("----------------------------------------------")

losses = 0
wins = 0
ties = 0

# play_again loop start
play_again = ""
while play_again == "":

    print()
    # asking how many rounds
    rounds = intcheck("How many rounds?", 1, 10)
    print()

    rounds_played = 0

    while rounds_played < rounds:
        # output amount of rounds and guesses allowed
        print("Round {} of {}".format(rounds_played + 1, rounds))
        print()

        WORDS = ("Paper", "Scissors", "Rock")
        word = random.choice(WORDS)
        correct = word
        print(word)  # (NEED TO # IFY (LATER))

        rounds_played += 1

        chosen_item = rps_checker()
        print(chosen_item)
        print(word)

        # Word vs Chosen_item results

        if word == chosen_item:
            tie = rps_statement("=== It's a Tie ===", "=")
            ties += 1

        elif word == "Scissors" and chosen_item == "Paper":
            loss_1 = rps_statement("Scissors cut Paper, You lose", "&")
            losses += 1

        elif word == "Rock" and chosen_item == "Scissors":
            loss_2 = rps_statement("Rock smashes Scissors, You lose", "&")
            losses += 1

        elif word == "Paper" and chosen_item == "Rock":
            loss_3 = rps_statement("Paper covers Rock, You Lose", "&")
            losses += 1

        elif word == "Paper" and chosen_item == "Scissors":
            won_1 = rps_statement("Scissors cut Paper, You Win", "$")
            wins += 1

        elif word == "Scissors" and chosen_item == "Rock":
            won_2 = rps_statement("Rock smashes Scissors, You Win", "$")
            wins += 1

        elif word == "Rock" and chosen_item == "Paper":
            won_3 = rps_statement("Paper covers Rock, You Win", "$")
            wins += 1

        else:
            print("error")  # (other ERROR into here???)

    # 'conclusion'

    final = rps_statement("*** Won:{}  |  Lost:{}  |  Draw:{} ***".format(wins, losses, ties), "*")

    play_again = (input("Push <enter> to play again/continue or any other key to quit"))

# Goodbye message

print("Thanks For Playing!")
