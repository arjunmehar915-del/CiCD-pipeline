from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_ITEM = ".inventory_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ADD_TO_CART_BTN = "button[data-test^='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def get_product_names(self) -> list[str]:
        return self.page.locator(self.ITEM_NAME).all_inner_texts()

    def get_product_prices(self) -> list[str]:
        return self.page.locator(self.ITEM_PRICE).all_inner_texts()

    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN).first.click()

    def add_item_by_name(self, name: str):
        btn_test_id = f"add-to-cart-{name.lower().replace(' ', '-')}"
        self.page.click(f"[data-test='{btn_test_id}']")

    def get_cart_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        return int(badge.inner_text()) if badge.is_visible() else 0

    def sort_by(self, option: str):
        self.page.select_option(self.SORT_DROPDOWN, option)

    def logout(self):
        self.page.click(self.MENU_BUTTON)
        self.page.click(self.LOGOUT_LINK)

    def go_to_cart(self):
        self.page.click(".shopping_cart_link")
