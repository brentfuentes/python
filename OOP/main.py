"""
Prelim Performance Task: Restaurant Ordering System (Python OOP version)
Run with:  python main.py
"""
from menu import Menu
from order import Order
from receipt import Receipt
from input_helpers import ask_yes_no, get_valid_quantity


def take_order(menu):
    order = Order(menu)

    while True:
        item_input = input("\nEnter menu item name: ").strip()
        matched_item = menu.find_item(item_input)

        if matched_item is None:
            print(f"  >> '{item_input}' is not on the menu. Please try again.")
            continue

        quantity = get_valid_quantity()
        order.add_item(matched_item, quantity)
        print(f"  >> Added: {quantity} x {matched_item}")

        if not ask_yes_no("\nDo you want to order another item? (yes/no): "):
            break

    return order


def main():
    menu = Menu()
    menu.display()

    if not ask_yes_no("\nWould you like to order? (yes/no): "):
        print("\nThank you for visiting! Goodbye.")
        return

    order = take_order(menu)
    order.has_sc_pwd_id = ask_yes_no("\nDo you have a Senior Citizen/PWD ID? (yes/no): ")
    Receipt(order).print()


if __name__ == "__main__":
    main()