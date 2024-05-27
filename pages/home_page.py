from pages.base_page import BasePage
from components.components import WebElement

class HomePage(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://localhost:5000/'
        super().__init__(driver, self.base_url)

        self.middle_text = WebElement(driver, 'body > section > div.hero-body > div > h1')
        self.btn_home = WebElement(driver, '#navbarMenuHeroA > div > a:nth-child(1)')
        self.btn_login = WebElement(driver, '#navbarMenuHeroA > div > a:nth-child(2)')
        self.btn_sing_up = WebElement(driver, '#navbarMenuHeroA > div > a:nth-child(3)')


