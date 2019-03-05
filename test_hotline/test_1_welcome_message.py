# -*- encoding: utf-8 -*-

import time
import allure
import pytest


# Проверка отображения в Чате служебного приветственного сообщения

@allure.title("Проверка отображения приветственного сообщения")
#@pytest.mark.skip(reason='This test is skipped as there is not a kit which has not written a long time!')
def test_welcome_message(app):
    print("test_1_welcome_message.py is running")

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    client_name = "866712#main_autotest"
    print("client_name: ", client_name)
    locator = "//span[contains(text(),'" + client_name + "')]"
    app.changing_client_name(client_name)
    app.save_client_info()
    if (app.is_element_present_main(locator) == True):
        print("В ОД имя Клиента совпадает с новым значением")
    else:
        print("ОШИБКА: В ОД имя Клиента не совпадает с новым значением!")
        assert (app.is_element_present_main(locator) == True)
    app.logout_client()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
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
