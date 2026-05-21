import allure
import json
import pytest
import os

from pages.login_page import LoginPage
from utilities.config_reader import read_config


PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(PROJECT_ROOT, "test_data", "users.json")


def load_data():
    with open(file_path) as f:
        return json.load(f)


@allure.feature("Login")
@allure.story("Valid Login")
@pytest.mark.parametrize("data", load_data())
def test_login(driver, data):

    page = LoginPage(driver)
    page.login(
        data["username"], 
        data["password"]
        )

    if data["expected"]:
        assert "dashboard" in driver.current_url
    else:
        assert "login" in driver.current_url