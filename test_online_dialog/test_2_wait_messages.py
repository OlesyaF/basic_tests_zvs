# -*- encoding: utf-8 -*-

import time
import allure


# Проверка отображения служебных сообщений во время ожидания подключения к Чату Агента

@allure.title("Проверка отображения сообщений во время ожидания подключения к Чату Агента")
def test_wait_messages(app):
    print("test_2_wait_messages.py is running")

    #PRECONDITION: Очищение очереди и завершение всех активных Чатов в АРМ РИЦ
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_connect_to_all_chat()
    app.agent_completion_chat()
    app.logout_agent()

    #TEST
    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)

    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_" + str(num)
    print("mess_client: ")
    app.client_send_message(mess_client)
    app.is_client_message_in_ov_chat(mess_client)

    locator = "//*[contains(text(),'Производится поиск свободного специалиста. Пожалуйста, подождите.')]"
    if (app.is_element_present_main(locator) == True):
        print("В Чате отображается первое ожидательное сообщение (Производится поиск свободного специалиста. Пожалуйста, подождите.) - ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: Первое ожидательно сообщение в Чате не отображается - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        assert (app.is_element_present_main(locator) == True)

    time.sleep(30)

    locator = "//*[contains(text(),'В настоящий момент все специалисты заняты. Подождите, пожалуйста, еще немного.')]"
    if (app.is_element_present_main(locator) == True):
        print("В Чате отображается второе ожидательное сообщение (В настоящий момент все специалисты заняты. Подождите, пожалуйста, еще немного.) - ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: Второе ожидательно сообщение в Чате не отображается - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        assert (app.is_element_present_main(locator) == True)

    time.sleep(30)

    locator = "//*[contains(text(),'В ближайшее время специалист подключится к беседе с Вами.')]"
    if (app.is_element_present_main(locator) == True):
        print(
            "В Чате отображается третье ожидательное сообщение (В ближайшее время специалист подключится к беседе с Вами.) - ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: Третье ожидательно сообщение в Чате не отображается - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        assert (app.is_element_present_main(locator) == True)

    time.sleep(30)

    locator = "//*[contains(text(),'Пожалуйста, подождите. Мы ответим Вам очень скоро.')]"
    if (app.is_element_present_main(locator) == True):
        print(
            "В Чате отображается четвертое ожидательное сообщение (Пожалуйста, подождите. Мы ответим Вам очень скоро.) - ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: Четвертое ожидательно сообщение в Чате не отображается - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        assert (app.is_element_present_main(locator) == True)

    app.logout_client()
    print("test_2_wait_messages.py is done successfully")
