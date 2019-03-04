# -*- encoding: utf-8 -*-

import time

import allure


# Проверка отсутствия служебных сообщений об ожидания после подключения Агента к Чату

@allure.title("Проверка отсутствия служебных сообщений об ожидания после подключения Агента к Чату")
def test_no_wait_messages(app):
    print("test_4_no_wait_messages.py is running")

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)

    locator1 = "//*[contains(text(),'Производится поиск свободного специалиста. Пожалуйста, подождите.')]"
    locator2 = "//*[contains(text(),'В настоящий момент все специалисты заняты. Подождите, пожалуйста, еще немного.')]"
    locator3 = "//*[contains(text(),'В ближайшее время специалист подключится к беседе с Вами.')]"
    locator4 = "//*[contains(text(),'Пожалуйста, подождите. Мы ответим Вам очень скоро.')]"
    if (app.is_element_present_main(locator1) == False and app.is_element_present_main(
            locator2) == False and app.is_element_present_main(locator3) == False and app.is_element_present_main(
            locator4) == False):
        print(
            "В активном Чате не отображаются ожидательные сообщения - ТЕСТ УСПЕШНЫЙ")
        allure.dynamic.description('В активном Чате не отображаются ожидательные сообщения - ТЕСТ УСПЕШНЫЙ')
    else:
        print("ОШИБКА: В активном Чате отображаются ожидательные сообщения - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        allure.dynamic.description('ОШИБКА: В активном Чате отображаются ожидательные сообщения - ТЕСТ НЕ УСПЕШНЫЙ!!!')
    assert (app.is_element_present_main(locator1) == False and app.is_element_present_main(
        locator2) == False and app.is_element_present_main(locator3) == False and app.is_element_present_main(
        locator4) == False)

    app.logout_client()
    print("test_4_no_wait_messages.py is done successfully")
