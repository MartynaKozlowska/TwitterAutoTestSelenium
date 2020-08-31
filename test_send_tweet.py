import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.proflie_page import ProfilePage
from ddt import ddt, file_data
import unittest


@ddt
@pytest.mark.usefixtures("setup_driver")
class SendTweet(unittest.TestCase):

    @file_data('test_data/test_send_tweet_data.json')
    def test_send_tweet(self, login_credentials, tweet):
        # Test sending single tweet and deleting it after

        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        profile_page = ProfilePage(self.driver)
        logout_page = LogoutPage(self.driver)

        login_page.navigate_to_url()
        login_page.fill_in_email_and_password(login_credentials)
        login_page.click_log_in_button()
        login_page.verify_identity_if_required(login_credentials)

        home_page.close_cookies_use_info_bar()
        home_page.send_tweet_with_emoji(tweet)
        home_page.click_profile_menu_item()

        self.assertTrue(profile_page.check_if_tweet_is_visible(tweet), "Tweet is not visible on profile page.")
        profile_page.delete_tweet()
        profile_page.confirm_delete_tweet()
        self.assertTrue(profile_page.check_if_tweet_successfully_deleted(), "Tweet was not deleted successfully.")

        home_page.log_out()

        logout_page.confirm_log_out()
