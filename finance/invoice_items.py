from finance.money import Money


# =====================================================
# Discount
# =====================================================

class Discount:

    def __init__(self):

        self._name = ""

        self._percentage = 0.0

        self._amount = Money()

    # ---------------------------------

    def set_name(self, value):

        self._name = value

    def get_name(self):

        return self._name

    # ---------------------------------

    def set_percentage(self, value):

        self._percentage = float(value)

    def get_percentage(self):

        return self._percentage

    # ---------------------------------

    def amount(self):

        return self._amount


# =====================================================
# Tax
# =====================================================

class Tax:

    def __init__(self):

        self._name = ""

        self._percentage = 0.0

        self._amount = Money()

    # ---------------------------------

    def set_name(self, value):

        self._name = value

    def get_name(self):

        return self._name

    # ---------------------------------

    def set_percentage(self, value):

        self._percentage = float(value)

    def get_percentage(self):

        return self._percentage

    # ---------------------------------

    def amount(self):

        return self._amount


# =====================================================
# Invoice Item
# =====================================================

class InvoiceItem:

    def __init__(self):

        self._description = ""

        self._sku = ""

        self._category = ""

        self._quantity = 0

        self._unit_price = Money()

        self._line_total = Money()

        self._discount = Discount()

        self._tax = Tax()

    # ---------------------------------

    def set_description(self, value):

        self._description = value

    def get_description(self):

        return self._description

    # ---------------------------------

    def set_sku(self, value):

        self._sku = value

    def get_sku(self):

        return self._sku

    # ---------------------------------

    def set_category(self, value):

        self._category = value

    def get_category(self):

        return self._category

    # ---------------------------------

    def set_quantity(self, value):

        self._quantity = int(value)

    def get_quantity(self):

        return self._quantity

    # ---------------------------------

    def unit_price(self):

        return self._unit_price

    # ---------------------------------

    def line_total(self):

        return self._line_total

    # ---------------------------------

    def discount(self):

        return self._discount

    # ---------------------------------

    def tax(self):

        return self._tax

    # ---------------------------------

    def __str__(self):

        return (
            f"{self._description} | "
            f"Qty={self._quantity}"
        )


# =====================================================
# Item Collection
# =====================================================

class ItemCollection:

    def __init__(self):

        self._items = []

    # ---------------------------------

    def add(self, item):

        self._items.append(item)

    # ---------------------------------

    def remove(self, item):

        self._items.remove(item)

    # ---------------------------------

    def clear(self):

        self._items.clear()

    # ---------------------------------

    def count(self):

        return len(self._items)

    # ---------------------------------

    def get(self, index):

        return self._items[index]

    # ---------------------------------

    def get_all(self):

        return self._items

    # ---------------------------------

    def total_quantity(self):

        total = 0

        for item in self._items:

            total += item.get_quantity()

        return total
