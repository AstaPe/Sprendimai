class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        return f'This is {self.name}, and it is a {self.species}.'