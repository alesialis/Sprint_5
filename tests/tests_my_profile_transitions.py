from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgersLocators


class TestBurgersMyProfile:

    def test_open_profile_by_profile_button(self, driver, registration):
        test_email = registration[0]
        test_password = registration[1]

        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.MY_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))

        driver.find_element(*BurgersLocators.LOGIN_EMAIL_FIELD).send_keys(test_email)
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(test_password)
        driver.find_element(*BurgersLocators.LOGIN_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "button_button__33qZ0"), "Оформить заказ"))
        before_click_url = driver.current_url

        driver.find_element(*BurgersLocators.MY_PROFILE_BUTTON).click()
        after_click_url = driver.current_url

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_button__14Yp3")))
        assert after_click_url != before_click_url
        driver.quit()

    def test_open_constructor_by_constructor_button(self, driver, registration):
        test_email = registration[0]
        test_password = registration[1]

        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.MY_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))

        driver.find_element(*BurgersLocators.LOGIN_EMAIL_FIELD).send_keys(test_email)
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(test_password)
        driver.find_element(*BurgersLocators.LOGIN_PROFILE_BUTTON).click()

        driver.find_element(*BurgersLocators.CONSTRUCTOR_BUTTON_ON_PROFILE_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))
        driver.quit()

    def test_open_constructor_by_logo_click(self, driver, registration):
        test_email = registration[0]
        test_password = registration[1]

        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.MY_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))

        driver.find_element(*BurgersLocators.LOGIN_EMAIL_FIELD).send_keys(test_email)
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(test_password)
        driver.find_element(*BurgersLocators.LOGIN_PROFILE_BUTTON).click()

        driver.find_element(*BurgersLocators.LOGO_ON_PROFILE_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))
        driver.quit()

    def test_logout_by_logout_button_on_profile_page(self, driver, registration):
        test_email = registration[0]
        test_password = registration[1]

        driver.get(f'{URL}')
        driver.find_element(*BurgersLocators.MY_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button_button__33qZ0")))

        driver.find_element(*BurgersLocators.LOGIN_EMAIL_FIELD).send_keys(test_email)
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(test_password)
        driver.find_element(*BurgersLocators.LOGIN_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "button_button__33qZ0"), "Оформить заказ"))
        driver.find_element(*BurgersLocators.MY_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "Account_button__14Yp3"), "Выход"))
        driver.find_element(*BurgersLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "button_button__33qZ0"), "Войти"))
        driver.quit()
