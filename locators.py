from selenium.webdriver.common.by import By


class BurgersLocators:
    # поле "Имя" на странице регистрации
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/../input")
    # поле "Почта" на странице регистрации
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/../input")
    # поле "Пароль" на странице регистрации
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/../input")
    # кнопка "Зарегистрироваться" на странице регистрации
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    # текст ошибки "Некорректный пароль" при регистрации
    INCORRECT_PASSWORD = (By.XPATH, ".//p[contains(@class, 'input__error text') and text()='Некорректный пароль']")

    # кнопка "Войти в аккаунт" на главной /И "Войти" на форме входа
    LOGIN_PROFILE_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")

    # поле "Почта" на странице входа
    LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@name = 'name']")
    # поле "Пароль" на странице входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name = 'Пароль']")

    # кнопка "Личный кабинет" на главной
    MY_PROFILE_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")

    # кнопка "Войти" на странице регистрации
    LOGIN_BUTTON_ON_REG_PAGE = (By.CLASS_NAME, "Auth_link__1fOlj")

    # кнопка "Войти" на странице восстановления пароля
    LOGIN_BUTTON_ON_RESTORE_PAGE = (By.CLASS_NAME, "Auth_link__1fOlj")

    # кнопка "Выход" на странице личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    # кнопка "Конструктор" на странице личного кабинета
    CONSTRUCTOR_BUTTON_ON_PROFILE_PAGE = (By.XPATH, "//li/a[@href = '/']")
    # лого на странице личного кабинета
    LOGO_ON_PROFILE_PAGE = (By.XPATH, "//div/a[@href = '/']")

    # кнопка "Соусы" на странице конструктора/главной
    SAUCES_BUTTON = (By.XPATH, "//span[text() = 'Соусы']")
    # кнопка "Начинки" на странице конструктора/главной
    FILLINGS_BUTTON = (By.XPATH, "//span[text() = 'Начинки']")
    # кнопка "Булки" на странице конструктора/главной
    BUNS_BUTTON = (By.XPATH, "//span[text() = 'Булки']")
    # кнопка "Оформить заказ" на странице конструктора/главной
    BUTTON_ORDER = (By.XPATH, ".//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']")
    # текущая опция в разделе ингредиентов в конструкторе
    CURRENT_OPTION = (By.XPATH, "//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")