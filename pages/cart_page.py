from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    CHECKOUT_BTN = "[data-test='checkout']"
    REMOVE_BTN = "button[data-test^='remove']"
    CONTINUE_SHOPPING_BTN = "[data-test='continue-shopping']"

    def get_cart_items(self) -> list[str]:
        return self.page.locator(self.ITEM_NAME).all_inner_texts()

    def get_cart_prices(self) -> list[str]:
        return self.page.locator(self.ITEM_PRICE).all_inner_texts()

    def remove_first_item(self):
        self.page.locator(self.REMOVE_BTN).first.click()

    def proceed_to_checkout(self):
        self.page.click(self.CHECKOUT_BTN)

    def continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING_BTN)

    def get_item_count(self) -> int:
        return self.page.locator(self.CART_ITEM).count()
