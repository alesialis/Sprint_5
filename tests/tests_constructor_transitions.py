from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgersLocators


class TestBurgersConstructor:
    def test_open_sauces_by_click(self, driver):
        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.SAUCES_BUTTON).click()
        assert driver.find_element(*BurgersLocators.CURRENT_OPTION).text == 'Соусы'

    def test_open_fillings_by_click(self, driver):
        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.FILLINGS_BUTTON).click()
        assert driver.find_element(*BurgersLocators.CURRENT_OPTION).text == 'Начинки'

    def test_open_buns_by_click(self, driver):
        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.FILLINGS_BUTTON).click()
        driver.find_element(*BurgersLocators.BUNS_BUTTON).click()
        assert driver.find_element(*BurgersLocators.CURRENT_OPTION).text == 'Булки'






