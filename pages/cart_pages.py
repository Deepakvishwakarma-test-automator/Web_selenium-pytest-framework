# pages/cart_page.py

from pages.base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):

    def get_cart_item_name(self):
        return self.get_text(CartLocators.CART_ITEM)

    def click_checkout(self):
        self.click(CartLocators.CHECKOUT_BUTTON)