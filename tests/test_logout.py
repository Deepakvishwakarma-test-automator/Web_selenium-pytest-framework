import allure
import pytest
import json
import os   
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.config_reader import read_config


PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(PROJECT_ROOT, "test_data", "users.json")


def load_data():
    with open(file_path) as f:
        return json.load(f)

@allure.feature("Logout")
@allure.story("Logout from Inventory Page")
@pytest.mark.parametrize("test_data", load_data())
def test_logout(driver, test_data):

    login_page = LoginPage(driver)
    login_page.login(
        test_data["username"], 
        test_data["password"]
        )

    inventory_page = InventoryPage(driver)
    inventory_page.logout()
