import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.proflie_page import ProfilePage
from ddt import ddt, file_data
import unittest


@ddt
@pytest.mark.usefixtures("setup_driver")
class FollowAndRetweet(unittest.TestCase):

    @file_data('test_data/test_retweet_and_follow_data.json')
    def test_follow_and_retweet(self, login_credentials, searched_phrase, profile_name, tweet_number):
        # Test retweeting, following and unfollowing someone, deleting the retweet after

        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        profile_page = ProfilePage(self.driver)
        logout_page = LogoutPage(self.driver)

        login_page.navigate_to_url()
        login_page.fill_in_email_and_password(login_credentials)
        login_page.click_log_in_button()
        login_page.verify_identity_if_required(login_credentials)

        home_page.close_cookies_use_info_bar()
        home_page.search_twitter(searched_phrase)
        home_page.pick_found_profile(profile_name)

        profile_page.retweet_chosen_tweet(tweet_number)
        profile_page.follow_profile()
        self.assertTrue(profile_page.check_if_profile_is_followed(), "Profile is not followed.")
        profile_page.unfollow_profile()

        home_page.click_profile_menu_item()

        self.assertTrue(profile_page.check_if_retweet_is_visible(), "Retweet is not visible on profile page.")
        profile_page.undo_retweet()
        self.assertTrue(profile_page.check_if_profile_has_no_tweets(), "Retweet was not deleted successfully.")

        home_page.log_out()

        logout_page.confirm_log_out()
