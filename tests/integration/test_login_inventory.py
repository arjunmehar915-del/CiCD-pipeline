import pytest
from utils.validators import is_valid_price


@pytest.mark.integration
class TestLoginInventoryIntegration:

    def test_successful_login_redirects_to_inventory(self, login_page):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        assert "inventory" in login_page.get_url()

    def test_locked_user_cannot_login(self, login_page, config):
        login_page.open()
        login_page.login(config.LOCKED_USER, config.PASSWORD)
        assert login_page.is_error_visible()
        assert "locked out" in login_page.get_error_message().lower()

    def test_wrong_password_shows_error(self, login_page):
        login_page.open()
        login_page.login("standard_user", "wrong_password")
        assert login_page.is_error_visible()

    def test_inventory_loads_products_after_login(self, inventory_page):
        names = inventory_page.get_product_names()
        assert len(names) == 6

    def test_all_product_prices_are_valid_format(self, inventory_page):
        prices = inventory_page.get_product_prices()
        assert all(is_valid_price(p) for p in prices)


@pytest.mark.integration
class TestCartInventoryIntegration:

    def test_add_item_updates_cart_badge(self, inventory_page):
        inventory_page.add_first_item_to_cart()
        assert inventory_page.get_cart_count() == 1

    def test_cart_contains_added_item(self, cart_page):
        assert cart_page.get_item_count() == 1

    def test_remove_item_from_cart(self, cart_page):
        cart_page.remove_first_item()
        assert cart_page.get_item_count() == 0

    def test_continue_shopping_returns_to_inventory(self, cart_page):
        cart_page.continue_shopping()
        assert "inventory" in cart_page.get_url()
