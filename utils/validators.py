import re


def is_valid_username(username: str) -> bool:
    return bool(username and username.strip())


def is_valid_price(price_str: str) -> bool:
    return bool(re.match(r"^\$\d+\.\d{2}$", price_str))


def is_sorted_ascending(items: list) -> bool:
    return items == sorted(items)


def is_sorted_descending(items: list) -> bool:
    return items == sorted(items, reverse=True)


def is_valid_product_name(name: str) -> bool:
    return bool(name and len(name.strip()) > 0)


def cart_total_matches(prices: list[float], expected: float) -> bool:
    return round(sum(prices), 2) == round(expected, 2)
