# -*- encoding: utf-8 -*-

import time
import allure


# Одновременное изменение всех контактных данных Клиента

@allure.title("Одновременное изменение всех контактных данных Клиента (позитивный тест)")
def test_changing_client_info(app):
    print("test_changing_client_info.py is running")

    client_name = str(app.calc_check_sum_from_date()) + "#autotest"
    print("client_name: ", client_name)
    locator1 = "//span[contains(text(),'" + client_name + "')]"

    email = str(app.calc_check_sum_from_date()) + "@autotest.ru"
    print("email: ", email)
    locator2 = "//span[contains(text(),'" + email + "')]"

    phone, phone_mask = app.get_phone_as_random_set()
    locator3 = "//input[@value='" + phone_mask + "']"

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_name(client_name)
    app.changing_client_email(email)
    app.changing_client_phone(phone)
    app.save_client_info()
    time.sleep(2)

    if (app.is_element_present_main(locator1) == True):
        print("В ОД имя Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description(
            'В ОД имя Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: В ОД имя Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: В ОД имя Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!')
    assert (app.is_element_present_main(locator1) == True)

    if (app.is_element_present_main(locator2) == True):
        print("В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description(
            'В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!')
    assert (app.is_element_present_main(locator2) == True)

    app.go_to_client_info()

    if (app.is_element_present_main(locator3) == True):
        print("В окне 'Изменить контактные данные' после перевхода номер телефона совпадает с новым значением "
              "- ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description('Номер телефона совпадает с новым значением - ТЕСТ УСПЕШНЫЙ')
    else:
        print(
            "ОШИБКА: В окне 'Изменить контактные данные' после перевхода номер телефона не совпадает с новым значением "
            "- ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description('ОШИБКА: номер телефона не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!')
    assert (app.is_element_present_main(locator3) == True)
    allure.dynamic.description('Имя, email и телефон Клиента изменены - ТЕСТ УСПЕШНЫЙ')

    app.logout_client()
    print("test_changing_client_info.py is done successfully")