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
    app.agent_completion_chat()
    count_of_chat_after = app.count_of_elements_main(elements)
    if (count_of_chat_after == 0):
        if (count_of_chat_before > 0):
            print("Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ")
            allure.dynamic.description('Все активные Чаты завершены - ТЕСТ УСПЕШНЫЙ')
        else:
            print("ПРЕДУПРЕЖДЕНИЕ: У Агента нет активных Чатов. Завершено: 0")
            allure.dynamic.description('ПРЕДУПРЕЖДЕНИЕ: У Агента нет активных Чатов. Завершено: 0')
    else:
        print("ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description('ОШИБКА: Завершены не все активные Чаты - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.count_of_elements_main(elements) == 0)
    app.logout_agent()
    print("test_5_completion_sessions.py is done successfully")
