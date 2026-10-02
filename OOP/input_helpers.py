"""Reusable, validated user-input prompts (handles human error)."""


def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        print("  >> Invalid input. Please answer with 'yes' or 'no'.\n")


def get_valid_quantity():
    while True:
        quantity_input = input("Enter quantity: ").strip()
        if quantity_input.isdigit() and int(quantity_input) > 0:
            return int(quantity_input)
        print("  >> Invalid quantity. Please enter a whole number greater than 0.\n")