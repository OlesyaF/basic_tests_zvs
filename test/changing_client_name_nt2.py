# -*- encoding: utf-8 -*-

import datetime
import logging
import logging.config
import os.path
import random
import time

import pytest

from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# Изменение имени клиента (негативный тест): нельзя сохранить имя, состоящее из одного символа

def test_changing_client_name_nt2(app):
    list = ['s', 'R', 'м', 'Б', '8', '#', '/']
    client_name = random.choice(list)
    locator1 = "//div[contains(@class, 'FormCustomerFullnameError') and contains(text(),'Введите корректное имя')]"

    print("changing_client_name_nt2.py is running")

    app.go_to_online_version(ov_link="https://login.consultant.ru")
    app.login_client(client_name="866712#autotest4", client_password="cDKgrqe7")
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_name(client_name)
    if (app.is_element_present_main(locator1) == True):
        print(
            "Нельзя сохранить имя Клиента, состоящее из одного символа (под полем 'Имя' - 'Введите корректное имя', "
            "после нажатия на 'Сохранить' остались в окне 'Изменить контактные данные') "
            "- ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: Не найдено: под полем 'Имя' - 'Заполните это поле' - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator1) == True)

    app.logout_client()
    print("changing_client_name_nt2.py is done successfully")
