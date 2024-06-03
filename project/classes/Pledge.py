class Pledge:
    def __init__(self, description, value):
        self.description = description
        self.value = value

    def display_pledge(self):
        print(f"Pledge: {self.description}, Value: {self.value}")