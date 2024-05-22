from namu_darbai.classes.Item_order5 import Item, Order

item1 = Item("Laptop", 1000)
item2 = Item("Mouse", 20)
item3 = Item("Keyboard", 50)


order = Order(1)


order.add_item(item1)
order.add_item(item2)
order.add_item(item3)


order.remove_item("Mouse")


total_price = order.calculate_total_price()
print(f'Bendra užsakymo kaina: {total_price} EUR')