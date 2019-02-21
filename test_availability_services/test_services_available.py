# -*- encoding: utf-8 -*-

import random
import time
import pytest
import allure


# Проверка доступности сервисов "Задать вопрос": Онлайн-диалог и Написать эксперту доступны

@allure.title("Проверка доступности сервисов 'Задать вопрос': Онлайн-диалог и Написать эксперту доступны")
def test_services_available(app):
    print("test_services_available.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    app.kit_search()
    time.sleep(2)

    app.setting_checkbox("on", "//input[@id='3124332_HotlineValue']", "//label[@for='3124332_HotlineValue']")
    app.setting_checkbox("on", "//input[@id='3124332_ExpconsValue']", "//label[@for='3124332_ExpconsValue']")
    time.sleep(2)

    app.save_setting_checkbox()
    time.sleep(2)

    # if (app.is_element_present_main(locator) == True):
    #     print("В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
    #     allure.dynamic.description(
    #         'В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ')
    # else:
    #     print("ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    #     allure.dynamic.description(
    #         'ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!')
    # assert (app.is_element_present_main(locator) == True)

    app.logout_agent()
    print("test_services_available.py is done successfully")


# Проверка доступности сервисов "Задать вопрос": Онлайн-диалог не доступен и Написать эксперту доступно

@allure.title("Проверка доступности сервисов 'Задать вопрос': Онлайн-диалог не доступен")
@pytest.mark.skip(reason='This test is skipped as it is not ready!')
def test_hotline_is_not_available(app):
    print("test_hotline_is_not_available.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    app.kit_search()
    time.sleep(3)

    app.setting_checkbox("off", "//input[@id='3124332_HotlineValue']", "//label[@for='3124332_HotlineValue']")
    app.setting_checkbox("on", "//input[@id='3124332_ExpconsValue']", "//label[@for='3124332_ExpconsValue']")

    time.sleep(3)

    # if (app.is_element_present_main(locator) == True):
    #     print("В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
    #     allure.dynamic.description(
    #         'В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ')
    # else:
    #     print("ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    #     allure.dynamic.description(
    #         'ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!')
    # assert (app.is_element_present_main(locator) == True)

    app.logout_agent()
    print("test_hotline_is_not_available.py is done successfully")


# Проверка доступности сервисов "Задать вопрос": Онлайн-диалог доступен и Написать эксперту не доступно

@allure.title("Проверка доступности сервисов 'Задать вопрос': Написать эксперту не доступно")
@pytest.mark.skip(reason='This test is skipped as it is not ready!')
def test_expcons_is_not_available(app):
    print("test_expcons_is_not_available.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    app.kit_search()
    time.sleep(3)

    app.setting_checkbox("on", "//input[@id='3124332_HotlineValue']", "//label[@for='3124332_HotlineValue']")
    app.setting_checkbox("off", "//input[@id='3124332_ExpconsValue']", "//label[@for='3124332_ExpconsValue']")

    time.sleep(3)

    # if (app.is_element_present_main(locator) == True):
    #     print("В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
    #     allure.dynamic.description(
    #         'В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ')
    # else:
    #     print("ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    #     allure.dynamic.description(
    #         'ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!')
    # assert (app.is_element_present_main(locator) == True)

    app.logout_agent()
    print("test_expcons_is_not_available.py is done successfully")


# Проверка доступности сервисов "Задать вопрос": Онлайн-диалог и Написать эксперту не доступны

@allure.title("Проверка доступности сервисов 'Задать вопрос': Онлайн-диалог и Написать эксперту не доступны")
@pytest.mark.skip(reason='This test is skipped as it is not ready!')
def test_services_is_not_available(app):
    print("test_services_is_not_available.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    app.kit_search()
    time.sleep(3)

    app.setting_checkbox("off", "//input[@id='3124332_HotlineValue']", "//label[@for='3124332_HotlineValue']")
    app.setting_checkbox("off", "//input[@id='3124332_ExpconsValue']", "//label[@for='3124332_ExpconsValue']")

    time.sleep(3)

    # if (app.is_element_present_main(locator) == True):
    #     print("В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ")
    #     allure.dynamic.description(
    #         'В ОД email Клиента совпадает с новым значением - ТЕСТ УСПЕШНЫЙ')
    # else:
    #     print("ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    #     allure.dynamic.description(
    #         'ОШИБКА: В ОД email Клиента не совпадает с новым значением - ТЕСТ НЕ УСПЕШНЫЙ!!!')
    # assert (app.is_element_present_main(locator) == True)

    app.logout_agent()
    print("test_services_is_not_available.py is done successfully")