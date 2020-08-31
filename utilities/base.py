from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.get("https://www.twitter.com")

    def get_element(self, locator):
        self.driver.find_element(*locator)

    @staticmethod
    def locator_with_variable(locator, *args):
        return locator[0], locator[1] % args

    def wait_until_visible(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def clear_and_send_keys(self, locator, keys):
        self.wait_until_visible(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(keys)

    def click(self, locator):
        self.wait_until_visible(locator)
        self.driver.find_element(*locator).click()

    def press_key(self, key):
        action = ActionChains(self.driver)
        action.send_keys(key)
        action.perform()

    def check_if_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

