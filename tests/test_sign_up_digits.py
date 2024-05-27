import time
from pages.home_page import HomePage
from pages.sign_up_page import SidnUpPage
from pages.login_page import LoginPage


def test_digits_without_dot_com(browser):
    test_home_page = HomePage(browser)
    sign_up_page = SidnUpPage(browser)
    login_page = LoginPage(browser)

    test_home_page.visit()

    time.sleep(3)
    test_home_page.btn_sing_up.click()
    time.sleep(3)
    assert sign_up_page.equal_url()

    sign_up_page.email_field.send_keys('1@111')

    sign_up_page.sing_up_btn.click()
    time.sleep(3)

    assert not login_page.equal_url()

def test_digits_with_dot_digits(browser):
    test_home_page = HomePage(browser)
    sign_up_page = SidnUpPage(browser)
    login_page = LoginPage(browser)

    test_home_page.visit()

    time.sleep(3)
    test_home_page.btn_sing_up.click()
    time.sleep(3)
    assert sign_up_page.equal_url()

    sign_up_page.email_field.send_keys('9@111.11')

    sign_up_page.password_field.send_keys('8')

    sign_up_page.sing_up_btn.click()
    time.sleep(3)

    assert not login_page.equal_url()

def test_digits_with_dot_rus(browser):
    test_home_page = HomePage(browser)
    sign_up_page = SidnUpPage(browser)
    login_page = LoginPage(browser)

    test_home_page.visit()

    time.sleep(3)
    test_home_page.btn_sing_up.click()
    time.sleep(3)
    assert sign_up_page.equal_url()

    sign_up_page.email_field.send_keys('9@маил.ру')

    sign_up_page.password_field.send_keys('5')

    sign_up_page.sing_up_btn.click()
    time.sleep(3)

    assert not login_page.equal_url()

