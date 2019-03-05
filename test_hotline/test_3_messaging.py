# -*- encoding: utf-8 -*-

import time

import allure


# Проверка обмена сообщениями между Клиентом и Агентом

@allure.title("Проверка обмена сообщениями между Клиентом и Агентом")
def test_messaging(app):
    print("test_3_messaging.py is running")

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_" + str(num)
    app.client_send_message(mess_client)
    app.is_client_message_in_ov_chat(mess_client)
    app.logout_client()

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    mess_agent = "BasicATAgent_" + str(num)
    client_name = "866712#main_autotest"
    app.agent_search_chat(client_name)
    time.sleep(7)
    app.is_client_message_in_arm_ric_chat(mess_client)
    app.agent_send_message(mess_agent)
    app.is_agent_message_in_arm_ric_chat(mess_agent)
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.is_agent_message_in_ov_chat(mess_agent)
    app.logout_client()

    print("test_3_messaging.py is done successfully")
