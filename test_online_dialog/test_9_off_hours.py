# -*- encoding: utf-8 -*-

import time
import allure


# Проверка работы Чата при переходе на нерабочее время и обратно

@allure.title("Проверка взятия в работу в нерабочее время Чата, попавшего в очередь в рабочее время")
def test_queue_off_hours(app):
    print("test_queue_off_hours.py is running")

    # PRECONDITION: Завершение всех активных Чатов в АРМ РИЦ
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(15)
    app.agent_completion_chat()
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client_1 = "BasicATClient_message_1_" + str(num)
    app.client_send_message(mess_client_1)
    app.is_client_message_in_ov_chat(mess_client_1)
    time.sleep(10)
    app.logout_client()

    weekday = time.strftime("%a", time.localtime(time.time()))
    weekday_num = 1 + int(time.strftime("%w", time.localtime(time.time())))
    hour = time.strftime("%H", time.localtime(time.time()))
    print("weekday = ", weekday)
    print("weekday_num = ", weekday_num)
    print("hour = ", hour)

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    if (app.is_element_visible_main("//div[@class='HelperQueue' and text()='В очереди клиентов на консультацию: 0 человек']") == True):
        print("ОШИБКА!!! Перед переходом на нерабочее время очередь пуста!")
        assert(app.is_element_visible_main("//div[@class='HelperQueue' and text()='В очереди клиентов на консультацию: 0 человек']") != True)
    app.go_to_work_time_settings()
    unavailable_text = app.get_agent_unavailable_text()
    app.set_up_work_time(weekday, hour, weekday_num)
    app.go_to_online_dialog()
    time.sleep(2)
    app.agent_search_only_one_chat()
    time.sleep(7)
    app.is_client_message_in_arm_ric_chat(mess_client_1)
    mess_agent = "BasicATAgent_message_" + str(num)
    app.agent_send_message(mess_agent)
    app.is_agent_message_in_arm_ric_chat(mess_agent)
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.is_agent_message_in_ov_chat(mess_agent)
    mess_client_2 = "BasicATClient_message_2_" + str(num)
    app.client_send_message(mess_client_2)
    app.is_client_message_in_ov_chat(mess_client_2)
    if (app.is_element_visible_main("//div[contains(text(),'" + unavailable_text + "')]") != True):
        print(
            "В ОД ОВ не отображается сообщение о недоступности онлайн-диалога, заданное в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ")
    else:
        print(
            "ОШИБКА!!! В ОД ОВ отображается сообщение о недоступности онлайн-диалога, указанное в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ")
        assert (app.is_element_visible_main("//div[contains(text(),'" + unavailable_text + "')]") != True)
    app.logout_client()

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_search_only_one_chat()
    time.sleep(7)
    app.is_client_message_in_arm_ric_chat(mess_client_2)
    app.go_to_work_time_settings()
    app.set_up_work_time(weekday, hour, weekday_num=0)
    app.logout_agent()

    allure.dynamic.description(
        'Чат, попавший в очередь в рабочее время, взят в работу в нерабочее время: в ОД ОВ Клиент отправляет в Чат сообщения, в ОД ОВ не отображается сообщение о недоступности онлайн-диалога - ТЕСТ УСПЕШНЫЙ!')
    print(
        "Чат, начатый в рабочее время, при переходе на нерабочее время остается активным: в ОД ОВ Клиент отправляет в Чат сообщения, в ОД ОВ не отображается сообщение о недоступности онлайн-диалога - ТЕСТ УСПЕШНЫЙ!")

    print("test_queue_off_hours.py is done successfully")


