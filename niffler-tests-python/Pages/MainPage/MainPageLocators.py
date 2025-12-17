"""
Локаторы главной страницы
"""
from selenium.webdriver.common.by import By


class MainPageLocators:

    SPENDING = (By.CSS_SELECTOR, "[id='spendings']")