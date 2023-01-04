import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        element = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(by_locator))
        element.click()

    def click_using_js(self, by_locator):
        element = WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].click();", element)

    def input_element(self, by_locator: object, text: object) -> object:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def upload_element(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return element.text

    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute_name):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    def verify_element_display(self, by_locator):
        self.wait(2)
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).is_displayed()

    def verify_element_enable(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator))
        return element.is_enabled()

    def get_web_element(self, by_locator):
        element = WebDriverWait(self.driver, 35).until(EC.visibility_of_element_located(by_locator))
        return element

    def wait(self, seconds=3):
        time.sleep(seconds)

    def move_to_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def assert_equal(self, actual_value, expected_value, Message):
        self.wait(30)
        assert actual_value == expected_value, Message

    def verify_element_disabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.is_enabled()

    def get_all_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for ele in elements:
            return ele.text

