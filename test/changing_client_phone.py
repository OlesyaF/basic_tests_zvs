# -*- encoding: utf-8 -*-

import datetime
import logging
import logging.config
import os.path
import time

import pytest

from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# Изменение телефона клиента

def test_changing_client_phone(app):
    phone, phone_mask = app.get_phone_as_random_set()
    locator = "//input[@value='" + phone_mask + "']"

    print("changing_client_phone.py is running")

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
    print("changing_client_phone.py is done successfully")
