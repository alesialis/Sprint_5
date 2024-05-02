﻿# Sprint_5
tests_burgers_registration содержит два теста на проверку регистрации:
1- регистрация успешна - test_sign_up_successful
2- регистрация неуспешна - test_sign_up_unsuccessful

tests_burgers_login содержит четыре теста на проверку входа в аккаунт:
3- вход через кнопку "Войти в аккаунт" на главной - test_login_by_login_button_on_main_page
4- вход через кнопку "Личный кабинет" - test_login_by_my_profile_button_on_main_page
5- вход через кнопку в форме регистрации - test_login_by_login_button_on_register_page
6- вход через кнопку в форме восстановления пароля - test_login_by_login_button_on_restore_page

tests_my_profile_transitions содержит четыре теста на проверку переходов, связанных с личным кабинетом:
7- переход по клику на "Личный кабинет" в личный кабинет - test_open_profile_by_profile_button
8- переход в конструктор по клику на "Конструктор" - test_open_constructor_by_constructor_button
9- переход в конструктор по клику на логотип - test_open_constructor_by_logo_click
10- выход по кнопке "Выйти" в личном кабинете - test_logout_by_logout_button_on_profile_page

tests_constructor_transitions содержит три теста на проверху переходов к разделам состава бургера:
11- переход к соусам - test_open_sauces_by_click
12- переход к начинкам - test_open_fillings_by_click
13- переход к булочкам - test_open_buns_by_click
