import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()                            # создание объекта драйвера
    driver.set_window_size(2000, 1000)         # установка размеров окна по умолчанию 1000х1000
    yield driver                                           # использование драйвера
    driver.quit()

