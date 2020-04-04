# this handles some of the main game logic
import os

class Game:
    def __init__(self):
        self.day = 0

    def draw_hud(self, player):
        print("in hud")

    # clears the screen to avoid displaying old game state
    def clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
