import random

class Clientele:
    options = ["Ashland", "Medford", "Mt Shasta", "Portland"]
    possible_tastes = [('Fruity', 'Hoppy'), ('Non-Alcoholic' , 'Flavorful')]
    names = ["Jeff", "Mary", "Greg", "Matt", "Adam", "Elijah", "John", "Sarah", "Emily"]

    def __init__(self):
        # assign class variables, lots of random stuff going on
        rand_num = random.randint(0, len(self.options) - 1)
        self.location = self.options[rand_num]
        rand_taste = random.randint(0, len(self.possible_tastes) - 1)
        self.taste = self.possible_tastes[rand_taste]
        self.name = self.names[random.randint(0, len(self.names) - 1)]

    def order(self):
        print("Hello! My name is {0}, and I am from {1}. I am looking for something {2} and {3}. What do you have for me?".format(self.name, self.location, self.taste[0], self.taste[1]))

    # this is called after the player has chosen a drink, this checks if it is compatible. 
    def check_beer_given(self, beer, all_beers):
        # I know this isn't fair, but isn't it true? ;)
        if self.location == "Ashland":
            ran = random.randint(0, 100)
            if ran > 50: # random chance that a client from Ashland results in an automatic failure due to self-importance
                print('{0} from {1} says: "Um, excuse me? This is not infused with the crystals of the Lumerians? Ugh, Why did I ever leave Ashland?"'.format(self.name, self.location))
                return False
        elif self.location == "Medford":
            ran = random.randint(0, 100)
            if ran > 50:
                print('{0} from {1} says: "What the heck? You don\'t have any Bud Light? This is garbage!'.format(self.name, self.location))
                return False

        chosen_beer = all_beers[beer]
        if self.taste[0] == chosen_beer[0] and self.taste[1] == chosen_beer[1]:
            if self.location in chosen_beer[2]: # checks if the client's location is in the beer's location array
                print('{0} says: "Mmm, this is really good! {1} might be my new favorite!"'.format(self.name, beer))
                return True # indicates given beer is compatible
            else:
                print('{0} says: "Excuse me, but I am from {1}. This drink does not live up to my standards!"'.format(self.name, self.location))
        else:
            print('{0} says: "I asked for something {1} and {2}. this is not what I wanted!"'.format(self.name, self.taste[0], self.taste[1]))       
        print("\nSadly you made no money.") 
        return False # if any of the above conditionals were not true, then the check was not successful