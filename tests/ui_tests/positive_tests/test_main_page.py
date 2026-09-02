import pytest
from playwright.sync_api import expect

from tests.ui_tests.pages.goodfon_page import GoodFonPage


@pytest.mark.ui
def test_main_page(page):
    # ARRANGE
    goodfon = GoodFonPage(page)
    goodfon.open()

    # ASSERT
    expect(goodfon.logo).to_be_visible()