import pytest
from playwright.sync_api import expect

from tests.ui_tests.pages.goodfon_page import GoodFonPage


@pytest.mark.ui
def test_login_button(page):
    # ARRANGE
    goodfon = GoodFonPage(page)
    goodfon.open()

    # ACT
    goodfon.click_login()

    # ASSERT
    expect(page).to_have_url("https://www.goodfon.ru/auth/signin/")