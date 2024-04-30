from selenium.webdriver.common.by import By


class BurgersLocators:
    # поле "Имя" на странице регистрации
    NAME_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    # поле "Почта" на странице регистрации
    EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
    # поле "Пароль" на странице регистрации
    PASSWORD_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input")
    # кнопка "Зарегистрироваться" на странице регистрации
    REGISTER_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/form/button")

    # кнопка "Войти в аккаунт" на главной /И "Войти" на форме входа
    LOGIN_PROFILE_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")

    # поле "Почта" на странице входа
    LOGIN_EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    # поле "Пароль" на странице входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")

    # кнопка "Личный кабинет" на главной
    MY_PROFILE_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")

    # кнопка "Войти" на странице регистрации
    LOGIN_BUTTON_ON_REG_PAGE = (By.XPATH, "//*[@id='root']/div/main/div/div/p/a")

    # кнопка "Войти" на странице восстановления пароля
    LOGIN_BUTTON_ON_RESTORE_PAGE = (By.XPATH, "//*[@id='root']/div/main/div/div/p/a")

    # кнопка "Выйти" на странице личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button")
    # кнопка "Конструктор" на странице личного кабинета
    CONSTRUCTOR_BUTTON_ON_PROFILE_PAGE = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a")
    # лого на странице личного кабинета
    LOGO_ON_PROFILE_PAGE = (By.XPATH, "//*[@id='root']/div/header/nav/div/a")

    # кнопка "Соусы" на странице конструктора/главной
    SAUCES_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]/span")
    # кнопка "Начинки" на странице конструктора/главной
    FILLINGS_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span")
    # кнопка "Булки" на странице конструктора/главной
    BUNS_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]/span")