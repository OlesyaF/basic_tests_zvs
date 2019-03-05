# -*- encoding: utf-8 -*-

import time

import allure


# Проверка отсутствия в активном Чате ОВ служебных сообщений: приветствия и уведомлений при ожидании подключения Агента

@allure.title("Проверка отсутствия в активном Чате ОВ служебных сообщений: приветствия и уведомлений при ожидании подключения Агента")
def test_no_wait_messages(app):
    print("test_4_no_wait_messages.py is running")

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)

    locator1 = "//div[contains(text(),'Здравствуйте, 866712#main_autotest!')]"
    locator2 = "//*[contains(text(),'Введите свой вопрос. Мы подключимся к диалогу в ближайшее время.')]"
    locator3 = "//*[contains(text(),'Производится поиск свободного специалиста. Пожалуйста, подождите.')]"
    locator4 = "//*[contains(text(),'В настоящий момент все специалисты заняты. Подождите, пожалуйста, еще немного.')]"
    locator5 = "//*[contains(text(),'В ближайшее время специалист подключится к беседе с Вами.')]"
    locator6 = "//*[contains(text(),'Пожалуйста, подождите. Мы ответим Вам очень скоро.')]"
    if (app.is_element_visible_main(locator1) == False and app.is_element_visible_main(
            locator2) == False and app.is_element_visible_main(locator3) == False and app.is_element_visible_main(
        locator4) == False and app.is_element_visible_main(locator5) == False and app.is_element_visible_main(
        locator6) == False):
        print(
            "В активном Чате не отображаются приветственные и ожидательные сообщения - ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description(
            'В активном Чате не отображаются  приветственные и ожидательные сообщения - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: В активном Чате отображаются приветственные и/или ожидательные сообщения - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description(
            'ОШИБКА: В активном Чате отображаются приветственные и/или ожидательные сообщения - ТЕСТ НЕ УСПЕШНЫЙ!!!')
        assert (app.is_element_visible_main(locator1) == False and app.is_element_visible_main(
            locator2) == False and app.is_element_visible_main(locator3) == False and app.is_element_visible_main(
            locator4) == False and app.is_element_visible_main(locator5) == False and app.is_element_visible_main(
            locator6) == False)

    app.logout_client()
    print("test_4_no_wait_messages.py is done successfully")
