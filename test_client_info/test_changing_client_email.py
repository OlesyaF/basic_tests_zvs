# -*- encoding: utf-8 -*-

import random
import time
import pytest
import allure


# Изменение email клиента

# Изменение email клиента (позитивный тест)

@allure.title("Изменение email клиента (позитивный тест)")
def test_changing_client_email(app):
    print("test_changing_client_email.py is running")

    email = str(app.calc_check_sum_from_date()) + "@autotest.ru"
    print("email: ", email)
    locator = "//span[contains(text(),'" + email + "')]"

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_email(email)
    app.save_client_info()
    if (app.is_element_present_main(locator) == True):
        print("В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description(
            'В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_present_main(locator) == True)

    app.logout_client()
    print("test_changing_client_email.py is done successfully")


# Изменение email клиента (негативный тест): нельзя сохранить поле 'Email' незаполненным

@allure.title("Изменение email клиента (негативный тест): нельзя сохранить поле 'Email' незаполненным")
def test_changing_client_email_nt1(app):
    print("changing_client_email_nt1.py is running")

    locator1 = "//div[contains(@class, 'FormCustomerEmailError') and contains(text(),'Заполните это поле')]"
    locator2 = "//input[@id='FormCustomerEmail'][@placeholder='Введите Ваш email']"

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_email(email="")
    app.save_client_info()
    if (app.is_element_present_main(locator1) == True and app.is_element_present_main(locator2) == True):
        print(
            "Нельзя сохранить пустой email Клиента (в поле 'Email' отображается 'Введите Ваш email', "
            "под полем 'Email' - 'Заполните это поле', после нажатия на 'Сохранить' остались в окне 'Изменить контактные данные') "
            "- ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description('Нельзя сохранить пустой email Клиента - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: Не найдено: в поле 'Email' - 'Введите Ваш email', под полем 'Email' - 'Заполните это поле' "
              "- ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: Не найдено: в поле "Email" - "Введите Ваш email", под полем "Email" - "Заполните это поле" - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_present_main(locator1) == True and app.is_element_present_main(locator2) == True)

    app.logout_client()
    print("changing_client_email_nt1.py is done successfully")


# Изменение email клиента (негативный тест): нельзя сохранить email, не соответствующий формату '%@%.%'

@allure.title("Изменение email клиента (негативный тест): нельзя сохранить email, не соответствующий формату '%@%.%'")
def test_changing_client_email_nt2(app):
    print("changing_client_email_nt2.py is running")

    locator1 = "//div[contains(@class, 'FormCustomerEmailError') and contains(text(),'Введите корректный email')]"

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    list = ['sss@sss.', '@sss.com', 'sss@.com', 'ssssss.com', 'sss@ssscom', 'яяя@sss.com', 'sss@sss.яяя']
    app.changing_client_email(email=random.choice(list))
    app.save_client_info()
    if (app.is_element_present_main(locator1) == True):
        print(
            "Нельзя сохранить email, не соответствующий формату '%@%.%' (под полем 'Email' - 'Введите корректный email', "
            "после нажатия на 'Сохранить' остались в окне 'Изменить контактные данные') "
            "- ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description('Нельзя сохранить email, не соответствующий формату "%@%.%" - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: Не найдено: под полем 'Email' - 'Введите корректный email' - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: Не найдено: под полем "Email" - "Введите корректный email" - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_present_main(locator1) == True)

    app.logout_client()
    print("changing_client_email_nt2.py is done successfully")


# Изменение email клиента: при вставке email из буфера обмена табуляция и пробелы автоматически удаляются

@allure.title("Изменение email клиента: при вставке email из буфера обмена табуляция и пробелы автоматически удаляются")
@pytest.mark.skip(reason='This test is skipped')
def test_changing_client_email_cut_tab(app):
    print("test_changing_client_email_cut_tab.py is running")

    email = str(app.calc_check_sum_from_date()) + "@autotest.ru"
    email_tab = "   " + str(app.calc_check_sum_from_date()) + "@autotest.ru" + "  "
    print("email: ", email)
    print("email_tab: ", email_tab)
    locator = "//span[contains(text(),'" + email + "')]"

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_email(email)
    app.save_client_info()
    if (app.is_element_present_main(locator) == True):
        print("В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description(
            'В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_present_main(locator) == True)

    app.logout_client()
    print("test_changing_client_email_cut_tab.py is done successfully")