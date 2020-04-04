# local python file imports
import player
import game
import clientele
import beers

# third-party module imports
import sys

prompt = "Hello! Please enter your name: "
name = raw_input(prompt)
print("Hello {0}! You just moved into the city of Mount Shasta, with a dream of selling the best craft beer in town.".format(name))
print("However, you have a difficult and wide ranging clientele from all over Oregon and northern California. They all have different tastes and preferences.")
print("If you don't sell them the beer they want, they'll get angry and awaken the Below-World!\n")

confirm = raw_input("Are you ready to play the game? Type 'y' when ready: ")
if confirm != 'y':
    print("Exiting game because 'y' was not input.")
    sys.exit(1) # exiting because the user did not type 'y'

# create the objects we need
player = player.Player(name)
game = game.Game()
the_beers = beers.Beers()
game.clear_screen()
while True: # main game loop
    game.draw_hud(player)
    print("A new client enters the store...")
    client = clientele.Clientele()
    client.order()
    game.action_menu()
    choice = game.get_action() # get action input from the player

    done = False
    while not done:
        # Python doesn't have switch statements, sad days...
        if choice == "help":
            game.help()
        elif choice == "1":
            the_beers.print_all_beers()
        elif choice == "2":
            done = True
        elif choice == "3":
            print("Exiting game.")
            sys.exit() # exit with 0 return code
        print("") # print a new line
        if not done:
            choice = game.get_action()

    game.day += 1
    #game.over()
