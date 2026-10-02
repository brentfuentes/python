from config import STORE_NAME


class Menu:
    """Blueprint for the restaurant menu.

    Attributes: items (dict of item name -> price)
    Methods:    display, find_item, get_price
    """

    def __init__(self, items=None):
        self.items = items if items is not None else {
            "Cheeseburger": 89.00,
            "Chicken Sandwich": 109.00,
            "Fries (Regular)": 59.00,
            "Fries (Large)": 79.00,
            "Nuggets (6pcs)": 99.00,
            "Spaghetti": 69.00,
            "Iced Tea": 45.00,
            "Soda (Regular)": 49.00,
            "Sundae": 39.00,
            "Rice": 25.00,
        }

    def display(self):
        print("=" * 40)
        print(f"{STORE_NAME:^40}")
        print("=" * 40)
        print(f"{'ITEM':<25}{'PRICE':>15}")
        print("-" * 40)
        for item_name, price in self.items.items():
            print(f"{item_name:<25}{'PHP ' + format(price, '.2f'):>15}")
        print("=" * 40)

    def find_item(self, user_input_item):
        """Case-insensitive lookup. Returns the proper menu key or None."""
        wanted = user_input_item.strip().lower()
        for item_name in self.items:
            if item_name.lower() == wanted:
                return item_name
        return None

    def get_price(self, item_name):
        return self.items[item_name]