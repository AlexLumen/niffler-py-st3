"""
Локаторы главной страницы
"""
from selenium.webdriver.common.by import By


class MainPageLocators:

    SPENDING = (By.CSS_SELECTOR, "[id='spendings']")
    NO_SPENDING_TEXT = (By.XPATH, "//p[contains(text(), 'There are no spendings')]")
    CATEGORY_NAME = (By.CSS_SELECTOR, ".MuiTableRow-root>.MuiTableCell-root:nth-child(2)>span")
    CATEGORY_NAME_SELL = (By.CSS_SELECTOR, ".MuiTableRow-root>.MuiTableCell-root:nth-child(2")
    AMOUNT_VALUE = (By.CSS_SELECTOR, '.MuiTableRow-root>.MuiTableCell-root:nth-child(3)>span')
    DESCRIPTION_VALUE = (By.CSS_SELECTOR, '.MuiTableRow-root>.MuiTableCell-root:nth-child(4)>span')
