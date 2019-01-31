# -*- encoding: utf-8 -*-

import time


# Изменение телефона клиента

def test_changing_client_phone(app):
    phone, phone_mask = app.get_phone_as_random_set()
    locator = "//input[@value='" + phone_mask + "']"

    print("test_changing_client_phone.py is running")

    app.go_to_online_version(ov_link="https://login.consultant.ru")
    app.login_client(client_name="866712#autotest4", client_password="cDKgrqe7")
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_phone(phone)
    time.sleep(2)
    app.go_to_client_info()
    if (app.is_element_present_main(locator) == True):
        print("В окне 'Изменить контактные данные' после перевхода номер телефона совпадает с новым значением "
                 "- ТЕСТ УСПЕШНЫЙ")
    else:
        print(
            "ОШИБКА: В окне 'Изменить контактные данные' после перевхода номер телефона не совпадает с новым значением "
            "- ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator) == True)

    app.logout_client()
    print("test_changing_client_phone.py is done successfully")


# Изменение телефона клиента: можно сохранить поле 'Телефон' незаполненным

def test_changing_client_phone_null(app):
    locator = "//input[@id='FormCustomerPhone'][@placeholder='+7 (___) ___-__-__'][@value='']"

    print("changing_client_phone_null.py is running")

    app.go_to_online_version(ov_link="https://login.consultant.ru")
    app.login_client(client_name="866712#autotest4", client_password="cDKgrqe7")
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_phone("")
    time.sleep(2)
    app.go_to_client_info()
    if (app.is_element_present_main(locator) == True):
        print(
            "В окне 'Изменить контактные данные' после перевхода в поле 'Телефон' отображается "
            "пустая маска +7 (___) ___-__-__ - ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: В окне 'Изменить контактные данные' после перевхода в поле 'Телефон' не отображается "
                 "пустая маска +7 (___) ___-__-__ - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator) == True and app.is_element_present_main(locator) == True)

    app.logout_client()
    print("changing_client_phone_null.py is done successfully")