# -*- encoding: utf-8 -*-

import datetime
import pytest
import time
import logging, logging.config, os.path
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# Изменение имени клиента

def test_changing_client_name(app):
    now = str(datetime.datetime.now())
    client_name = "866712#autotest4_" + now[:16]
    locator = "//span[contains(text(),'" + client_name + "')]"

    logging.config.fileConfig('log.conf')
    log = logging.getLogger('main')
    fh = logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/',
                                          'changing_client_name {}.log'.format(
                                              datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S'))))
    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | '"%(module)-12s"' | line %(lineno)04d | %(message)s')
    fh.setFormatter(formatter)
    log.addHandler(fh)

    log.info("changing_client_name.py is running")

    app.go_to_online_version(ov_link="https://login.consultant.ru")
    app.login_client(client_name="866712#autotest4", client_password="cDKgrqe7")
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_name(client_name)
    if (app.is_element_present_main(locator) == True):
        log.info("В ОД имя Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
    else:
        log.info("ОШИБКА: В ОД имя Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator) == True)

    app.logout_client()
    log.info("changing_client_name.py is done successfully")
