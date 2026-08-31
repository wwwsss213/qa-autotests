import pytest
from playwright.sync_api import expect


@pytest.mark.ui
def test_login_button(page):
    # ARRANGE
    page.goto("https://www.goodfon.ru")

    # ACT
    page.get_by_role("link", name="войти").click()

    # ASSERT
    expect(page).to_have_url("https://www.goodfon.ru/auth/signin/")