import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """'driver.implicitly_wait(45)': can be used
    'options.headless = True': without launching browser"""
    options = Options()
    options.add_argument("start-maximized")

    print("\nstart chrome browser for test..")
    driver = webdriver.Chrome(options=options)

    yield driver
    print("\nquit browser..")

    driver.quit()
