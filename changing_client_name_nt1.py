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


# Изменение имени клиента (негативный тест): нельзя сохранить имя незаполненным

def test_changing_client_name_nt1(app):
    locator1 = "//div[contains(@class, 'FormCustomerFullnameError') and contains(text(),'Заполните это поле')]"
    locator2 = "//input[@id='FormCustomerFullname'][@placeholder='Введите Ваше имя']"

    logging.config.fileConfig('log.conf')
    log = logging.getLogger('main')
    fh = logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/',
                                          'changing_client_name_nt1 {}.log'.format(
                                              datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S'))))
    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | '"%(module)-12s"' | line %(lineno)04d | %(message)s')
    fh.setFormatter(formatter)
    log.addHandler(fh)

    log.info("changing_client_name_nt1.py is running")

    app.go_to_online_version(ov_link="https://login.consultant.ru")
    app.login_client(client_name="866712#autotest4", client_password="cDKgrqe7")
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_name(client_name="")
    if (app.is_element_present_main(locator1) == True and app.is_element_present_main(locator2) == True):
        log.info(
            "Нельзя сохранить пустое имя Клиента (в поле 'Имя' отображается 'Введите Ваше имя', "
            "под полем 'Имя' - 'Заполните это поле', после нажатия на 'Сохранить' остались в окне 'Изменить контактные данные') "
            "- ТЕСТ УСПЕШНЫЙ")
    else:
        log.info("ОШИБКА: Не найдено: в поле 'Имя' - 'Введите Ваше имя', под полем 'Имя' - 'Заполните это поле' "
                 "- ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator1) == True and app.is_element_present_main(locator2) == True)

    app.logout_client()
    log.info("changing_client_name_nt1.py is done successfully")
