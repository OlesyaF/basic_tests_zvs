# -*- encoding: utf-8 -*-

import time

import allure
import pytest


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
    app.save_setting_checkbox()
    time.sleep(2)

    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)

    print("Проверка наличия вкладки 'Онлайн-диалог' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[contains(text(),'Онлайн-диалог')]") == True):
        print("Вкладка 'Онлайн-диалог' присутствует")
    else:
        print("ОШИБКА!!! Вкладка 'Онлайн-диалог' отсутствует!")
        assert (app.is_element_present_main("//div[contains(text(),'Онлайн-диалог')]") == True)

    print("Проверка наличия вкладки 'Написать эксперту' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[contains(text(),'Написать эксперту')]") == True):
        print("Вкладка 'Написать эксперту' присутствует")
    else:
        print("ОШИБКА!!! Вкладка 'Написать эксперту' отсутствует!")
        assert (app.is_element_present_main("//div[contains(text(),'Написать эксперту')]") == True)

    print("Проверка наличия вкладки 'Горячая линия/Контактная информация РИЦ' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[@id='tabLabelPhone']") == True):
        print("Вкладка 'Горячая линия/Контактная информация РИЦ' присутствует")
    else:
        print("ОШИБКА!!! Вкладка 'Горячая линия/Контактная информация РИЦ' отсутствует!")
        assert (app.is_element_present_main("//div[@id='tabLabelPhone']") == True)

    app.check_hotline_availability()
    app.go_to_expcons()
    app.check_expcons_availability()
    app.go_to_byphone()
    app.check_byphone_availability()

    app.logout_client()
    print("test_services_available.py is done successfully")


# Проверка доступности сервисов "Задать вопрос": Онлайн-диалог не доступен и Написать эксперту доступно

@allure.title("Проверка доступности сервисов 'Задать вопрос': Онлайн-диалог не доступен")
@pytest.mark.skip(reason='This test is skipped as it is not ready!')
def test_hotline_is_not_available(app):
    pytest.skip('This test is skipped as it is not ready!')
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
    pytest.skip('This test is skipped as it is not ready!')
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
    pytest.skip('This test is skipped as it is not ready!')
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
