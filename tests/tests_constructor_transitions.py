from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgersLocators


class TestBurgersConstructor:
    def test_open_sauces_by_click(self, driver):
        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//img[@alt='Соус Spicy-X']")))
        driver.quit()

    def test_open_fillings_by_click(self, driver):
        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']")))
        driver.quit()

    def test_open_buns_by_click(self, driver):
        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']")))
        driver.find_element(*BurgersLocators.BUNS_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")))
        driver.quit()






