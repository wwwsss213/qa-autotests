import pytest
from playwright.sync_api import expect

from tests.ui_tests.pages.goodfon_page import GoodFonPage


@pytest.mark.ui
def test_forgot_password_email_field(page):
    # ARRANGE
    goodfon = GoodFonPage(page)
    goodfon.open()

    # ACT
    goodfon.click_login()
    goodfon.click_forgot_password()

    # ASSERT
    expect(goodfon.recovery_email_input).to_be_visible()