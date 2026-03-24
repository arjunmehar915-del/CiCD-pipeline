import pytest
from utils.validators import is_sorted_ascending, is_sorted_descending


@pytest.mark.e2e
class TestFullPurchaseFlow:

    def test_complete_checkout_flow(self, inventory_page, config):
        from pages.cart_page import CartPage
        from pages.checkout_page import CheckoutPage

        inventory_page.add_first_item_to_cart()
        inventory_page.go_to_cart()

        cart = CartPage(inventory_page.page, config.BASE_URL)
        assert cart.get_item_count() == 1
        cart.proceed_to_checkout()

        checkout = CheckoutPage(inventory_page.page, config.BASE_URL)
        checkout.fill_info("John", "Doe", "12345")
        checkout.continue_checkout()
        checkout.finish_checkout()

        assert "Thank you" in checkout.get_confirmation_message()

    def test_checkout_without_info_shows_error(self, checkout_page):
        checkout_page.continue_checkout()
        assert checkout_page.is_error_visible()
        assert "First Name" in checkout_page.get_error_message()

    def test_checkout_without_last_name_shows_error(self, checkout_page):
        checkout_page.fill_info("John", "", "12345")
        checkout_page.continue_checkout()
        assert checkout_page.is_error_visible()

    def test_checkout_without_postal_shows_error(self, checkout_page):
        checkout_page.fill_info("John", "Doe", "")
        checkout_page.continue_checkout()
        assert checkout_page.is_error_visible()

    def test_order_total_is_displayed_on_summary(self, checkout_page):
        checkout_page.fill_info("John", "Doe", "12345")
        checkout_page.continue_checkout()
        total = checkout_page.get_total()
        assert "Total:" in total


@pytest.mark.e2e
class TestSortingFlow:

    def test_sort_products_name_ascending(self, inventory_page):
        inventory_page.sort_by("az")
        names = inventory_page.get_product_names()
        assert is_sorted_ascending(names)

    def test_sort_products_name_descending(self, inventory_page):
        inventory_page.sort_by("za")
        names = inventory_page.get_product_names()
        assert is_sorted_descending(names)

    def test_sort_products_price_low_to_high(self, inventory_page):
        inventory_page.sort_by("lohi")
        prices = [float(p.replace("$", "")) for p in inventory_page.get_product_prices()]
        assert prices == sorted(prices)

    def test_sort_products_price_high_to_low(self, inventory_page):
        inventory_page.sort_by("hilo")
        prices = [float(p.replace("$", "")) for p in inventory_page.get_product_prices()]
        assert prices == sorted(prices, reverse=True)


@pytest.mark.e2e
class TestLogoutFlow:

    def test_logout_redirects_to_login(self, inventory_page):
        inventory_page.logout()
        assert inventory_page.get_url().rstrip("/") == "https://www.saucedemo.com"

    def test_cannot_access_inventory_after_logout(self, inventory_page, config):
        inventory_page.logout()
        inventory_page.navigate("inventory.html")
        assert "inventory" not in inventory_page.get_url()
