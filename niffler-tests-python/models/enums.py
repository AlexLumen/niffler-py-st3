from dataclasses import dataclass


@dataclass
class Category:
    CATEGORY = "category"
    CATEGORY_EDIT = "edit_category"


@dataclass
class Currency:
    RUB = "RUB"
    KZT = "KZT"
    EUR = "EUR"
    USD = "USD"