@allure.title("Проверка завершения Чата в нерабочее время")
def test_completion_off_hours(app):
    print("test_completion_off_hours.py is running")

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_message_" + str(num)
    app.client_send_message(mess_client)
    app.is_client_message_in_ov_chat(mess_client)
    app.logout_client()

    weekday = time.strftime("%a", time.localtime(time.time()))
    weekday_num = 1 + int(time.strftime("%w", time.localtime(time.time())))
    hour = time.strftime("%H", time.localtime(time.time()))
    print("weekday = ", weekday)
    print("weekday_num = ", weekday_num)
    print("hour = ", hour)

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.go_to_work_time_settings()
    unavailable_text = app.get_agent_unavailable_text()
    app.set_up_work_time(weekday, hour, weekday_num)
    app.go_to_online_dialog()
    app.agent_search_only_one_chat()
    time.sleep(7)
    app.is_client_message_in_arm_ric_chat(mess_client)
    mess_agent = "BasicATAgent_message_" + str(num)
    app.agent_send_message(mess_agent)
    app.is_agent_message_in_arm_ric_chat(mess_agent)
    app.agent_completion_chat()
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.is_agent_message_in_ov_chat(mess_agent)

    if (app.is_element_present_main("//div[contains(text(),'" + unavailable_text + "')]") == True):
        print(
            "В ОД ОВ отображается сообщение о недоступности онлайн-диалога, заданное в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ.")
    else:
        print(
            "ОШИБКА!!! В ОД ОВ не отображается сообщение о недоступности онлайн-диалога, указанное в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ")
        assert (app.is_element_present_main("//div[contains(text(),'" + unavailable_text + "')]") == True)

    if (app.is_element_present_main("//textarea[@id='MsgInput' and @disabled]") == True):
        print(
            "Поле для ввода сообщения не активно.")
    else:
        print(
            "ОШИБКА!!! Поле для ввода сообщения активно.")
        assert (app.is_element_present_main("//textarea[@id='MsgInput' and @disabled]") == True)

    if (app.is_element_present_main("//div[@id='ChatMsgSubmit' and @class='send_button MsgSubmit disabled']") == True):
        print(
            "Кнопка отправки сообщения заблокирована.")
    else:
        print(
            "ОШИБКА!!! Кнопка отправки сообщения активна.")
        assert (app.is_element_present_main("//div[@id='ChatMsgSubmit' and @class='send_button MsgSubmit disabled']") == True)

    app.logout_client()

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.go_to_work_time_settings()
    app.set_up_work_time(weekday, hour, weekday_num=0)
    app.logout_agent()

    allure.dynamic.description(
        'Чат, завершенный Агентом в нерабочее время, не может быть продолжен: в ОД ОВ поле для ввода сообщения заблокировано и отображается сообщение о недоступности онлайн-диалога, заданное в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ - ТЕСТ УСПЕШНЫЙ!')

    print("test_completion_off_hours.py is done successfully")


@allure.title("Проверка невозможности начать Чат в нерабочее время")
def test_start_chat_off_hours(app):
    print("test_start_chat_off_hours.py is running")

    weekday = time.strftime("%a", time.localtime(time.time()))
    weekday_num = 1 + int(time.strftime("%w", time.localtime(time.time())))
    hour = time.strftime("%H", time.localtime(time.time()))
    print("weekday = ", weekday)
    print("weekday_num = ", weekday_num)
    print("hour = ", hour)

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_completion_chat()
    app.go_to_work_time_settings()
    unavailable_text = app.get_agent_unavailable_text()
    app.set_up_work_time(weekday, hour, weekday_num)
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)

    if (app.is_element_present_main("//div[contains(text(),'" + unavailable_text + "')]") == True):
        print(
            "В ОД ОВ отображается сообщение о недоступности онлайн-диалога, заданное в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ.")
    else:
        print(
            "ОШИБКА!!! В ОД ОВ не отображается сообщение о недоступности онлайн-диалога, указанное в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ")
        assert (app.is_element_present_main("//div[contains(text(),'" + unavailable_text + "')]") == True)

    if (app.is_element_present_main("//textarea[@id='MsgInput' and @disabled]") == True):
        print(
            "Поле для ввода сообщения не активно.")
    else:
        print(
            "ОШИБКА!!! Поле для ввода сообщения активно.")
        assert (app.is_element_present_main("//textarea[@id='MsgInput' and @disabled]") == True)

    if (app.is_element_present_main("//div[@id='ChatMsgSubmit' and @class='send_button MsgSubmit disabled']") == True):
        print(
            "Кнопка отправки сообщения заблокирована.")
    else:
        print(
            "ОШИБКА!!! Кнопка отправки сообщения активна.")
        assert (app.is_element_present_main("//div[@id='ChatMsgSubmit' and @class='send_button MsgSubmit disabled']") == True)

    app.logout_client()

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.go_to_work_time_settings()
    app.set_up_work_time(weekday, hour, weekday_num=0)
    app.logout_agent()

    allure.dynamic.description(
        'Клиент не может начать Чат в нерабочее время: в ОД ОВ поле для ввода сообщения заблокировано и отображается сообщение о недоступности онлайн-диалога, заданное в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ - ТЕСТ УСПЕШНЫЙ!')

    print("test_start_chat_off_hours.py is done successfully")


