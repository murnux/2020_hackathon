import player
import game

prompt = "Hello! Please enter your name: "
name = raw_input(prompt)
print("Hello {0}! You just moved into the city of Mount Shasta, with a dream of selling the best craft beer in town.".format(name))
print("However, you have a difficult and wide ranging clientele from all over southern Oregon and northern California. They all have different tastes and preferences.")
print("If you don't sell them the beer they want, they'll get angry and awaken the Below-World!")

player = player.Player(name)
game = game.Game()
while True: # main game loop
    print("In the loop")
    print(player.name)
    game.clear_screen()
    break
