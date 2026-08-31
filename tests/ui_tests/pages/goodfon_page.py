from playwright.sync_api import Page


class GoodFonPage:

    def __init__(self, page: Page):
        self.page = page

        self.logo = page.locator("a.headline__logo__icon")
        self.search_input = page.locator("input.js-search")
        self.search_button = page.get_by_role("button", name="Найти")
        self.wallpaper = page.locator("img.wallpapers__item__img").first
        self.login_button = page.get_by_role("link", name="войти")

    def open(self):
        self.page.goto("https://www.goodfon.ru")

    def search(self, text):
        self.search_input.fill(text)
        self.search_button.click()

    def click_login(self):
        self.login_button.click()