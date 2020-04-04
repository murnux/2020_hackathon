# this handles some of the main game logic
import os, sys

class Game:
    def __init__(self):
        self.day = 1
        self.max_fails = 2 # number of times the wrong beer can be sold in a day before game over
        self.num_fails = 0
        self.num_clients = 5 # number of clients a day
        self.current_client = 0

    def draw_hud(self, player):
        print("It is day #{0}\nClient Number: {1}/{2}\nNumber of Fails: {3}/{4}\n".format(self.day, self.current_client, self.num_clients, self.num_fails, self.max_fails))
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
        print("Oh no, the client wasn't happy with the order! They've gone crazy and awakened the below-world!")
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
        sys.exit()

    
