"""Menu data and menu-related functions."""
from config import STORE_NAME

# Key = item name, Value = price (float).
MENU = {
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


def display_menu(menu):
    print("=" * 40)
    print(f"{STORE_NAME:^40}")
    print("=" * 40)
    print(f"{'ITEM':<25}{'PRICE':>15}")
    print("-" * 40)
    for item_name, price in menu.items():
        print(f"{item_name:<25}{'PHP ' + format(price, '.2f'):>15}")
    print("=" * 40)


def find_menu_item(menu, user_input_item):
    """Case-insensitive lookup. Returns the proper menu key or None."""
    for item_name in menu:
        if item_name.lower() == user_input_item.strip().lower():
            return item_name
    return None