import random

class Clientele:
    options = ["Ashland", "Medford", "Shasta", "Portland"]
    possible_tastes = [('Fruity', 'Hoppy', 'Non-Alcoholic, Flavorful')]

    def __init__(self):
        rand_num = random.randint(0, len(self.options) - 1)
        self.location = self.options[rand_num]
        self.taste = ""

    def order(self):
        print("Greetings! My name is Jeff, and I am from {0}. I am looking for something Hoppy and Fruity. What do you have for me?".format(self.location))