# -*- encoding: utf-8 -*-

import datetime
import time
import allure


# Проверка отображения карточки Клиента в АРМ РИЦ

@allure.title("Проверка отображения карточки Клиента в АРМ РИЦ")
def test_client_card(app):
    print("test_client_card.py is running")

    #PRECONDITION: Завершение всех активных Чатов в АРМ РИЦ
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_completion_chat()
    app.logout_agent()

    #PRECONDITION: Отправка Клиентом сообщения
    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    client_name = app.get_client_name()
    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_" + str(num)
    app.client_send_message(mess_client)
    app.is_client_message_in_ov_chat(mess_client)
    app.logout_client()

    #TEST
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_search_only_one_chat()

    locator1 = "//strong[contains(text(),'" + client_name + "')]"
    locator2 = "//strong[contains(text(),'Универсальный')]"
    locator3 = "//*[contains(text(),'Производится поиск свободного специалиста. Пожалуйста, подождите.')]"
    locator4 = "//*[contains(text(),'В настоящий момент все специалисты заняты. Подождите, пожалуйста, еще немного.')]"
    locator5 = "//*[contains(text(),'В ближайшее время специалист подключится к беседе с Вами.')]"
    locator6 = "//*[contains(text(),'Пожалуйста, подождите. Мы ответим Вам очень скоро.')]"

    if (app.is_element_visible_main(locator1) == True and app.is_element_visible_main(locator2) == True):
        print(
            "В активном Чате не отображаются приветственные и ожидательные сообщения - ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description(
            'В активном Чате не отображаются  приветственные и ожидательные сообщения - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: В активном Чате отображаются приветственные и/или ожидательные сообщения - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: В активном Чате отображаются приветственные и/или ожидательные сообщения - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_visible_main(locator1) == True and app.is_element_visible_main(locator2) == True)

    app.logout_agent()
    print("test_client_card.py is done successfully")
