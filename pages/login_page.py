from utilities.base import Base
from utilities.locators import LoginPageLocators


class LoginPage(Base):
    locators = LoginPageLocators

    def check_if_sidebar_headers_are_visible(self):
        for x in range(1, 3):
            if self.check_if_visible(self.locator_with_variable(self.locators.SIDEBAR_HEADERS, x)):
                return True

    def fill_in_email_and_password(self, credentials):
        self.clear_and_send_keys(self.locators.USERNAME_OR_EMAIL_INPUT, credentials['email'])
        self.clear_and_send_keys(self.locators.PASSWORD_INPUT, credentials['password'])

    def click_log_in_button(self):
        self.click(self.locators.LOGIN_BUTTON)

    def was_login_successful(self):
        if self.check_if_visible(self.locators.LOGIN_ERROR_MESSAGE_1):
            return False
        else:
            return True

    def verify_identity_if_required(self, credentials):
        if self.check_if_visible(self.locators.LOGIN_ERROR_MESSAGE_2):
            self.clear_and_send_keys(self.locators.USERNAME_OR_EMAIL_INPUT, credentials['username'])
            self.clear_and_send_keys(self.locators.PASSWORD_INPUT, credentials['password'])
            self.click(self.locators.LOGIN_BUTTON)
