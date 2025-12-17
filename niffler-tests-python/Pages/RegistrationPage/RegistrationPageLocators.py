from selenium.webdriver.common.by import By


class RegistrationPageLocators:

    REGISTRATION_FORM = (By.CSS_SELECTOR, "[id='register-form']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "[id='username']")
    USERNAME_INPUT_ERROR_MESSAGE = (By.XPATH, "//label[contains(text(), 'Username')]/span")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[id='password']")
    PASSWORD_INPUT_ERROR_MESSAGE = (By.XPATH, "//label[contains(text(), 'Password')]/span")
    SUBMIT_PASSWORD_INPUT = (By.CSS_SELECTOR, "[id='passwordSubmit']")
    SUBMIT_PASSWORD_INPUT_ERROR_MESSAGE = (By.XPATH, "//label[contains(text(), 'Submit password')]/span")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    SUCCESS_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, ".form__paragraph_success")
    LOGIN_URL = (By.LINK_TEXT, "Log in!")
    SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign in")
