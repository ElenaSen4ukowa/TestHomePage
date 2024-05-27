import time
from pages.home_page import HomePage
from pages.sign_up_page import SidnUpPage
from pages.login_page import LoginPage


def test_sign_up_empty(browser):
    test_home_page = HomePage(browser)
    sign_up_page = SidnUpPage(browser)
    login_page = LoginPage(browser)

    test_home_page.visit()

    time.sleep(3)
    test_home_page.btn_sing_up.click()
    time.sleep(3)
    assert sign_up_page.equal_url()

    sign_up_page.sing_up_btn.click()
    time.sleep(3)

    assert not login_page.equal_url()

