class ShoppingCart:
    def __init__(self):
        self.items = []

    def _calculate_discount(self, total):
        if total > 100:
            return total * 0.10
        return 0

    def add_item(self, price):
        self.items.append(price)

    def total_price(self):
        total = sum(self.items)
        discount = self._calculate_discount(total)
        return total - discount

    def checkout(self):
        total = self.total_price()
        print(f'Galutinė kaina pritaikius nuolaidą: {total:.2f} Eur')