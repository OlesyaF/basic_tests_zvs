# -*- encoding: utf-8 -*-

import time
import allure


# Проверка завершения сеанса

@allure.title("Проверка завершения Чата")
def test_5_completion_sessions(app):
    print("test_5_completion_sessions.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    elements = "//button[contains(@name,'CloseSession') and @class='HelperButton']"
    count_of_chat_before = app.count_of_elements_main(elements)
    if count_of_chat_before > 0:
        print("У Агента есть активные Чаты")
        app.agent_completion_chat()
        count_of_chat_after = app.count_of_elements_main(elements)
        if (count_of_chat_after == 0):
            print("Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ")
            allure.dynamic.description('Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ')
        else:
            print("ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!")
            allure.dynamic.description('ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!')
            assert (app.count_of_elements_main(elements) == 0)
        app.logout_agent()
    else:
        print("У Агента нет активных Чатов")
        app.logout_agent()

        app.go_to_online_version()
        app.login_client()
        app.go_to_customer_support_service()
        time.sleep(7)
        client_name = app.get_client_name()
        num = app.calc_check_sum_from_date()
        mess_client = "BasicATClient_message_" + str(num)
        app.client_send_message(mess_client)
        app.is_client_message_in_ov_chat(mess_client)
        app.logout_client()

        app.go_to_arm_ric()
        app.login_agent()
        time.sleep(10)
        app.agent_search_chat(client_name)
        time.sleep(7)
        elements = "//button[contains(@name,'CloseSession') and @class='HelperButton']"
        count_of_chat_before = app.count_of_elements_main(elements)
        if count_of_chat_before > 0:
            print("У Агента есть активные Чаты")
            app.agent_completion_chat()
            count_of_chat_after = app.count_of_elements_main(elements)
            if (count_of_chat_after == 0):
                print("Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ")
                allure.dynamic.description('Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ')
            else:
                print("ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!")
                allure.dynamic.description('ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!')
                assert (app.count_of_elements_main(elements) == 0)
            app.logout_agent()

    print("test_5_completion_sessions.py is done successfully")
