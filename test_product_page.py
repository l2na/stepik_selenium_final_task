import pytest

from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('url', ["?promo=offer0",
                                  "?promo=offer1",
                                  "?promo=offer2",
                                  "?promo=offer3",
                                  "?promo=offer4",
                                  "?promo=offer5",
                                  "?promo=offer6",
                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                  "?promo=offer8",
                                  "?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, url):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{url}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.solve_quiz_and_get_code()
    page.book_name_match()
    page.book_price_match()



