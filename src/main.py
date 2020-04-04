# local python file imports
import player
import game
import clientele
import beers

# third-party module imports
import sys, time

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
    game.clear_screen() # clears the screen for this day

    while game.current_client <= game.num_clients: # loop to keep introducing clients until the day is over
        game.clear_screen()
        print("A new client enters the store...")
        time.sleep(2)
        game.draw_hud(player)
        client = clientele.Clientele()
        client.order()
        print("")
        game.action_menu()
        choice = game.get_action() # get action input from the player

        done = False
        while not done:
            # Python doesn't have switch statements, sad days...
            if choice == "help":
                game.help()
            elif choice == "1": # lists all beers
                the_beers.print_all_beers()
            elif choice == "2": # handle logic of giving a beer to the client
                beer = raw_input("Type in the name of the beer to give: ")
                while beer not in the_beers.all_beers:
                    print("\nThat beer does not exist, please try again.")
                    beer = raw_input("Type in the name of the beer to give: ")

                cost_to_make = the_beers.all_beers[beer][3] # how much it takes to produce this beer
                purchase_price = the_beers.all_beers[beer][4] # number the client pays on a successful purchase
                player.money -= cost_to_make # subtract the amount it took to produce this beer
                successful = client.check_beer_given(beer, the_beers.all_beers) # check if the given beer works.
                time.sleep(4)
                if not successful:
                    game.num_fails += 1
                    if game.num_fails >= game.max_fails: # if this is true, the number of fails has been exceeded and the game must end
                        game.over()
                else:
                    player.money += purchase_price
                done = True
            elif choice == "3": # exits the game
                print("Exiting game.")
                sys.exit() # exit with 0 return code
            print("") # print a new line
            if not done:
                choice = game.get_action()
            
            game.current_client += 1
            client = None

    print("Moving onto the next day...")
    time.sleep(3) # wait before moving onto the next day
    # reset some of the game object values
    game.current_client = 0
    game.num_fails = 0
    game.day += 1 # increment day number
