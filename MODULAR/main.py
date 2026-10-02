"""
Prelim Performance Task: Restaurant Ordering System (Modular version)
Run with:  python main.py
"""
from menu import MENU, display_menu
from inputs import ask_yes_no
from order import take_order, calculate_order
from discount import apply_discount
from receipt import print_receipt


def main():
    display_menu(MENU)

    if not ask_yes_no("\nWould you like to order? (yes/no): "):
        print("\nThank you for visiting! Goodbye.")
        return

    order_list = take_order(MENU)
    order_list, subtotal = calculate_order(order_list, MENU)
    discount_amount, discount_description = apply_discount(subtotal, order_list)
    print_receipt(order_list, subtotal, discount_amount, discount_description)


if __name__ == "__main__":
    main()