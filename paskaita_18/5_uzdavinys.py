class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_items(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_items(self, item, quantity):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]

    def view_cart(self):
        print("Shopping Cart Contents:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

    def calculate_total_price(self, prices):
        total_price = 0
        for item, quantity in self.items.items():
            if item in prices:
                total_price += prices[item] * quantity
        return total_price

# Example usage:
cart = ShoppingCart()
cart.add_items("Apple", 2)
cart.add_items("Banana", 3)
cart.add_items("Orange", 1)
cart.view_cart()

prices = {"Apple": 1.0, "Banana": 0.5, "Orange": 0.8}
total_price = cart.calculate_total_price(prices)
print("Total Price:", total_price)