# tests/conftest.py

import pytest
import allure

from utilities.config_reader import read_config
from utilities.driver_factory import get_driver

@pytest.fixture(scope="function")
def driver():

    config = read_config()

    driver = get_driver(config)

    driver.get(config["base_url"])

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        allure.attach(
            driver.get_screenshot_as_png(),
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG
        )


config = read_config()

print("\n================ CONFIG DEBUG ================")
print(config)
print("TYPE browser:", type(config["browser"]))
print("VALUE browser:", config["browser"])
print("=============================================\n")