from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(config):

    browser = config.get("browser")

    if isinstance(browser, str):
        browser_name = browser.lower()
        headless = False
    else:
        browser_name = browser.get("name", "chrome").lower()
        headless = browser.get("headless", False)


    if browser_name == "chrome":

        options = ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

        return driver


    elif browser_name == "firefox":

        options = FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

        driver.maximize_window()

        return driver

    else:
        raise Exception(f"Browser not supported: {browser_name}")