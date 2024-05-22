class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f'Elementas "{item.name}" pridėtas prie užsakymo.')

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f'Elementas "{item_name}" pašalintas iš užsakymo.')
                return
        print(f'Elementas "{item_name}" nerastas užsakyyme.')

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items)
        return total_price
