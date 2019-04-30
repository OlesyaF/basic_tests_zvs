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
    locator_close_session = "//button[contains(@name,'CloseSession') and @class='HelperButton']"
    count_of_chat_before = app.count_of_elements_main(locator_close_session)
    if count_of_chat_before > 0:
        print("У Агента есть", count_of_chat_before, "активных Чатов")
        app.agent_completion_chat()
        count_of_chat_after = app.count_of_elements_main(locator_close_session)
        if (count_of_chat_after == 0):
            print("Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ")
            allure.dynamic.description('Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ')
        else:
            print("ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!")
            allure.dynamic.description('ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!')
            assert (app.count_of_elements_main(locator_close_session) == 0)
        app.logout_agent()
    else:
        print("У Агента нет активных Чатов")
        locator_connect_to_session = "//*[@id='Sessions']/div[3]/button"
        if (app.is_element_visible_main(locator_connect_to_session) == True):
            print("У Агента есть Чат(ы) в очереди")
            app.agent_connect_to_all_chat()
            count_of_chat_before = app.count_of_elements_main(locator_close_session)
            if count_of_chat_before > 0:
                print("У Агента есть", count_of_chat_before, "активных Чатов")
                app.agent_completion_chat()
                count_of_chat_after = app.count_of_elements_main(locator_close_session)
                if (count_of_chat_after == 0):
                    print("Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ")
                    allure.dynamic.description('Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ')
                else:
                    print("ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!")
                    allure.dynamic.description('ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!')
                    assert (app.count_of_elements_main(locator_close_session) == 0)
                app.logout_agent()
        else:
            print("Очередь Чатов пуста")
            app.logout_agent()

            app.go_to_online_version()
            app.login_client()
            app.go_to_customer_support_service()
            time.sleep(7)
            num = app.calc_check_sum_from_date()
            mess_client = "BasicATClient_message_" + str(num)
            app.client_send_message(mess_client)
            app.is_client_message_in_ov_chat(mess_client)
            app.logout_client()

            app.go_to_arm_ric()
            app.login_agent()
            time.sleep(10)
            app.agent_connect_to_all_chat()
            time.sleep(7)
            count_of_chat_before = app.count_of_elements_main(locator_close_session)
            if count_of_chat_before > 0:
                print("У Агента есть активные Чаты")
                app.agent_completion_chat()
                count_of_chat_after = app.count_of_elements_main(locator_close_session)
                if (count_of_chat_after == 0):
                    print("Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ")
                    allure.dynamic.description('Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ')
                else:
                    print("ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!")
                    allure.dynamic.description('ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!')
                    assert (app.count_of_elements_main(locator_close_session) == 0)
                app.logout_agent()

    print("test_5_completion_sessions.py is done successfully")
