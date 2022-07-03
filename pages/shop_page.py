from pages.web_elements import WebElements
from pages.web_page import WebPage


class ShopPage(WebPage):
    def __init__(self, web_driver, uri: str = ""):

        super().__init__(web_driver, uri)

    promotional_products = WebElements(id="promo-product-button_0")
