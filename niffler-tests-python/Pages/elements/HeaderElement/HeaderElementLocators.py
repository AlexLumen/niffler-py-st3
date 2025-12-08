"""
    Локаторы элемента Header
"""

from selenium.webdriver.common.by import By


class HeaderElementLocators:
    PERSON_ICON = (By.CSS_SELECTOR, "[data-testid='PersonIcon']")
    ADD_SPENDING_BUTTON = (By.CSS_SELECTOR, "[href='/spending']")