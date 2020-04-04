# this handles some of the main game logic
import os

class Game:
    def __init__(self):
        self.day = 0
        self.max_fails = 3 # number of times the wrong beer can be sold in a day before game over

    def draw_hud(self, player):
        print("It is day #{0}\n".format(self.day))
        print("Name: {0}, Money: ${1:.2f}".format(player.name, player.money))

    # clears the screen to avoid displaying old game state
    def clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    # a list of actions the player can take
    def action_menu(self):
        print("1. List Beers\n2. Give Beer\n3. Exit Game")

    def get_action(self):
        return raw_input("What would you like to do? (type 'help' for some more details): ")

    def help(self):
        print("To list all beers, simply input the number 1.")
        print('To give a beer to the client, input the number 2 and then the name of the beer in the following prompt.')

    def over(self):
        self.clear_screen()
        print('''
             ooO
                     ooOOOo
                   oOOOOOOoooo
                 ooOOOooo  oooo
                /vvv\
               /V V V\ 
              /V  V  V\          
             /     V   \          AAAAH!  RUN FOR YOUR LIVES!
            /      VV   \               /
 ____      /        VVV    \   	  o          o
 /\      /        VVVV     \     /-   o     /-
/  \   /           VVVVVVV   \  /\  -/-    /\
                    VVVVVVVVVVVVV   /\
        ''')

    
