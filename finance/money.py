from enum import Enum
from datetime import datetime


# ===========================================================
# Currency Type
# ===========================================================

class CurrencyType(Enum):

    UNKNOWN = 0

    USD = 1
    EUR = 2
    GBP = 3
    INR = 4
    JPY = 5
    CNY = 6
    AUD = 7
    CAD = 8
    CHF = 9


# ===========================================================
# Currency
# ===========================================================

class Currency:

    def __init__(self):

        self._type = CurrencyType.UNKNOWN

        self._name = ""

        self._iso = ""

        self._symbol = ""

        self._native_symbol = ""

        self._numeric_iso = 0

        self._decimal_places = 2

    # -------------------------

    def set_type(self, value):

        self._type = value

    def get_type(self):

        return self._type

    # -------------------------

    def set_name(self, value):

        self._name = value

    def get_name(self):

        return self._name

    # -------------------------

    def set_iso(self, value):

        self._iso = value

    def get_iso(self):

        return self._iso

    # -------------------------

    def set_symbol(self, value):

        self._symbol = value

    def get_symbol(self):

        return self._symbol

    # -------------------------

    def set_native_symbol(self, value):

        self._native_symbol = value

    def get_native_symbol(self):

        return self._native_symbol

    # -------------------------

    def set_numeric_iso(self, value):

        self._numeric_iso = value

    def get_numeric_iso(self):

        return self._numeric_iso

    # -------------------------

    def set_decimal_places(self, value):

        self._decimal_places = value

    def get_decimal_places(self):

        return self._decimal_places


# ===========================================================
# Money
# ===========================================================

class Money:

    def __init__(self):

        self._amount = 0.0

        self._currency = Currency()

    # -------------------------

    def set_amount(self, value):

        self._amount = float(value)

    def get_amount(self):

        return self._amount

    # -------------------------

    def currency(self):

        return self._currency

    # -------------------------

    def __str__(self):

        return f"{self._currency.get_symbol()}{self._amount:,.2f}"


# ===========================================================
# Exchange Rate
# ===========================================================

class ExchangeRate:

    def __init__(self):

        self._from = CurrencyType.UNKNOWN

        self._to = CurrencyType.UNKNOWN

        self._rate = 1.0

        self._timestamp = datetime.now()

    def set_from(self, value):

        self._from = value

    def set_to(self, value):

        self._to = value

    def set_rate(self, value):

        self._rate = value

    def get_rate(self):

        return self._rate


# ===========================================================
# Exchange Rate Cache
# ===========================================================

class ExchangeRateCache:

    def __init__(self):

        self._rates = {}

    def add(self, rate):

        key = (rate._from, rate._to)

        self._rates[key] = rate

    def get(self, frm, to):

        return self._rates.get((frm, to))


# ===========================================================
# Currency Converter
# ===========================================================

class CurrencyConverter:

    SYMBOL_TABLE = {

        "$": CurrencyType.USD,
        "€": CurrencyType.EUR,
        "£": CurrencyType.GBP,
        "₹": CurrencyType.INR,
        "¥": CurrencyType.JPY,
        "C$": CurrencyType.CAD,
        "A$": CurrencyType.AUD

    }

    def __init__(self):

        self._cache = ExchangeRateCache()

    # ------------------------------------------------------

    def detect_currency(self, text):

        for symbol, currency in self.SYMBOL_TABLE.items():

            if text.startswith(symbol):

                return currency

        return CurrencyType.UNKNOWN

    # ------------------------------------------------------

    def parse_money(self, text):

        money = Money()

        currency = Currency()

        ctype = self.detect_currency(text)

        currency.set_type(ctype)

        if ctype == CurrencyType.USD:

            currency.set_symbol("$")
            currency.set_iso("USD")
            currency.set_name("US Dollar")

        elif ctype == CurrencyType.EUR:

            currency.set_symbol("€")
            currency.set_iso("EUR")
            currency.set_name("Euro")

        elif ctype == CurrencyType.INR:

            currency.set_symbol("₹")
            currency.set_iso("INR")
            currency.set_name("Indian Rupee")

        value = text

        for s in self.SYMBOL_TABLE.keys():

            value = value.replace(s, "")

        value = value.replace(",", "")

        money.set_amount(value)

        money._currency = currency

        return money

    # ------------------------------------------------------

    def convert(self, money, exchange_rate):

        result = Money()

        result._currency = money.currency()

        result.set_amount(

            money.get_amount() * exchange_rate.get_rate()

        )

        return result
