import time
from pages.home_page import HomePage

def test_check_middle_text(browser):
    test_home_page = HomePage(browser)
    test_home_page.visit()
    browser.set_window_size(2000, 1000)
    time.sleep(3)
    test_home_page.btn_home.click()
    time.sleep(3)
    assert test_home_page.equal_url()
    assert test_home_page.middle_text.exist()
    assert test_home_page.middle_text.get_text() == 'Test home page'
    browser.set_window_size(1000, 1000)
