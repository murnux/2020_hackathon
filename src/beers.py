class Beers:
    all_beers = {
        "Deschutes Fresh Squeeze": ("Fruity", "Hoppy")
        "Kombucha": ("Non-Alcoholic", "Flavorful")
    }

    def get_beer(self, name):
        return self.all_beers[name]
    
    def get_all_beers(self):
        return self.all_beers

    # print_beer takes in the name of the beer (key in the dict) and prints it
    def print_beer(self, beer_key):
        print("{0}: {1}".format(beer_key, self.all_beers[beer_key]))

    # prints all of the beers 
    def print_all_beers(self):
        for beer in self.all_beers:
            self.print_beer(beer)
