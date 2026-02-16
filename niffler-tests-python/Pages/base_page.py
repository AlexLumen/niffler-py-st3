

class BasePage:
    def __init__(self, page):
        self.browser = page

    def open_url(self, url):
        self.browser.goto(url)
