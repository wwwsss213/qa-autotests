import pytest
from playwright.sync_api import expect

from tests.ui_tests.pages.goodfon_page import GoodFonPage


@pytest.mark.ui
def test_search_invalid(page):
    # ARRANGE
    goodfon = GoodFonPage(page)
    goodfon.open()

    # ACT
    goodfon.search("qwertyxyz123")

    # ASSERT
    expect(goodfon.empty_search_message).to_contain_text(
        "ничего не найдено."
    )