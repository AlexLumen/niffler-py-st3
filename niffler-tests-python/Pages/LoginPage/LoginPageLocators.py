from playwright.sync_api import Page


class LoginPageLocators:
    def __init__(self, page: Page) -> None:
        self.page = page

    # def __init__(self, page: Page):
    #     self.page = page

    login_page = page.locator("[action='/login']")
    self.title = page.locator(".header")
    self.user_name_field = page.locator("[name='username']")
    self.password_field = page.locator("[name='password']")
    self.login_button = page.locator(".form__submit")
    self.registration_url_button = page.locator(".form__register")
    self.new_account_button = page.locator("[href='/register']")
    self.error_message = page.locator(".form__error")
