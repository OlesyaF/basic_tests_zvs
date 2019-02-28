# -*- encoding: utf-8 -*-

import time

import allure


# Проверка обмена сообщениями между Клиентом и Агентом

@allure.title("Проверка обмена сообщениями между Клиентом и Агентом")
def test_messaging(app):
    print("test_messaging.py is running")

    # app.go_to_online_version()
    # app.login_client(client_name="866712#fesayoyu", client_password="qNIgSjXz")
    # app.go_to_online_dialog(wait)
    # app.client_send_message(mess_client)
    # app.is_client_message_in_online_dialog(mess_client)
    # app.logout_client()
    # app.go_to_consultant_plus_agent()
    # app.login_agent(agent_login="ric997fesaiou", agent_password="m6pqbufy")
    # app.agent_search_chat_and_mess(mess_client, wait)
    # app.agent_send_message(mess_agent)
    # app.is_agent_message_in_consultant_plus(mess_agent)
    # app.logout_agent()
    # app.go_to_online_version()
    # app.login_client(client_name="866712#fesayoyu", client_password="qNIgSjXz")
    # app.go_to_online_dialog(wait)
    # app.is_agent_message_in_online_dialog(mess_agent)
    # app.logout_client()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    client_name = str(app.calc_check_sum_from_date()) + "#autotest"
    print("client_name: ", client_name)
    locator = "//span[contains(text(),'" + client_name + "')]"
    app.changing_client_name(client_name)
    app.save_client_info()
    if (app.is_element_present_main(locator) == True):
        print("В ОД имя Клиента совпадает с новым значением")
    else:
        print("ОШИБКА: В ОД имя Клиента не совпадает с новым значением!")
    assert (app.is_element_present_main(locator) == True)
    app.logout_client()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_" + str(num)
    mess_agent = "BasicATAgent_" + str(num)
    app.client_send_message(mess_client)
    app.is_client_message_in_online_dialog(mess_client)
    app.logout_client()

    app.go_to_arm_ric()
    app.login_agent()



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
