from selenium.webdriver.common.keys import Keys

from pages.product_purchase_page import ProductPurchasePage
from pages.shop_page import ShopPage
from pages.view_selected_purchase_and_tariff_page import (
    ViewSelectedPurchaseAndTariffPage,
)


def test_buy_promotional_smartphone_installments_for_6_months(driver):
    page_shop = ShopPage(driver, uri="https://www.a1.by/ru/c/shop")

    page_shop.promotional_products.scroll_to_element().click()

    product_purchase_page = ProductPurchasePage(driver)
    product_purchase_page.tab_new_contract.scroll_to_element().click()
    product_purchase_page.tab_current_contract.scroll_to_element()
    product_purchase_page.type_of_installments.click()
    product_purchase_page.type_of_installments.press_keyboard_button(
        Keys.ARROW_DOWN, count=2
    ).press_keyboard_button(Keys.ENTER)
    product_purchase_page.button_log_in_and_buy.scroll_to_element().click()

    view_selected_purchase_and_tariff_page = ViewSelectedPurchaseAndTariffPage(driver)
    text_selected_equipment = (
        view_selected_purchase_and_tariff_page.appellation_selected_equipment.get_text()
    )
    text_selected_payment = (
        view_selected_purchase_and_tariff_page.appellation_selected_payment.get_text()
    )

    print(
        f"«Выбран {text_selected_equipment}, вариант оплаты: {text_selected_payment}»"
    )

    assert (
        "Xiaomi 11T 128GB небесный голубой",
        "Рассрочка на 6 мес\nC обслуживанием не менее 12 мес от Драйв 5",
    ) == (text_selected_equipment, text_selected_payment)
