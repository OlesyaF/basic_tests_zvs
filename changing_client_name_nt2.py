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


# Изменение имени клиента (негативный тест): нельзя сохранить имя, состоящее из одного символа

def test_changing_client_name_nt1(app):
    locator1 = "//div[contains(@class, 'FormCustomerFullnameError') and contains(text(),'Введите корректное имя')]"

    logging.config.fileConfig('log.conf')
    log = logging.getLogger('main')
    fh = logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/',
                                          'changing_client_name_nt2 {}.log'.format(
                                              datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S'))))
    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | '"%(module)-12s"' | line %(lineno)04d | %(message)s')
    fh.setFormatter(formatter)
    log.addHandler(fh)

    log.info("changing_client_name_nt2.py is running")

    app.go_to_online_version(ov_link="https://login.consultant.ru")
    app.login_client(client_name="866712#autotest4", client_password="cDKgrqe7")
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    list = ['s','R','м','Б','8','#','/']
    app.changing_client_name(client_name = random.choice(list))
    if (app.is_element_present_main(locator1) == True):
        log.info(
            "Нельзя сохранить имя Клиента из одного символа (под полем 'Имя' - 'Заполните это поле', "
            "после нажатия на 'Сохранить' остались в окне 'Изменить контактные данные') "
            "- ТЕСТ УСПЕШНЫЙ")
    else:
        log.info("ОШИБКА: Не найдено: под полем 'Имя' - 'Заполните это поле' - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator1) == True)

    app.logout_client()
    log.info("changing_client_name_nt2.py is done successfully")
