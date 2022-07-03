from pages.web_elements import WebElements
from pages.web_page import WebPage


class ProductPurchasePage(WebPage):
    def __init__(self, web_driver, uri: str = ""):

        super().__init__(web_driver, uri)

    tab_new_contract = WebElements(css_selector='[data-pane-id="NEW_CONTRACT"]')

    tab_current_contract = WebElements(
        css_selector='[data-ajax-uid="velcomProductPurchaseConditionsComponent"]'
    )

    type_of_installments = WebElements(
        css_selector="#NEW_CONTRACT > div.live-filter > div.live-filter-controls > div > label"
    )

    button_log_in_and_buy = WebElements(
        css_selector="div.live-filter-content-item.active > form > div.price-block-button > button"
    )
