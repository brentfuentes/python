"""Taking the order and computing its totals."""
from menu import find_menu_item
from inputs import ask_yes_no, get_valid_quantity


def take_order(menu):
    order_list = []

    while True:
        item_input = input("\nEnter menu item name: ").strip()
        matched_item = find_menu_item(menu, item_input)

        if matched_item is None:
            print(f"  >> '{item_input}' is not on the menu. Please try again.")
            continue

        quantity = get_valid_quantity()
        order_list.append({"item": matched_item, "quantity": quantity})
        print(f"  >> Added: {quantity} x {matched_item}")

        if not ask_yes_no("\nDo you want to order another item? (yes/no): "):
            break

    return order_list


def calculate_order(order_list, menu):
    """Adds unit_price and line_total to each line; returns (order_list, subtotal)."""
    subtotal = 0.0
    for order_line in order_list:
        unit_price = menu[order_line["item"]]
        line_total = unit_price * order_line["quantity"]
        order_line["unit_price"] = unit_price
        order_line["line_total"] = line_total
        subtotal += line_total
    return order_list, subtotal


def get_total_quantity(order_list):
    return sum(order_line["quantity"] for order_line in order_list)