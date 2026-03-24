import pytest
from utils.validators import (
    is_valid_username,
    is_valid_price,
    is_sorted_ascending,
    is_sorted_descending,
    is_valid_product_name,
    cart_total_matches,
)


@pytest.mark.unit
class TestValidators:

    def test_valid_username(self):
        assert is_valid_username("standard_user") is True

    def test_empty_username_is_invalid(self):
        assert is_valid_username("") is False

    def test_whitespace_username_is_invalid(self):
        assert is_valid_username("   ") is False

    def test_valid_price_format(self):
        assert is_valid_price("$29.99") is True

    def test_invalid_price_no_dollar(self):
        assert is_valid_price("29.99") is False

    def test_invalid_price_no_cents(self):
        assert is_valid_price("$29") is False

    def test_sorted_ascending(self):
        assert is_sorted_ascending(["Apple", "Banana", "Cherry"]) is True

    def test_not_sorted_ascending(self):
        assert is_sorted_ascending(["Banana", "Apple", "Cherry"]) is False

    def test_sorted_descending(self):
        assert is_sorted_descending(["Cherry", "Banana", "Apple"]) is True

    def test_valid_product_name(self):
        assert is_valid_product_name("Sauce Labs Backpack") is True

    def test_empty_product_name_invalid(self):
        assert is_valid_product_name("") is False

    def test_cart_total_matches(self):
        assert cart_total_matches([9.99, 7.99, 15.99], 33.97) is True

    def test_cart_total_mismatch(self):
        assert cart_total_matches([9.99, 7.99], 20.00) is False
