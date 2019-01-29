# -*- encoding: utf-8 -*-

import datetime
import pytest
import time
import logging, logging.config, os.path
from application import Application
import random


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# Изменение email клиента (негативный тест): нельзя сохранить email, не соответствующий формату '%@%.%'

def test_changing_client_email_nt2(app):

    locator1 = "//div[contains(@class, 'FormCustomerEmailError') and contains(text(),'Введите корректный email')]"

    logging.config.fileConfig('log.conf')
    log = logging.getLogger('main')
    fh = logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/',
                                          'changing_client_email_nt2 {}.log'.format(
                                              datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S'))))
    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | '"%(module)-12s"' | line %(lineno)04d | %(message)s')
    fh.setFormatter(formatter)
    log.addHandler(fh)

    log.info("changing_client_email_nt2.py is running")

    app.go_to_online_version(ov_link="https://login.consultant.ru")
    app.login_client(client_name="866712#autotest4", client_password="cDKgrqe7")
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    list = ['sss@sss.','@sss.com','sss@.com','ssssss.com','sss@ssscom','яяя@sss.com','sss@sss.яяя']
    app.changing_client_email(email= random.choice(list))
    if (app.is_element_present_main(locator1) == True):
        log.info(
            "Нельзя сохранить email, не соответствующий формату '%@%.%' (под полем 'Email' - 'Введите корректный email', "
            "после нажатия на 'Сохранить' остались в окне 'Изменить контактные данные') "
            "- ТЕСТ УСПЕШНЫЙ")
    else:
        log.info("ОШИБКА: Не найдено: под полем 'Email' - 'Введите корректный email' - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator1) == True)

    app.logout_client()
    log.info("changing_client_email_nt2.py is done successfully")
