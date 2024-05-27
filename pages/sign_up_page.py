from pages.base_page import BasePage
from components.components import WebElement

class SidnUpPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://localhost:5000/signup'
        super().__init__(driver, self.base_url)

        self.email_field = WebElement(driver, 'div.control > input[name="email"]')
        self.name_field = WebElement(driver, 'div.control > input[name="name"]')
        self.password_field = WebElement(driver, 'div.control > input[name="password"]')
        self.sing_up_btn = WebElement(driver, 'body > section > div.hero-body > div > div > div > form > button')

