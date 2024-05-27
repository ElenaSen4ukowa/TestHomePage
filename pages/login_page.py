from pages.base_page import BasePage
from components.components import WebElement

class LoginPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://localhost:5000/login'
        super().__init__(driver, self.base_url)

        self.login_form = WebElement(driver, 'body > section > div.hero-body > div > div')
        self.your_email = WebElement(driver, 'div.control > input[name="email"]')
        self.your_password = WebElement(driver, 'div.control > input[name="password"]')
        self.btn_login = WebElement(driver, 'body > section > div.hero-body > div > div > div > form > button')
        self.checkbox_remember = WebElement(driver, 'form > div:nth-child(3) > label > input[type=checkbox]')

