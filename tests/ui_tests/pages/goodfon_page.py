from playwright.sync_api import Page


class GoodFonPage:

    def __init__(self, page: Page):
        self.page = page

        # Основные элементы
        self.logo = page.locator("a.headline__logo__icon")
        self.search_input = page.locator("input.js-search")
        self.search_button = page.get_by_role("button", name="Найти")

        # Обои
        self.wallpaper = page.locator("img.wallpapers__item__img").first
        self.wallpapers = page.locator("img.wallpapers__item__img")

        # Авторизация
        self.login_button = page.get_by_role("link", name="войти")
        self.forgot_password_link = page.get_by_role(
            "link", name="Вспомнить пароль"
        )

        # Восстановление пароля
        self.recovery_email_input = page.get_by_placeholder(
            "Электронная почта для восстановления пароля"
        )

        # Поиск
        self.empty_search_message = page.locator("div.margin_top20.text")

        # Пагинация
        self.next_page_link = page.get_by_role("link", name="Cледующая")

    def open(self):
        self.page.goto("https://www.goodfon.ru")

    def search(self, text):
        self.search_input.fill(text)
        self.search_button.click()

    def click_login(self):
        self.login_button.click()

    def click_forgot_password(self):
        self.forgot_password_link.click()

    def click_next_page(self):
        self.next_page_link.click()