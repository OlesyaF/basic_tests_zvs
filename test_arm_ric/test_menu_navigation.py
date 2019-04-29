# -*- encoding: utf-8 -*-

import time
import allure
import pytest


# Проверка навигации по меню АРМ РИЦ

@allure.title("Проверка перехода на вкладку По телефону")
#@pytest.mark.skip(reason='This test is skipped as it is not need!')
def test_go_by_phone(app):
    print("test_go_by_phone.py is running")
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_by_phone()
    app.logout_agent()
    print("test_go_by_phone.py is done successfully")

# @allure.title("Проверка перехода на вкладку По телефону")
# #@pytest.mark.skip(reason='This test is skipped as it is not need!')
# def test_go_by_phone(app):
#     print("test_go_by_phone.py is running")
#     app.go_to_arm_ric()
#     app.login_agent()
#     time.sleep(7)
#     app.go_to_by_phone()
#     app.logout_agent()
#     print("test_go_by_phone.py is done successfully")