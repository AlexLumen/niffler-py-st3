from selenium.webdriver.common.by import By

"""
   Локаторы элемента Меню
"""


class NavbarElementLocators:
    SIGN_OUT_BUTTON = (By.XPATH, "//li[contains(text(), 'Sign out')]")
