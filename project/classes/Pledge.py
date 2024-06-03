class Pledge:
    def __init__(self, description, value):
        self.description = description
        self.value = value

    def display_pledge(self):
        return f"Pledge Description: {self.description}, Value: {self.value}"
