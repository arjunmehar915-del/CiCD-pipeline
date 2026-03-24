import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope="session")
def config():
    return Config()


@pytest.fixture(scope="function")
def browser_page(config):
    with sync_playwright() as p:
        browser = getattr(p, config.BROWSER).launch(headless=config.HEADLESS)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def login_page(browser_page, config):
    return LoginPage(browser_page, config.BASE_URL)


@pytest.fixture(scope="function")
def logged_in_page(browser_page, config):
    lp = LoginPage(browser_page, config.BASE_URL)
    lp.open()
    lp.login(config.STANDARD_USER, config.PASSWORD)
    return browser_page


@pytest.fixture(scope="function")
def inventory_page(logged_in_page, config):
    return InventoryPage(logged_in_page, config.BASE_URL)


@pytest.fixture(scope="function")
def cart_page(logged_in_page, config):
    inv = InventoryPage(logged_in_page, config.BASE_URL)
    inv.add_first_item_to_cart()
    inv.go_to_cart()
    return CartPage(logged_in_page, config.BASE_URL)


@pytest.fixture(scope="function")
def checkout_page(cart_page, logged_in_page, config):
    cart_page.proceed_to_checkout()
    return CheckoutPage(logged_in_page, config.BASE_URL)
