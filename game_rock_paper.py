"""
Name: Prachi Santosh Kolte

File Description: This file contains claasic game of 'Rock paper scissors spock lizard'. It accepts input from users
and simulates random option from computer which gives the effect of game whole.
"""



import random
game_choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
global player_score
global computer_score



def view_scores():
    if (player_score > computer_score):
        print("Player wins by {} numbers".format(player_score - computer_score))
    elif (player_score < computer_score):
        print("Computer wins by : {} numbers".format(computer_score - player_score))
    else:
        print("It's a tie!")

    print("PLayer score is :{}".format(player_score))
    print("Computer score is :{}".format(computer_score))


def main():
    while (True):
        print("Rock Paper Scissors Lizard Spock")

        menu = """
        ---------------------------------
        Main Menu:
        ---------------------------------
        [1] Play
        [2] Scores
        [3] Exit
        """
        print(menu)
        option = (input("Select an option <3 to exit>:"))
        if option == '1':
            play_games()
        elif option == '2':
            view_scores()
        elif option == '3':
            print("Bye")
            exit()
        else:
            print("wrong choice")


def play_games():
    global player_score
    global computer_score
    player_score = 0
    computer_score = 0

    while (True):

        options_display = """
        Rock
        Paper
        Scissors
        Lizard
        Spock
        """
        print(options_display)
        your_choice = input("Enter Your choice <X to exit to the main menu>:")
        computer_choice = (random.choice(game_choices))
        print("Computer's choice:", computer_choice)
        # print(computer_choice)
        if your_choice.lower() in game_choices:

            if your_choice == computer_choice:
                print("Both are equal!")
                player_score += 1
                computer_score += 1

            elif your_choice == 'spock':
                if computer_choice == 'scissors' or computer_choice == 'rock':
                    print("You won !")
                    player_score += 2
                else:
                    print("computer won!")
                    computer_score += 2

            elif your_choice == 'lizard':
                if computer_choice == 'spock' or computer_choice == 'paper':
                    print("You won !")
                    player_score += 2
                else:
                    print("computer won!")
                    computer_score += 2

            elif your_choice == 'scissors':
                if computer_choice == 'lizard' or computer_choice == 'paper':
                    print("You won !")
                    player_score += 2
                else:
                    print("computer won!")
                    computer_score += 2

            elif your_choice == 'rock':
                if computer_choice == 'scissors' or computer_choice == 'lizard':
                    print("You won !")
                    player_score += 2
                else:
                    print("computer won!")
                    computer_score += 2

            elif your_choice == 'paper':
                if computer_choice == 'spock' or computer_choice == 'rock':
                    print("You won !")
                    player_score += 2
                else:
                    print("computer won!")
                    computer_score += 2



        elif your_choice == 'X':

            return 0

        else:
            print("Invalid Choice!")


if __name__ == '__main__':
    main()
