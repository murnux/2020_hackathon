class Beers:
    all_beers = {
        # values are as follows: drink name, attributes, acceptable locations, cost to make, purchase price
        "Fresh Squeeze": ("Fruity", "Hoppy", ["Ashland", "Portland"], 2.50, 4.00),
        "Kombucha": ("Non-Alcoholic", "Flavorful", ["Ashland", "Portland"], 3.00, 4.25),
        "White Claw": ("Non-Alcoholic", "Flavorful", ["Medford", "Portland", "Mt Shasta"], 2.00, 3.25),
        "Amber Ale": ("Smooth", "Sweet", ["Ashland", "Portland"], 3.25, 4.10),
        "Drop Top": ("Smooth", "Sweet", ["Medford", "Mt Shasta"], 2.75, 3.50),
        "Alpha Centauri": ("Fruity", "Hoppy", ["Medford", "Mt Shasta"], 3.50, 4.25)
    }

    def get_beer(self, name):
        return self.all_beers[name]
    
    def get_all_beers(self):
        return self.all_beers

    # print_beer takes in the name of the beer (key in the dict) and prints it
    def _print_beer(self, beer_key):
        print("{0}".format(beer_key))
        print("\tAttributes: {0}, {1}".format(self.all_beers[beer_key][0], self.all_beers[beer_key][1]))
        print("\tAcceptable Locations: {0}".format(self.all_beers[beer_key][2]))
        print("\tCost to Produce: ${0:.2f}".format(self.all_beers[beer_key][3]))
        print("\tPurchase Price: ${0:.2f}".format(self.all_beers[beer_key][4]))

    # prints all of the beers 
    def print_all_beers(self):
        # iterate through the dictionary and print all of the beers
        for beer in self.all_beers:
            self._print_beer(beer)

    
    
