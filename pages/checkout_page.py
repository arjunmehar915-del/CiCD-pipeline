from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    CONTINUE_BTN = "[data-test='continue']"
    FINISH_BTN = "[data-test='finish']"
    SUMMARY_TOTAL = ".summary_total_label"
    COMPLETE_HEADER = ".complete-header"
    ERROR_MESSAGE = "[data-test='error']"

    def fill_info(self, first: str, last: str, postal: str):
        self.page.fill(self.FIRST_NAME, first)
        self.page.fill(self.LAST_NAME, last)
        self.page.fill(self.POSTAL_CODE, postal)

    def continue_checkout(self):
        self.page.click(self.CONTINUE_BTN)

    def finish_checkout(self):
        self.page.click(self.FINISH_BTN)

    def get_total(self) -> str:
        return self.page.inner_text(self.SUMMARY_TOTAL)

    def get_confirmation_message(self) -> str:
        return self.page.inner_text(self.COMPLETE_HEADER)

    def get_error_message(self) -> str:
        return self.page.inner_text(self.ERROR_MESSAGE)

    def is_error_visible(self) -> bool:
        return self.page.is_visible(self.ERROR_MESSAGE)
