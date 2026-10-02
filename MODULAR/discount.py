"""Discount rules (only the bigger discount applies, no stacking)."""
from config import SC_PWD_DISCOUNT, BULK_DISCOUNT, BULK_DISCOUNT_MIN_QTY
from inputs import ask_yes_no
from order import get_total_quantity


def apply_discount(subtotal, order_list):
    """Returns (discount_amount, description)."""
    sc_pwd_discount_amount = 0.0
    bulk_discount_amount = 0.0

    if ask_yes_no("\nDo you have a Senior Citizen/PWD ID? (yes/no): "):
        sc_pwd_discount_amount = subtotal * SC_PWD_DISCOUNT

    if get_total_quantity(order_list) >= BULK_DISCOUNT_MIN_QTY:
        bulk_discount_amount = subtotal * BULK_DISCOUNT

    if sc_pwd_discount_amount >= bulk_discount_amount and sc_pwd_discount_amount > 0:
        return sc_pwd_discount_amount, f"Senior/PWD Discount ({int(SC_PWD_DISCOUNT * 100)}%)"
    elif bulk_discount_amount > 0:
        return bulk_discount_amount, f"Bulk Order Discount ({int(BULK_DISCOUNT * 100)}%)"
    return 0.0, "None"