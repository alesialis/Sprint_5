from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgersLocators
from helpers import get_sign_up_data


class TestBurgersRegistration:

    def test_sign_up_successful(self, driver):
        driver.get(f'{URL}register')
        name_data, email_data, password_data = get_sign_up_data()

        name = driver.find_element(*BurgersLocators.NAME_FIELD)
        name.send_keys(name_data)
        email = driver.find_element(*BurgersLocators.EMAIL_FIELD)
        email.send_keys(email_data)
        password = driver.find_element(*BurgersLocators.PASSWORD_FIELD)
        password.send_keys(password_data)
        driver.find_element(*BurgersLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(BurgersLocators.LOGIN_PROFILE_BUTTON, "Войти"))
        assert driver.find_element(*BurgersLocators.LOGIN_PROFILE_BUTTON).text == 'Войти'

    def test_sign_up_unsuccessful(self, driver):
        driver.get(f'{URL}register')
        name_data, email_data, password_data = get_sign_up_data()
        password_incorrect_data = password_data[:5]

        name = driver.find_element(*BurgersLocators.NAME_FIELD)
        name.send_keys(name_data)
        email = driver.find_element(*BurgersLocators.EMAIL_FIELD)
        email.send_keys(email_data)
        password_incorrect = driver.find_element(*BurgersLocators.PASSWORD_FIELD)
        password_incorrect.send_keys(password_incorrect_data)
        driver.find_element(*BurgersLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgersLocators.INCORRECT_PASSWORD))
        assert driver.find_element(*BurgersLocators.INCORRECT_PASSWORD).text == 'Некорректный пароль'






