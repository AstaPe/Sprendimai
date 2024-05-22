class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f'The engine of the {self.brand} is now running.')

    def print_info(self):
        print(f'Car 1: {self.brand}, {self.color}')
