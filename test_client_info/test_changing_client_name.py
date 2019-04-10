# -*- encoding: utf-8 -*-

import random
import time

import allure


# Изменение имени клиента

@allure.title("Изменение имени клиента (позитивный тест)")
def test_changing_client_name(app):
    print("test_changing_client_name.py is running")

    client_name = "Autotest#" + str(app.calc_check_sum_from_date())
    print("client_name: ", client_name)
    locator = "//span[contains(text(),'" + client_name + "')]"

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_name(client_name)
    app.save_client_info()
    if (app.is_element_present_main(locator) == True):
        print("В ОД имя Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description(
            'В ОД имя Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: В ОД имя Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: В ОД имя Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_present_main(locator) == True)

    app.logout_client()
    print("test_changing_client_name.py is done successfully")


# Изменение имени клиента (негативный тест): нельзя сохранить имя незаполненным

@allure.title("Изменение имени клиента (негативный тест): нельзя сохранить имя незаполненным")
def test_changing_client_name_nt1(app):
    print("changing_client_name_nt1.py is running")

    locator1 = "//div[contains(@class, 'FormCustomerFullnameError') and contains(text(),'Заполните это поле')]"
    locator2 = "//input[@id='FormCustomerFullname'][@placeholder='Введите Ваше имя']"

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_name(client_name="")
    app.save_client_info()
    if (app.is_element_present_main(locator1) == True and app.is_element_present_main(locator2) == True):
        print(
            "Нельзя сохранить пустое имя Клиента (в поле 'Имя' отображается 'Введите Ваше имя', "
            "под полем 'Имя' - 'Заполните это поле', после нажатия на 'Сохранить' остались в окне 'Изменить контактные данные') "
            "- ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description('Нельзя сохранить пустое имя Клиента - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: Не найдено: в поле 'Имя' - 'Введите Ваше имя', под полем 'Имя' - 'Заполните это поле' "
              "- ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description('ОШИБКА: Не найдено требование заполнить поле с именем - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_present_main(locator1) == True and app.is_element_present_main(locator2) == True)

    app.logout_client()
    print("changing_client_name_nt1.py is done successfully")


# Изменение имени клиента (негативный тест): нельзя сохранить имя, состоящее из одного символа

@allure.title("Изменение имени клиента (негативный тест): нельзя сохранить имя, состоящее из одного символа")
def test_changing_client_name_nt2(app):
    print("changing_client_name_nt2.py is running")

    list = ['s', 'R', 'м', 'Б', '8', '#', '/']
    client_name = random.choice(list)
    locator = "//div[contains(@class, 'FormCustomerFullnameError') and contains(text(),'Введите корректное имя')]"

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_name(client_name)
    app.save_client_info()
    if (app.is_element_present_main(locator) == True):
        print(
            "Нельзя сохранить имя Клиента, состоящее из одного символа (под полем 'Имя' - 'Введите корректное имя', "
            "после нажатия на 'Сохранить' остались в окне 'Изменить контактные данные') "
            "- ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description('Нельзя сохранить имя Клиента, состоящее из одного символа - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: Не найдено: под полем 'Имя' - 'Введите корретное имя' - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: Не найдено требование корректно заполнить поле с именем - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_present_main(locator) == True)

    app.logout_client()
    print("changing_client_name_nt2.py is done successfully")
