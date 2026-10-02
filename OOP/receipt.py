from config import STORE_NAME, STORE_ADDRESS


class Receipt:
    """Blueprint for a printable receipt built from an Order."""

    def __init__(self, order):
        self.order = order

    def print(self):
        order = self.order
        discount_amount, discount_description = order.get_discount()

        print("\n" + "=" * 40)
        print(f"{STORE_NAME:^40}")
        print(f"{STORE_ADDRESS:^40}")
        print("=" * 40)
        print(f"{'QTY':<5}{'ITEM':<20}{'AMOUNT':>15}")
        print("-" * 40)

        for line in order.lines:
            print(f"{line['quantity']:<5}{line['item']:<20}{format(line['line_total'], '.2f'):>15}")
            print(f"{'':<5}{'@ PHP ' + format(line['unit_price'], '.2f'):<20}")

        print("-" * 40)
        print(f"{'Subtotal:':<25}{format(order.get_subtotal(), '.2f'):>15}")
        print(f"{'Discount (' + discount_description + '):':<25}{format(discount_amount, '.2f'):>15}")
        print(f"{'VAT (12%):':<25}{format(order.get_vat(), '.2f'):>15}")
        print("=" * 40)
        print(f"{'TOTAL:':<25}{format(order.get_grand_total(), '.2f'):>15}")
        print("=" * 40)
        print(f"{'Thank you for ordering!':^40}")
        print("=" * 40)