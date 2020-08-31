import pytest
from ddt import ddt, file_data
import unittest

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.logout_page import LogoutPage


@ddt
@pytest.mark.usefixtures("setup_driver")
class LoginInAndOut(unittest.TestCase):

    @file_data('test_data/test_log_in_and_out_data.json')
    def test_log_in_and_log_out(self, login_credentials):
        # Test logging in and logging out

        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        logout_page = LogoutPage(self.driver)

        login_page.navigate_to_url()
        self.assertTrue(login_page.check_if_sidebar_headers_are_visible(), "Not all sidebar headers are visible.")
        login_page.fill_in_email_and_password(login_credentials)
        login_page.click_log_in_button()
        login_page.verify_identity_if_required(login_credentials)
        self.assertTrue(login_page.was_login_successful(), "Login not successful - check your credentials.")

        home_page.close_cookies_use_info_bar()
        home_page.log_out()

        logout_page.confirm_log_out()
