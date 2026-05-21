# locators/inventory_locators.py

from selenium.webdriver.common.by import By


class InventoryLocators:

    TITLE = (By.CLASS_NAME, "title")

    ADD_TO_CART_BACKPACK = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")