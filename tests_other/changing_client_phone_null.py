# -*- encoding: utf-8 -*-

import time


# Изменение телефона клиента: можно сохранить поле 'Телефон' незаполненным

def test_changing_client_phone_null(app):
    locator = "//input[@id='FormCustomerPhone'][@placeholder='+7 (___) ___-__-__'][@value='']"

    print("changing_client_phone_null.py is running")

    app.go_to_online_version(ov_link="https://login.consultant.ru")
    app.login_client(client_name="866712#autotest4", client_password="cDKgrqe7")
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(3)
    app.changing_client_phone("")
    time.sleep(3)
    app.go_out_online_dialog()
    time.sleep(3)
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(3)
    if (app.is_element_present_main(locator) == True):
        print(
            "В окне 'Изменить контактные данные' после перевхода в поле 'Телефон' отображается "
            "пустая маска +7 (___) ___-__-__ - ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: В окне 'Изменить контактные данные' после перевхода в поле 'Телефон' не отображается "
                 "пустая маска +7 (___) ___-__-__ - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator) == True)

    app.logout_client()
    print("changing_client_phone_null.py is done successfully")
