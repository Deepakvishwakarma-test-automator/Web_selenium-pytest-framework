# locators/cart_locators.py

from selenium.webdriver.common.by import By


class CartLocators:

    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")

    CHECKOUT_BUTTON = (By.ID, "checkout")