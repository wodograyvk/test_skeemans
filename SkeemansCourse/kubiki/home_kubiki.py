
import random

def dice():
    player = random.randint(1,6)
    print("You rolled " + str(player) )

    ai = random.randint(1,6)
    print("The ai rolled " + str(ai) )

    if player > ai :
        print("You good, you win")
    elif player == ai :
        print("Tie game")
    else:
        print("You lose")

    print("quit game? Yes/No?")
    cont = input()

    if cont == "Yes" or cont == "yes":
        exit()
    elif cont == "No" or cont == "no":
        pass
    else:
        print("I did not understand that. Playing again")


