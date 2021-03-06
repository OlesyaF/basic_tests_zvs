# -*- encoding: utf-8 -*-

import time

import allure


# Проверка отправки быстрого ответа

@allure.title("Проверка отправки быстрого ответа")
def test_send_fast_answer(app):
    print("test_send_fast_answer.py is running")

    # PRECONDITION: Отправка Клиентом сообщения
    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_" + str(num)
    app.client_send_message(mess_client)
    app.is_client_message_in_ov_chat(mess_client)
    app.logout_client()

    # TEST
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_search_only_one_chat()
    app.agent_send_fast_answer()
    time.sleep(2)
    app.agent_send_message("Контрольное сообщение от Агента-Автотеста!")
    app.logout_agent()
    print("test_send_fast_answer.py is done successfully")
