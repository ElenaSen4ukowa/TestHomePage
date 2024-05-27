import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

def test_remember(browser):
    test_home_page = HomePage(browser)
    login_page = LoginPage(browser)
    profile_page = ProfilePage(browser)
    test_home_page.visit()
    time.sleep(3)
    test_home_page.btn_login.click()
    time.sleep(3)

    assert login_page.equal_url()
    assert login_page.login_form.exist()

    login_page.your_email.send_keys('test@mail.com')
    login_page.your_password.send_keys('12345678')
    login_page.checkbox_remember.click_force()
    time.sleep(3)
    login_page.btn_login.click()
    time.sleep(3)

    assert profile_page.equal_url()
    time.sleep(3)
    assert profile_page.centered_text.get_text() == 'Welcome, Helena!'
    time.sleep(3)
    profile_page.btn_logout.click()
    time.sleep(3)
    assert test_home_page.equal_url()
    assert test_home_page.middle_text.get_text() == 'Test home page'

    test_home_page.btn_login.click()
    time.sleep(3)

    assert login_page.your_email.get_text() == 'test@mail.com'

