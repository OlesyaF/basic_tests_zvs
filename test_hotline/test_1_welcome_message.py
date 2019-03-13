# -*- encoding: utf-8 -*-

import time
import allure


# Проверка отображения в Чате служебного приветственного сообщения

@allure.title("Проверка отображения приветственного сообщения")
def test_welcome_message(app):
    print("test_1_welcome_message.py is running")

    #PRECONDITION: Завершение всех активных Чатов в АРМ РИЦ
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_completion_chat()
    app.logout_agent()

    #TEST
    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)

    client_name = app.get_client_name()

    locator1 = "//div[contains(text(),'Здравствуйте, " + client_name + "!')]"
    locator2 = "//*[contains(text(),'Введите свой вопрос. Мы подключимся к диалогу в ближайшее время.')]"

    if (app.is_element_present_main(locator1) == True and app.is_element_present_main(locator2) == True):
        print("В Чате отображается корректное приветственное сообщение - ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description('В Чате отображается корректное приветственное сообщение - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: В Чате НЕ отображается корректное приветственное сообщение - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: В Чате НЕ отображается корректное приветственное сообщение - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_present_main(locator1) == True and app.is_element_present_main(locator2) == True)

    app.logout_client()
    print("test_1_welcome_message.py is done successfully")
