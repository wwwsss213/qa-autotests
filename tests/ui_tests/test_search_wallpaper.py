import pytest
from playwright.sync_api import expect


@pytest.mark.ui
def test_search_wallpaper(page):
    # ARRANGE
    page.goto("https://www.goodfon.ru")

    # ACT
    page.locator("input.js-search").fill("машина")
    page.get_by_role("button", name="Найти").click()

    # ASSERT
    expect(
        page.locator("img.wallpapers__item__img").first
    ).to_be_visible()