@allure.title("Проверка работы Чата, начатого в рабочее время, при переходе на нерабочее время")
def test_chat_off_hours(app):
    print("test_chat_off_hours.py is running")

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client_1 = "BasicATClient_message_1_" + str(num)
    app.client_send_message(mess_client_1)
    app.is_client_message_in_ov_chat(mess_client_1)
    app.logout_client()

    weekday = time.strftime("%a", time.localtime(time.time()))
    weekday_num = 1 + int(time.strftime("%w", time.localtime(time.time())))
    hour = time.strftime("%H", time.localtime(time.time()))
    print("weekday = ", weekday)
    print("weekday_num = ", weekday_num)
    print("hour = ", hour)

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_search_only_one_chat()
    time.sleep(7)
    app.is_client_message_in_arm_ric_chat(mess_client_1)
    mess_agent_1 = "BasicATAgent_message_1_" + str(num)
    app.agent_send_message(mess_agent_1)
    app.is_agent_message_in_arm_ric_chat(mess_agent_1)
    app.go_to_work_time_settings()
    unavailable_text = app.get_agent_unavailable_text()
    app.set_up_work_time(weekday, hour, weekday_num)
    app.go_to_online_dialog()
    time.sleep(2)
    mess_agent_2 = "BasicATAgent_message_2_" + str(num)
    app.agent_send_message(mess_agent_2)
    app.is_agent_message_in_arm_ric_chat(mess_agent_2)
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.is_agent_message_in_ov_chat(mess_agent_1)
    app.is_agent_message_in_ov_chat(mess_agent_2)
    mess_client_2 = "BasicATClient_message_2_" + str(num)
    app.client_send_message(mess_client_2)
    app.is_client_message_in_ov_chat(mess_client_2)
    app.check_click("//textarea[@id='MsgInput']")
    time.sleep(10)
    if (app.is_element_visible_main("//div[contains(text(),'" + unavailable_text + "')]") != True):
        print(
            "В ОД ОВ не отображается сообщение о недоступности онлайн-диалога, заданное в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ")
    else:
        print(
            "ОШИБКА!!! В ОД ОВ отображается сообщение о недоступности онлайн-диалога, указанное в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ")
        assert (app.is_element_visible_main("//div[contains(text(),'" + unavailable_text + "')]") != True)
    app.logout_client()

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_search_only_one_chat()
    time.sleep(7)
    app.is_client_message_in_arm_ric_chat(mess_client_2)
    app.go_to_work_time_settings()
    app.set_up_work_time(weekday, hour, weekday_num=0)
    app.logout_agent()

    allure.dynamic.description(
        'Чат, начатый в рабочее время, при переходе на нерабочее время остается активным: в ОД ОВ Клиент отправляет в Чат сообщения, в ОД ОВ не отображается сообщение о недоступности онлайн-диалога - ТЕСТ УСПЕШНЫЙ!')
    print(
        "Чат, начатый в рабочее время, при переходе на нерабочее время остается активным: в ОД ОВ Клиент отправляет в Чат сообщения, в ОД ОВ не отображается сообщение о недоступности онлайн-диалога - ТЕСТ УСПЕШНЫЙ!")

    print("test_chat_off_hours.py is done successfully")