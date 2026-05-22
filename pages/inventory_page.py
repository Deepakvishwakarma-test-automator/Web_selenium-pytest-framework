# pages/inventory_page.py

from pages.base_page import BasePage
from locators.inventory_locators import InventoryLocators


class InventoryPage(BasePage):

    def get_page_title(self):
        return self.get_text(InventoryLocators.TITLE)

    def add_backpack_to_cart(self):
        self.click(InventoryLocators.ADD_TO_CART_BACKPACK)

    def open_cart(self):
        self.click(InventoryLocators.SHOPPING_CART)

    def open_menu(self):
        self.click(InventoryLocators.MENU_BUTTON)

    def logout(self):
        self.open_menu()
        self.click(InventoryLocators.LOGOUT_BUTTON) 
        