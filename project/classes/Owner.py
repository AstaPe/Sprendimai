class Owner:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def display_info(self):
        return f"Owner: {self.name}, Address: {self.address}, Phone: {self.phone}"
