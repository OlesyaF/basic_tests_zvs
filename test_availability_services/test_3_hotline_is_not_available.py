# -*- encoding: utf-8 -*-

import time

import allure


# Проверка доступности сервисов "Задать вопрос": Онлайн-диалог не доступен и Написать эксперту доступно

@allure.title("Проверка доступности сервисов 'Задать вопрос': Онлайн-диалог не доступен")
def test_hotline_is_not_available(app):
    print("test_3_hotline_is_not_available.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    app.kit_search()
    time.sleep(2)

    app.setting_checkbox("off", "//input[@id='3124332_HotlineValue']", "//label[@for='3124332_HotlineValue']")
    app.setting_checkbox("on", "//input[@id='3124332_ExpconsValue']", "//label[@for='3124332_ExpconsValue']")
    app.save_setting_checkbox()
    time.sleep(2)

    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)

    print("Проверка наличия вкладки 'Онлайн-диалог' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[contains(text(),'Онлайн-диалог')]") == False):
        print("Вкладка 'Онлайн-диалог' отсутствует")
    else:
        print("ОШИБКА!!! Вкладка 'Онлайн-диалог' присутствует!")
        assert (app.is_element_present_main("//div[contains(text(),'Онлайн-диалог')]") == False)

    print("Проверка наличия вкладки 'Написать эксперту' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[contains(text(),'Написать эксперту')]") == True):
        print("Вкладка 'Написать эксперту' отсутсвует")
    else:
        print("ОШИБКА!!! Вкладка 'Написать эксперту' присутствует!")
        assert (app.is_element_present_main("//div[contains(text(),'Написать эксперту')]") == True)

    print("Проверка наличия вкладки 'Горячая линия/Контактная информация РИЦ' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[@id='tabLabelPhone']") == True):
        print("Вкладка 'Горячая линия/Контактная информация РИЦ' присутствует")
    else:
        print("ОШИБКА!!! Вкладка 'Горячая линия/Контактная информация РИЦ' отсутствует!")
        assert (app.is_element_present_main("//div[@id='tabLabelPhone']") == True)

    app.check_expcons_availability()
    # Переход на вкладку с контактами Горячей линии и РИЦ
    app.click_by_phone()
    app.check_byphone_availability()
    # Возврат со вкладки с контактами Горячей линии и РИЦ (попадаем на вкладку "Написать эксперту")
    app.click_by_phone()
    # Проверям, что папали на вкладку "Написать эксперту"
    app.check_expcons_availability()

    app.logout_client()
    print("test_3_hotline_is_not_available.py is done successfully")
