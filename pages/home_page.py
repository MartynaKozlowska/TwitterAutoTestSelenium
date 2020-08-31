from selenium.webdriver.common.keys import Keys

from utilities.base import Base
from utilities.locators import HomePageLocators


class HomePage(Base):
    locators = HomePageLocators

    def close_cookies_use_info_bar(self):
        self.click(self.locators.COOKIES_USE_BAR_CLOSE_BUTTON)

    def log_out(self):
        self.click(self.locators.SIDEBAR_ACCOUNT_SWITCHER_BUTTON)
        self.click(self.locators.ACCOUNT_SWITCHER_LOGOUT_BUTTON)

    def send_tweet_with_emoji(self, tweet):
        self.clear_and_send_keys(self.locators.TWEET_DRAFT_INPUT, tweet)
        self.click(self.locators.EMOJIS_POPUP_BUTTON)
        self.click(self.locators.GRINNING_FACE_EMOJI)
        self.press_key(Keys.ESCAPE)
        self.click(self.locators.SEND_TWEET_BUTTON)

    def click_profile_menu_item(self):
        self.click(self.locators.PROFILE_MENU_ITEM)

    def search_twitter(self, phrase):
        self.clear_and_send_keys(self.locators.SEARCH_TWITTER_SEARCHBOX, phrase)
        self.press_key(Keys.ENTER)

    def pick_found_profile(self, profile):
        self.click(self.locator_with_variable(self.locators.FOUND_PROFILE_LABEL, profile))
