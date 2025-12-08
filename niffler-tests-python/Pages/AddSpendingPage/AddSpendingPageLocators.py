"""
 Локаторы страницы Add new spending
"""
from selenium.webdriver.common.by import By


class AddSpendingPageLocators:
    AMOUNT_FIELD = (By.CSS_SELECTOR, "[id='amount']")
    CURRENCY_SELECT = (By.CSS_SELECTOR, "[id='currency']")
    CURRENCY_ITEM = (By.CSS_SELECTOR, ".MuiPaper-root>.MuiList-padding>li>span:nth-child(1)")
    CATEGORY_FIELD = (By.CSS_SELECTOR, "[id='category']")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "[id='description']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "[id='cancel']")
    ADD_BUTTON = (By.CSS_SELECTOR, "[id='save']")
