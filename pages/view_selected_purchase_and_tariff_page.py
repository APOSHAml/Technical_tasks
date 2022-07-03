from pages.web_elements import WebElements
from pages.web_page import WebPage


class ViewSelectedPurchaseAndTariffPage(WebPage):
    def __init__(self, web_driver, uri: str = ""):

        super().__init__(web_driver, uri)

    appellation_selected_equipment = WebElements(
        css_selector="div.product-info-title > a > span"
    )

    appellation_selected_payment = WebElements(css_selector='[class="product-info"]')
