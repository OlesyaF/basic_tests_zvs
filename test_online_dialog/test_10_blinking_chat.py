# -*- encoding: utf-8 -*-

import time

import allure


# Проверка работы Чата при переходе на нерабочее время и обратно

@allure.title("Проверка работы Чата, начатого в рабочее время, при переходе на нерабочее время")
def test_blinking_chat(app):
    print("test_blinking_chat.py is running")

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client_1 = "BasicATClient_message_1_" + str(num)
    app.client_send_message(mess_client_1)
    app.is_client_message_in_ov_chat(mess_client_1)
    app.logout_client()

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_search_only_one_chat()
    time.sleep(7)
    app.is_client_message_in_arm_ric_chat(mess_client_1)
    mess_agent_1 = "BasicATAgent_message_1_" + str(num)
    app.agent_send_message(mess_agent_1)
    app.is_agent_message_in_arm_ric_chat(mess_agent_1)
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()

    if (app.is_element_present_main_css("div.livechat.right.blink") == True):
        print("Меню 'Задать вопрос' мигает")
    else:
        print("ОШИБКА!!! Меню 'Задать вопрос' не мигает")
        assert (app.is_element_present_main_css("div.livechat.right.blink") == True)

    app.go_to_customer_support_service_press_button()

    if (app.is_element_present_main_css("div.livechat.right.hidden") == True):
        print("Меню 'Задать вопрос' не отображается")
    else:
        print("ОШИБКА!!! Меню 'Задать вопрос' отображается")
        assert (app.is_element_present_main_css("div.livechat.right.hidden") == True)

    app.go_to_customer_support_service_go_frame()
    time.sleep(7)
    app.is_agent_message_in_ov_chat(mess_agent_1)
    app.go_out_customer_support_service()

    time.sleep(3)

    if (app.is_element_present_main_css("div.livechat.right.hidden") != True):
        print("Меню 'Задать вопрос' отображается")
    else:
        print("ОШИБКА!!! Меню 'Задать вопрос' скрыто")
        assert (app.is_element_present_main_css("div.livechat.right.hidden") != True)

    if (app.is_element_present_main_css("div.livechat.right.blink") != True):
        print("Меню 'Задать вопрос' не мигает")
    else:
        print("ОШИБКА!!! Меню 'Задать вопрос' мигает")
        assert (app.is_element_present_main_css("div.livechat.right.blink") != True)

    app.logout_client()

    print("test_blinking_chat.py is done successfully")
