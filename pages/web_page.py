from typing import Any

from selenium.webdriver.chrome.webdriver import WebDriver


class WebPage:
    _web_driver = None

    def __init__(self, web_driver: WebDriver, uri=""):

        self._web_driver = web_driver
        self.get_url(uri)

    def __getattribute__(self, item: Any):
        attr = object.__getattribute__(self, item)

        if not item.startswith("_") and not callable(attr):
            attr._web_driver = self._web_driver
            attr._page = self

        return attr

    def get_url(self, uri: str):

        if uri:
            self._web_driver.get(uri)
