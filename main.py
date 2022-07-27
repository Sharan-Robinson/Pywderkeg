import time
from game import *

global savelist
savelist = []

def startgame():

    print("Please select a nation to play as!")
    gamenation = input(
        "1. Austria-Hungary"
        "2.Serbia"
        "3. Greece"
        "4. Turkey"
        "5. Bulgaria"
    )

    savegamename = input("What would you like to call this game?")

    newgame = game(gamenation)

    newgame.createsavegame(savegamename)

def continuesave():
    if not savelist:
        print("You don't have any savegames!")
        return
    else:
        print("I found one!")


def main():
    print("Welcome to Pywderkeg. \nIn this game you will one of the balkan nations and make sure "
          "no great war erupts!")
    print("Please select an option:")
    option = input(
        "1. Start New Game\n"
        "2. Continue Game\n"
        "3. Exit Game\n"
        
        "Enter a the number corresponding here:"
    )
    if option == '1':
        startgame()
    elif option == '2':
        continuesave()
    elif option == '3':
        exit()
    else:
        print("That's not a valid option, Please try again. ")


main()

