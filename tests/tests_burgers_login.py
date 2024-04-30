from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgersLocators


class TestBurgersLogin:

    def test_login_by_login_button_on_main_page(self, driver, registration):
        test_email = registration[0]
        test_password = registration[1]

        driver.get(f'{URL}')
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))
        driver.find_element(*BurgersLocators.LOGIN_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))
        driver.find_element(*BurgersLocators.LOGIN_EMAIL_FIELD).send_keys(test_email)
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(test_password)
        driver.find_element(*BurgersLocators.LOGIN_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "button_button__33qZ0"), "Оформить заказ"))
        driver.quit()

    def test_login_by_my_profile_button_on_main_page(self, driver, registration):
        test_email = registration[0]
        test_password = registration[1]
        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.MY_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))

        driver.find_element(*BurgersLocators.LOGIN_EMAIL_FIELD).send_keys(test_email)
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(test_password)
        driver.find_element(*BurgersLocators.LOGIN_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "button_button__33qZ0"), "Оформить заказ"))
        driver.quit()

    def test_login_by_login_button_on_register_page(self, driver, registration):
        test_email = registration[0]
        test_password = registration[1]
        driver.get(f'{URL}register')
        driver.find_element(*BurgersLocators.LOGIN_BUTTON_ON_REG_PAGE).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))

        driver.find_element(*BurgersLocators.LOGIN_EMAIL_FIELD).send_keys(test_email)
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(test_password)
        driver.find_element(*BurgersLocators.LOGIN_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "button_button__33qZ0"), "Оформить заказ"))
        driver.quit()

    def test_login_by_login_button_on_restore_page(self, driver, registration):
        test_email = registration[0]
        test_password = registration[1]
        driver.get(f'{URL}forgot-password')
        driver.find_element(*BurgersLocators.LOGIN_BUTTON_ON_RESTORE_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))
        driver.find_element(*BurgersLocators.LOGIN_EMAIL_FIELD).send_keys(test_email)
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(test_password)
        driver.find_element(*BurgersLocators.LOGIN_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "button_button__33qZ0"), "Оформить заказ"))
        driver.quit()


