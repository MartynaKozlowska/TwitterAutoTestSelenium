from selenium.webdriver.common.keys import Keys

from utilities.base import Base
from utilities.locators import ProfilePageLocators


class ProfilePage(Base):
    locators = ProfilePageLocators

    # My Profile Page
    def check_if_tweet_is_visible(self, tweet):
        return self.check_if_visible(self.locator_with_variable(self.locators.BOX_WITH_POSTED_TWEET, tweet))

    def delete_tweet(self):
        self.click(self.locators.MORE_EXPAND_BUTTON)
        self.click(self.locators.DELETE_TWEET_OPTION)

    def confirm_delete_tweet(self):
        self.press_key(Keys.ENTER)

    def check_if_tweet_successfully_deleted(self):
        return self.check_if_visible(self.locators.TWEET_DELETED_CONFIRMATION_POPUP, 10)

    def check_if_retweet_is_visible(self):
        return self.check_if_visible(self.locators.YOU_RETWEETED_LABEL)

    def undo_retweet(self):
        self.click(self.locators.UNRETWEET_EXPAND_BUTTON)
        self.click(self.locators.CONFIRM_UNDO_RETWEET_BUTTON)

    def check_if_profile_has_no_tweets(self):
        return self.check_if_visible(self.locators.NO_TWEETS_LABEL)

    # Other Profile Pages
    def retweet_chosen_tweet(self, tweet_number):
        self.click(self.locator_with_variable(self.locators.RETWEET_EXPAND_BUTTON, tweet_number))
        self.click(self.locators.CONFIRM_RETWEET_BUTTON)

    def follow_profile(self):
        self.click(self.locators.FOLLOW_BUTTON)

    def check_if_profile_is_followed(self):
        return self.check_if_visible(self.locators.UNFOLLOW_BUTTON)

    def unfollow_profile(self):
        if self.check_if_visible(self.locators.SUGGESTED_PROFILES_LABEL):
            self.click(self.locators.UNFOLLOW_BUTTON)
            self.click(self.locators.CONFIRM_UNFOLLOW_BUTTON)
