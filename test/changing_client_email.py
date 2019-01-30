# -*- encoding: utf-8 -*-

import time

import pytest

from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# Изменение email клиента

def test_changing_client_email(app):
    email = str(app.calc_check_sum_from_date()) + "@autotest4.ru"
    print("email: ", email)
    locator = "//span[contains(text(),'" + email + "')]"

    print("changing_client_email.py is running")

    app.go_to_online_version(ov_link="https://login.consultant.ru")
    app.login_client(client_name="866712#autotest4", client_password="cDKgrqe7")
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_email(email)
    if (app.is_element_present_main(locator) == True):
        print("В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator) == True)

    app.logout_client()
    print("changing_client_email.py is done successfully")
