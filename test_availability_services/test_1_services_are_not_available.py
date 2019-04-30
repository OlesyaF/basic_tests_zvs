# -*- encoding: utf-8 -*-

import time

import allure


# Проверка доступности сервисов "Задать вопрос": Онлайн-диалог и Написать эксперту не доступны

@allure.title("Проверка доступности сервисов 'Задать вопрос': Онлайн-диалог и Написать эксперту не доступны")
def test_services_are_not_available(app):
    print("test_1_services_are_not_available.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    app.kit_search()
    kit_id = app.get_kit_id()
    time.sleep(2)

    app.setting_checkbox("off", "//input[@id='" + kit_id + "_HotlineValue']", "//label[@for='" + kit_id + "_HotlineValue']")
    app.setting_checkbox("off", "//input[@id='" + kit_id + "_ExpconsValue']", "//label[@for='" + kit_id + "_ExpconsValue']")
    app.save_setting_checkbox()
    time.sleep(2)

    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)

    print("Проверка наличия вкладки 'Онлайн-диалог' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[contains(text(),'Онлайн-диалог')]") == False):
        print("Вкладка 'Онлайн-диалог' присутствует")
    else:
        print("ОШИБКА!!! Вкладка 'Онлайн-диалог' отсутствует!")
        assert (app.is_element_present_main("//div[contains(text(),'Онлайн-диалог')]") == False)

    print("Проверка наличия вкладки 'Написать эксперту' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[contains(text(),'Написать эксперту')]") == False):
        print("Вкладка 'Написать эксперту' присутствует")
    else:
        print("ОШИБКА!!! Вкладка 'Написать эксперту' отсутствует!")
        assert (app.is_element_present_main("//div[contains(text(),'Написать эксперту')]") == False)

    print("Проверка наличия вкладки 'Горячая линия/Контактная информация РИЦ' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[@id='tabLabelPhone']") == True):
        print("Вкладка 'Горячая линия/Контактная информация РИЦ' присутствует")
    else:
        print("ОШИБКА!!! Вкладка 'Горячая линия/Контактная информация РИЦ' отсутствует!")
        assert (app.is_element_present_main("//div[@id='tabLabelPhone']") == True)

    app.check_byphone_availability()

    app.logout_client()
    print("test_1_services_are_not_available.py is done successfully")
