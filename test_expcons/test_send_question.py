# -*- encoding: utf-8 -*-

import time
import allure


# Проверка отправка Клиентом вопроса эксперту

@allure.title("Проверка отправка Клиентом вопроса эксперту")
def test_send_question(app):
    print("test_view_hotline_info.py is running")

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    client_name = app.get_client_name()
    client_email = app.get_client_email()
    client_phone = app.get_client_phone()
    if client_phone == "":
        phone, phone_mask = app.get_phone_as_random_set()
        locator = "//input[@value='" + phone_mask + "']"
        app.changing_client_phone(phone)
        app.save_client_info()
        time.sleep(2)
        app.go_to_client_info()
        if (app.is_element_present_main(locator) == True):
            print("В окне 'Изменить контактные данные' после перевхода номер телефона совпадает с новым значением")
            allure.dynamic.description('Номер телефона совпадает с новым значением')
            client_phone = app.get_client_phone()
        else:
            print(
                "ОШИБКА: В окне 'Изменить контактные данные' после перевхода номер телефона не совпадает с новым значением!!!")
            allure.dynamic.description('ОШИБКА: номер телефона не совпадает с новым значением!!!')
            assert (app.is_element_present_main(locator) == True)
    time.sleep(2)
    app.go_to_expcons()
    question_client = str(app.calc_check_sum_from_date()) + "#question"
    print("question_client: ", question_client)
    app.client_send_question(question_client)
    app.check_expcons_after_question(question_client, client_name, client_email, client_phone)
    app.logout_client()
    print("test_view_hotline_info.py is done successfully")
