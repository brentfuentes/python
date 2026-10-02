from config import (
    VAT_RATE, SC_PWD_DISCOUNT, BULK_DISCOUNT, BULK_DISCOUNT_MIN_QTY,
)


class Order:
    """Blueprint for a customer's order.

    Attributes: menu, lines, has_sc_pwd_id
    Methods:    add_item, get_subtotal, get_total_quantity,
                get_discount, get_vat, get_grand_total
    """

    def __init__(self, menu):
        self.menu = menu
        self.lines = []            # [{"item", "quantity", "unit_price", "line_total"}]
        self.has_sc_pwd_id = False

    def add_item(self, item_name, quantity):
        unit_price = self.menu.get_price(item_name)
        self.lines.append({
            "item": item_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "line_total": unit_price * quantity,
        })

    def get_subtotal(self):
        return sum(line["line_total"] for line in self.lines)

    def get_total_quantity(self):
        return sum(line["quantity"] for line in self.lines)

    def get_discount(self):
        """Only the bigger discount applies (no stacking).
        Returns (discount_amount, description)."""
        subtotal = self.get_subtotal()
        sc_pwd_amount = subtotal * SC_PWD_DISCOUNT if self.has_sc_pwd_id else 0.0
        bulk_amount = (
            subtotal * BULK_DISCOUNT
            if self.get_total_quantity() >= BULK_DISCOUNT_MIN_QTY else 0.0
        )

        if sc_pwd_amount >= bulk_amount and sc_pwd_amount > 0:
            return sc_pwd_amount, f"Senior/PWD Discount ({int(SC_PWD_DISCOUNT * 100)}%)"
        elif bulk_amount > 0:
            return bulk_amount, f"Bulk Order Discount ({int(BULK_DISCOUNT * 100)}%)"
        return 0.0, "None"

    def get_vat(self):
        discount_amount, _ = self.get_discount()
        return (self.get_subtotal() - discount_amount) * VAT_RATE

    def get_grand_total(self):
        discount_amount, _ = self.get_discount()
        return (self.get_subtotal() - discount_amount) + self.get_vat()