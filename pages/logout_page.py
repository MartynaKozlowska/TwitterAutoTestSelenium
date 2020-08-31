from selenium.webdriver.common.keys import Keys

from utilities.base import Base
from utilities.locators import LogoutPageLocators


class LogoutPage(Base):
    locators = LogoutPageLocators

    def confirm_log_out(self):
        self.press_key(Keys.ENTER)
