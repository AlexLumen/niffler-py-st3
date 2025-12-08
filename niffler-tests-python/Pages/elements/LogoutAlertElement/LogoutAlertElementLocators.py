"""
    Локаторы окна подтверждения логаута
"""
from selenium.webdriver.common.by import By


class LogoutAlertElementLocators:

    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Log out')]")
