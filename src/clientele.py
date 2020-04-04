import random

class Clientele:
    options = ["Ashland", "Medford", "Shasta", "Portland"]
    possible_tastes = [('Fruity', 'Hoppy'), ('Non-Alcoholic' , 'Flavorful')]

    def __init__(self):
        rand_num = random.randint(0, len(self.options) - 1)
        self.location = self.options[rand_num]
        rand_taste = random.randint(0, len(self.possible_tastes) - 1)
        self.taste = self.possible_tastes[rand_taste]

    def order(self):
        print("Greetings! My name is Jeff, and I am from {0}. I am looking for something {1} and {2}. What do you have for me?".format(self.location, self.taste[0], self.taste[1]))

    # this is called after the player has chosen a drink, this checks if it is compatible. 
    def check_beer_given(self, beer, all_beers):
        if self.taste[0] == all_beers[beer][0] and self.taste[1] == all_beers[beer][1]:
            return True # indicates given beer is compatible
        else:
            return False