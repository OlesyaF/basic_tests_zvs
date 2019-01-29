# -*- encoding: utf-8 -*-

import datetime
import logging
import logging.config
import os.path
import time

import pytest

from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# Изменение телефона клиента: можно сохранить поле 'Телефон' незаполненным

def test_changing_client_phone_null(app):
    locator = "//input[@id='FormCustomerPhone'][@placeholder='+7 (___) ___-__-__'][@value='']"

    logging.config.fileConfig('log.conf')
    log = logging.getLogger('main')
    fh = logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/',
                                          'changing_client_phone_null {}.log'.format(
                                              datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S'))))
    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | '"%(module)-12s"' | line %(lineno)04d | %(message)s')
    fh.setFormatter(formatter)
    log.addHandler(fh)

    log.info("changing_client_phone_null.py is running")

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
        log.info(
            "В окне 'Изменить контактные данные' после перевхода в поле 'Телефон' отображается "
            "пустая маска +7 (___) ___-__-__ - ТЕСТ УСПЕШНЫЙ")
    else:
        log.info("ОШИБКА: В окне 'Изменить контактные данные' после перевхода в поле 'Телефон' не отображается "
                 "пустая маска +7 (___) ___-__-__ - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator) == True and app.is_element_present_main(locator) == True)

    app.logout_client()
    log.info("changing_client_phone_null.py is done successfully")
