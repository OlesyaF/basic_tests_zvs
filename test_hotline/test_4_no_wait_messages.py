# -*- encoding: utf-8 -*-

import time

import allure


# Проверка отсутствия в активном Чате ОВ служебных сообщений: приветствия и уведомлений при ожидании подключения Агента

@allure.title(
    "Проверка отсутствия в активном Чате ОВ служебных сообщений: приветствия и уведомлений при ожидании подключения Агента")
def test_no_wait_messages(app):
    print("test_4_no_wait_messages.py is running")

    # PRECONDITION: Завершение всех активных Чатов в АРМ РИЦ
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_completion_chat()
    app.logout_agent()

    # PRECONDITION: Создание активного Чата (Онлайн-Версия)
    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_message_" + str(num)
    app.client_send_message(mess_client)
    app.is_client_message_in_ov_chat(mess_client)
    app.logout_client()

    # PRECONDITION: Создание активного Чата (АРМ РИЦ)
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    mess_agent = "BasicATAgent_message_" + str(num)
    app.agent_search_only_one_chat()
    time.sleep(7)
    app.is_client_message_in_arm_ric_chat(mess_client)
    app.agent_send_message(mess_agent)
    app.is_agent_message_in_arm_ric_chat(mess_agent)
    app.logout_agent()

    # TEST
    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    client_name = app.get_client_name()
    app.go_out_client_info()
    time.sleep(2)

    locator1 = "//div[contains(text(),'Здравствуйте, " + client_name + "!')]"
    locator2 = "//*[contains(text(),'Введите свой вопрос. Мы подключимся к диалогу в ближайшее время.')]"
    locator3 = "//*[contains(text(),'Производится поиск свободного специалиста. Пожалуйста, подождите.')]"
    locator4 = "//*[contains(text(),'В настоящий момент все специалисты заняты. Подождите, пожалуйста, еще немного.')]"
    locator5 = "//*[contains(text(),'В ближайшее время специалист подключится к беседе с Вами.')]"
    locator6 = "//*[contains(text(),'Пожалуйста, подождите. Мы ответим Вам очень скоро.')]"

    if (app.is_element_visible_main(locator1) == False and app.is_element_visible_main(
            locator2) == False and app.is_element_visible_main(locator3) == False and app.is_element_visible_main(
        locator4) == False and app.is_element_visible_main(locator5) == False and app.is_element_visible_main(
        locator6) == False):
        print(
            "В активном Чате не отображаются приветственные и ожидательные сообщения - ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description(
            'В активном Чате не отображаются  приветственные и ожидательные сообщения - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: В активном Чате отображаются приветственные и/или ожидательные сообщения - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: В активном Чате отображаются приветственные и/или ожидательные сообщения - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_visible_main(locator1) == False and app.is_element_visible_main(
            locator2) == False and app.is_element_visible_main(locator3) == False and app.is_element_visible_main(
            locator4) == False and app.is_element_visible_main(locator5) == False and app.is_element_visible_main(
            locator6) == False)

    app.logout_client()
    print("test_4_no_wait_messages.py is done successfully")
