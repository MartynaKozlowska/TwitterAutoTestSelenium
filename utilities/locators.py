from selenium.webdriver.common.by import By


class LoginPageLocators:
    SIDEBAR_HEADERS = (By.XPATH, "(//div[@class='css-901oao r-jwli3a r-1qd0xha r-1b6yd1w r-vw2c0b r-17rnw9f r-1ozfoo7 "
                                 "r-bcqeeo r-qvutc0'])[%s]")
    USERNAME_OR_EMAIL_INPUT = (By.NAME, "session[username_or_email]")
    PASSWORD_INPUT = (By.NAME, "session[password]")
    LOGIN_BUTTON = (By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")
    LOGIN_ERROR_MESSAGE_1 = (By.XPATH, "//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0' "
                                       "and contains(text(), 'Nazwa użytkownika i hasło nie zgadzają się')]")
    LOGIN_ERROR_MESSAGE_2 = (By.XPATH, "//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0' "
                                       "and contains(text(), 'Na Twoim koncie odnotowaliśmy podejrzane logowanie')]")


class LogoutPageLocators:
    LOG_OUT_POPUP = (By.XPATH, "//div[@class='css-1dbjc4n r-1awozwy r-1kihuf0 r-18u37iz r-1pi2tsx r-1777fci r-1pjcn9w "
                               "r-fxte16 r-1xcajam r-ipm5af r-9dcw1g']")
    LOG_OUT_BUTTON = (By.NAME, "//div[@data-testid='confirmationSheetConfirm']")


class HomePageLocators:
    COOKIES_USE_BAR_CLOSE_BUTTON = (By.XPATH, "//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo "
                                              "r-qvutc0' and contains(text(), 'Close')]")
    SIDEBAR_ACCOUNT_SWITCHER_BUTTON = (By.XPATH, "//div[@data-testid='SideNav_AccountSwitcher_Button']")
    ACCOUNT_SWITCHER_LOGOUT_BUTTON = (By.XPATH, "//a[@data-testid='AccountSwitcher_Logout_Button']")
    TWEET_DRAFT_INPUT = (By.XPATH, "//div[@class='notranslate public-DraftEditor-content']")
    EMOJIS_POPUP_BUTTON = (By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-1niwhzg r-42olwf r-sdzlij r-1phboty "
                                     "r-rs99b7 r-1w2pmg r-mvpalk r-1vuscfd r-53xb7h r-1ny4l3l r-mk0yit r-o7ynqc "
                                     "r-6416eg r-lrvibr r-136ojw6']")
    GRINNING_FACE_EMOJI = (By.XPATH, "//div[@aria-label='Grinning face']")
    SEND_TWEET_BUTTON = (By.XPATH, "//div[@data-testid='tweetButtonInline']")
    PROFILE_MENU_ITEM = (By.XPATH, "//a[@aria-label='Profile']")
    SEARCH_TWITTER_SEARCHBOX = (By.XPATH, "//input[@placeholder='Search Twitter']")
    FOUND_PROFILE_LABEL = (By.XPATH, "//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0' and "
                                     "contains(text(), '%s')]")


class ProfilePageLocators:
    # My Profile Page
    BOX_WITH_POSTED_TWEET = (By.XPATH, "//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0' "
                                       "and contains(text(), '%s')]")
    MORE_EXPAND_BUTTON = (By.XPATH, "//div[@data-testid='caret']")
    DELETE_TWEET_OPTION = (By.XPATH, "//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0' and "
                                     "contains(text(), 'Delete')]")
    TWEET_DELETED_CONFIRMATION_POPUP = (By.XPATH, "//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo "
                                                  "r-qvutc0' and contains(text(), 'Your Tweet was deleted')]")
    YOU_RETWEETED_LABEL = (By.XPATH, "//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0'and "
                                     "contains(text(), 'You Retweeted')]")
    UNRETWEET_EXPAND_BUTTON = (By.XPATH, "//div[@data-testid='unretweet']")
    CONFIRM_UNDO_RETWEET_BUTTON = (By.XPATH, "//div[@data-testid='unretweetConfirm']")
    NO_TWEETS_LABEL = (By.XPATH, "//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0' and "
                                 "contains(text(), 'You haven’t Tweeted yet')]")
    # Other Profile Pages
    FOLLOW_BUTTON = (By.XPATH, "(//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0' and "
                               "contains(text(), 'Follow')])[1]")
    SUGGESTED_PROFILES_LABEL = (By.XPATH, "//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo "
                                          "r-qvutc0' and contains(text(), 'Suggested')]")
    UNFOLLOW_BUTTON = (By.XPATH, "//div[@data-testid='1171755060-unfollow']")
    CONFIRM_UNFOLLOW_BUTTON = (By.XPATH, "//div[@data-testid='confirmationSheetConfirm']")
    RETWEET_EXPAND_BUTTON = (By.XPATH, "(//div[@data-testid='retweet'])[%s]")
    CONFIRM_RETWEET_BUTTON = (By.XPATH, "//div[@data-testid='retweetConfirm']")