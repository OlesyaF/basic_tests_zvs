# -*- encoding: utf-8 -*-

import time

import allure


# Проверка доступности сервисов "Задать вопрос": Онлайн-диалог доступен и Написать эксперту не доступно

@allure.title("Проверка доступности сервисов 'Задать вопрос': Написать эксперту не доступно")
def test_expcons_is_not_available(app):
    print("test_2_expcons_is_not_available.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    app.press_configure()
    app.kit_search()
    kit_id = app.get_kit_id()
    time.sleep(2)

    app.setting_checkbox("on", "//input[@id='" + kit_id + "_HotlineValue']", "//label[@for='" + kit_id + "_HotlineValue']")
    app.setting_checkbox("off", "//input[@id='" + kit_id + "_ExpconsValue']", "//label[@for='" + kit_id + "_ExpconsValue']")
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

    print("Проверка отсутствия вкладки 'Написать эксперту' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[contains(text(),'Написать эксперту')]") == False):
        print("Вкладка 'Написать эксперту' отсутствует")
    else:
        print("ОШИБКА!!! Вкладка 'Написать эксперту' присутствует!")
        assert (app.is_element_present_main("//div[contains(text(),'Написать эксперту')]") == False)

    print("Проверка наличия вкладки 'Горячая линия/Контактная информация РИЦ' в окне 'Сервис поддержки клиентов':")
    if (app.is_element_present_main("//div[@id='tabLabelPhone']") == True):
        print("Вкладка 'Горячая линия/Контактная информация РИЦ' присутствует")
    else:
        print("ОШИБКА!!! Вкладка 'Горячая линия/Контактная информация РИЦ' отсутствует!")
        assert (app.is_element_present_main("//div[@id='tabLabelPhone']") == True)

    app.check_hotline_availability()
    # Переход на вкладку с контактами Горячей линии и РИЦ
    app.click_by_phone()
    app.check_byphone_availability()
    # Возврат со вкладки с контактами Горячей линии и РИЦ (попадаем на вкладку "Онлайн-диалог")
    app.click_by_phone()
    # Проверям, что папали на вкладку "Онлайн-диалог"
    app.check_hotline_availability()

    app.logout_client()
    print("test_2_expcons_is_not_available.py is done successfully")
