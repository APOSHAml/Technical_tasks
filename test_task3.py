import pytest
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def driver():

    options = Options()
    options.add_argument("start-maximized")
    print("\nstart chrome browser for test..")
    driver = webdriver.Chrome(options=options)

    yield driver
    print("\nquit browser..")

    driver.quit()


ignored_exceptions = (
    NoSuchElementException,
    StaleElementReferenceException,
)


def test_buy_promotional_smartphone_installments_for_6_months(
    driver: WebDriver, uri: str = "https://www.a1.by/ru/c/shop"
):

    driver.get(uri)

    promotional_products = driver.find_element(By.ID, "promo-product-button_0")

    driver.execute_script("arguments[0].scrollIntoView();", promotional_products)

    WebDriverWait(driver, 25, ignored_exceptions=ignored_exceptions).until(
        EC.text_to_be_present_in_element((By.ID, "promo-product-button_0"), "Подробнее")
    )

    WebDriverWait(driver, 25, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable((By.ID, "promo-product-button_0"))
    )

    promotional_products.click()

    tab_new_contract = driver.find_element(By.CSS_SELECTOR, '[data-pane-id="NEW_CONTRACT"]')

    tab_new_contract.click()

    tab_current_contract = driver.find_element(
        By.CSS_SELECTOR, '[data-ajax-uid="velcomProductPurchaseConditionsComponent"]'
    )
    driver.execute_script("arguments[0].scrollIntoView();", tab_current_contract)

    WebDriverWait(driver, 50, ignored_exceptions=ignored_exceptions).until(
        EC.text_to_be_present_in_element(
            (
                By.CSS_SELECTOR,
                "#NEW_CONTRACT > div.live-filter > div.live-filter-controls > div > label",
            ),
            "24 мес по 75,79 руб/мес",
        )
    )
    type_of_installments = driver.find_element(
        By.CSS_SELECTOR,
        "#NEW_CONTRACT > div.live-filter > div.live-filter-controls > div > label",
    )

    type_of_installments.click()

    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    button_log_in_and_buy = driver.find_element(
        By.CSS_SELECTOR,
        "div.live-filter-content-item.active > form > div.price-block-button > button",
    )

    driver.execute_script("arguments[0].scrollIntoView();", button_log_in_and_buy)
    WebDriverWait(driver, 50, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "div.live-filter-content-item.active > form > div.price-block-button > button",
            )
        )
    )
    WebDriverWait(driver, 50, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "div.live-filter-content-item.active > form > div.price-block-button > button",
            )
        )
    )
    button_log_in_and_buy.click()

    appellation_selected_equipment = driver.find_element(
        By.CSS_SELECTOR, "div.product-info-title > a > span"
    )
    appellation_selected_payment = driver.find_element(
        By.CSS_SELECTOR, '[class="product-info"]'
    )


    print(f'«Выбран {appellation_selected_equipment.text}, вариант оплаты: {appellation_selected_payment.text}»')

    assert (
        "Xiaomi 11T 128GB небесный голубой",
        "Рассрочка на 6 мес\nC обслуживанием не менее 12 мес от Драйв 5",
    ) == (appellation_selected_equipment.text, appellation_selected_payment.text)
