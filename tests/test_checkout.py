# tests/test_checkout.py

import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_pages import CartPage
from pages.checkout_page import CheckoutPage
from utilities.config_reader import read_config




@allure.feature("Checkout")
@allure.story("Complete Checkout Flow")
def test_complete_checkout(driver):

    config = read_config()

    login_page = LoginPage(driver)

    login_page.login(
        config["credentials"]["username"],
        config["credentials"]["password"]
    )

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)

    assert cart_page.get_cart_item_name() == "Sauce Labs Backpack"

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    checkout_page.enter_checkout_information(
        "John",
        "Doe",
        "122001"
    )

    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert (
        checkout_page.get_success_message()
        == "Thank you for your order!"
    )