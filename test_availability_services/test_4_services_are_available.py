# -*- encoding: utf-8 -*-

import time

import allure


# Проверка доступности сервисов "Задать вопрос": Онлайн-диалог и Написать эксперту доступны

@allure.title("Проверка доступности сервисов 'Задать вопрос': Онлайн-диалог и Написать эксперту доступны")
def test_services_available(app):
    print("test_4_services_are_available.py is running")

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
    # Переход на вкладку "Написать эксперту"
    app.go_to_expcons()
    app.check_expcons_availability()
    # Переход на вкладку с контактами Горячей линии и РИЦ
    app.click_by_phone()
    app.check_byphone_availability()
    # Возврат со вкладки с контактами Горячей линии и РИЦ (попадаем на вкладку "Написать эксперту")
    app.click_by_phone()
    # Проверям, что попали на вкладку "Написать эксперту"
    app.check_expcons_availability()

    app.logout_client()
    print("test_4_services_are_available.py is done successfully")
