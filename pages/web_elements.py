from time import sleep

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ignored_exceptions = (
    NoSuchElementException,
    StaleElementReferenceException,
)


class WebElements:

    _locator = ("", "")
    _web_driver = None
    _page = None
    _timeout = 45

    def __init__(self, timeout=45, **kwargs):
        self._timeout = timeout

        for attr in kwargs:

            self._locator = (str(attr).replace("_", " "), str(kwargs.get(attr)))

    def find(self, timeout=45):

        element = None

        try:
            element = WebDriverWait(
                self._web_driver, timeout, ignored_exceptions=ignored_exceptions
            ).until(EC.presence_of_element_located(self._locator))
        except Exception:
            print(f"Element with {self._locator} not found on the page!")

        return element

    def get_text(self):

        element = self.find()
        text = ""

        try:
            text = str(element.text)
        except Exception as e:
            print("Error: {0}".format(e))

        return text

    def wait_until_not_visible(self, timeout=45):

        element = None

        try:
            element = WebDriverWait(
                self._web_driver, timeout, ignored_exceptions=ignored_exceptions
            ).until(EC.visibility_of_element_located(self._locator))
        except Exception:
            print(f"Element with {self._locator} not visible!")

        if element:
            js = (
                "return (!(arguments[0].offsetParent === null) && "
                '!(window.getComputedStyle(arguments[0]) === "none") &&'
                "arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0"
                ");"
            )
            visibility = self._web_driver.execute_script(js, element)
            iteration = 0

            while not visibility and iteration < 16:
                sleep(0.5)

                iteration += 1

                visibility = self._web_driver.execute_script(js, element)
                print("Element {0} visibility: {1}".format(self._locator, visibility))

        return element

    def wait_to_be_clickable(self, timeout=45, check_visibility=True):

        element = None

        try:
            element = WebDriverWait(
                self._web_driver, timeout, ignored_exceptions=ignored_exceptions
            ).until(EC.element_to_be_clickable(self._locator))
        except Exception:
            print(f"Element with {self._locator} not clickable!")

        if check_visibility:
            self.wait_until_not_visible()

        return element

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        try:
            element = self.wait_to_be_clickable()

            if element:
                action = ActionChains(self._web_driver)
                action.move_to_element_with_offset(element, x_offset, y_offset).pause(
                    hold_seconds
                ).click(on_element=element).perform()
            else:
                print("No Found Element")
        except Exception as e:
            print(f"{e}: No Click")

    def scroll_to_element(self):

        element = self.find()

        try:
            self._web_driver.execute_script("arguments[0].scrollIntoView();", element)
        except Exception:
            pass
        return self

    def press_keyboard_button(self, key, count=1):
        action = ActionChains(self._web_driver)

        if count > 1:
            start = 0
            while start != count:
                action.key_down(key).key_up(key).perform()
                start += 1
        else:
            action.key_down(key).key_up(key).perform()
        return self
