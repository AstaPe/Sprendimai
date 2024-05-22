from namu_darbai.classes.shopping_chart_7 import ShoppingCart

cart = ShoppingCart()


cart.add_item("apple", 5)
cart.add_item("banana", 3)


cart.remove_item("apple", 2)
cart.remove_item("banana", 5)


total_items = cart.get_total_items()
print("Total items in the shopping cart:", total_items)
