# pages/checkout_page.py

from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):

    def enter_checkout_information(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.type(CheckoutLocators.FIRST_NAME, first_name)
        self.type(CheckoutLocators.LAST_NAME, last_name)
        self.type(CheckoutLocators.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.click(CheckoutLocators.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(CheckoutLocators.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(CheckoutLocators.SUCCESS_MESSAGE)