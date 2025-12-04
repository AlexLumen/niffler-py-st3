from selenium.webdriver.common.by import (By)


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, "[action='/login']")
    TITLE = (By.CSS_SELECTOR, ".header")
    USER_NAME_FIELD = (By.CSS_SELECTOR, "[name='username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".form__submit")
    REGISTER_URL_BUTTON = (By.CSS_SELECTOR, ".form__register")
    NEW_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[href='/register']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".form__error")
