import pytest
from playwright.sync_api import expect


@pytest.mark.ui
def test_main_page(page):
    # ARRANGE
    page.goto("https://www.goodfon.ru")

    # ASSERT
    expect(page.locator("a.headline__logo__icon")).to_be_visible()