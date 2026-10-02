"""Receipt printing."""
from config import STORE_NAME, STORE_ADDRESS, VAT_RATE


def print_receipt(order_list, subtotal, discount_amount, discount_description):
    vat_amount = (subtotal - discount_amount) * VAT_RATE
    grand_total = (subtotal - discount_amount) + vat_amount

    print("\n" + "=" * 40)
    print(f"{STORE_NAME:^40}")
    print(f"{STORE_ADDRESS:^40}")
    print("=" * 40)
    print(f"{'QTY':<5}{'ITEM':<20}{'AMOUNT':>15}")
    print("-" * 40)

    for line in order_list:
        print(f"{line['quantity']:<5}{line['item']:<20}{format(line['line_total'], '.2f'):>15}")
        print(f"{'':<5}{'@ PHP ' + format(line['unit_price'], '.2f'):<20}")

    print("-" * 40)
    print(f"{'Subtotal:':<25}{format(subtotal, '.2f'):>15}")
    print(f"{'Discount (' + discount_description + '):':<25}{format(discount_amount, '.2f'):>15}")
    print(f"{'VAT (12%):':<25}{format(vat_amount, '.2f'):>15}")
    print("=" * 40)
    print(f"{'TOTAL:':<25}{format(grand_total, '.2f'):>15}")
    print("=" * 40)
    print(f"{'Thank you for ordering!':^40}")
    print("=" * 40)