class ShoppingCart:
    def __init__(self):
        self._items = {}

    def _calculate_total(self):
        return sum(self._items.values())

    def add_item(self, item, quantity):
        if item in self._items:
            self._items[item] += quantity
        else:
            self._items[item] = quantity
        print(f"{quantity} {item}(s) added to the shopping cart.")

    def remove_item(self, item, quantity):
        if item in self._items:
            if self._items[item] > quantity:
                self._items[item] -= quantity
                print(f"{quantity} {item}(s) removed from the shopping cart.")
            elif self._items[item] == quantity:
                del self._items[item]
                print(f"All {item}(s) removed from the shopping cart.")
            else:
                print(f"Not enough {item}(s) in the shopping cart.")
        else:
            print(f"{item} is not in the shopping cart.")

    def get_total_items(self):
        return self._calculate_total()