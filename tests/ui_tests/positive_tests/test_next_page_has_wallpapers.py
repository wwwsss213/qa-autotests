import pytest
from playwright.sync_api import expect

from tests.ui_tests.pages.goodfon_page import GoodFonPage


@pytest.mark.ui
def test_next_page_has_wallpapers(page):
    # ARRANGE
    goodfon = GoodFonPage(page)
    goodfon.open()

    # ACT
    goodfon.click_next_page()

    # ASSERT
    expect(goodfon.wallpapers.first).to_be_visible()