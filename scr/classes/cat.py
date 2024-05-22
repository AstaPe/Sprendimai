class Cat:
    total_cats = 0

    def __init__(self, name):
        self.name = name
        Cat.total_cats += 1