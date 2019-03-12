# -*- encoding: utf-8 -*-

import datetime
import time

import allure


# Изменение цвета карточки Клиента после взятия сеанса в работу

@allure.title("Изменение цвета карточки Клиента после взятия сеанса в работу")
def test_change_chat_color_green_yellow_red(app):
    print("test_change_chat_color_green_yellow_red.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_completion_chat()
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_" + str(num)
    app.client_send_message(mess_client)
    app.is_client_message_in_ov_chat(mess_client)
    app.logout_client()

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    client_name = "866712#main_autotest"
    app.agent_search_chat(client_name)

    print(str(datetime.datetime.now()))
    locator = "//div[@class='Tick SessionRowActive SessionRowGreen']"
    if (app.is_element_present_main(locator, wait=1) == True):
        print("Карточка нового сеанса зеленая - ТЕСТ УСПЕШНЫЙ")
        print(str(datetime.datetime.now()))
    else:
        print("ОШИБКА: Карточка нового сеанса НЕ зеленая - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator) == True)
    print("Ожидание 30 сек...")

    time.sleep(30)
    locator = "//div[@class='Tick SessionRowActive SessionRowYellow']"
    print(str(datetime.datetime.now()))
    if (app.is_element_present_main(locator, wait=1) == True):
        print(
            "Через 30 секунд зеленая карточка сеанса становится желтой (при отсутствии сообщений со стороны Агента) - ТЕСТ УСПЕШНЫЙ")
        print(str(datetime.datetime.now()))
    else:
        print(
            "ОШИБКА: Через 30 секунд зеленая карточка сеанса НЕ становится желтой (при отсутствии сообщений со стороны Агента) - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator) == True)
    print("Ожидание 30 сек...")

    time.sleep(30)
    locator = "//div[@class='Tick SessionRowActive SessionRowRed']"
    print(str(datetime.datetime.now()))
    if (app.is_element_present_main(locator, wait=1) == True):
        print(
            "Через 30 секунд желтая карточка сеанса становится красной (при отсутствии сообщений со стороны Агента) - ТЕСТ УСПЕШНЫЙ")
        print(str(datetime.datetime.now()))
    else:
        print(
            "ОШИБКА: Через 30 секунд желтая карточка сеанса НЕ становится красной (при отсутствии сообщений со стороны Агента) - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator) == True)

    allure.dynamic.description(
        'Карточка нового сеанса зеленая, при отсутствии сообщений со стороны Агента через 30 секунд - желтая, еще через 30  секунд - красная - ТЕСТ УСПЕШНЫЙ!!!')

    app.logout_agent()
    print("test_change_chat_color_green_yellow_red.py is done successfully")


# Желтая карточка становится зеленой при отправке Агентом сообщения

@allure.title("Желтая карточка становится зеленой при отправке Агентом сообщения")
def test_change_chat_color_yellow_to_green(app):
    print("test_change_chat_color_yellow_to_green.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_completion_chat()
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_" + str(num)
    app.client_send_message(mess_client)
    app.is_client_message_in_ov_chat(mess_client)
    app.logout_client()

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    client_name = "866712#main_autotest"
    app.agent_search_chat(client_name)

    print(str(datetime.datetime.now()))
    locator_green = "//div[@class='Tick SessionRowActive SessionRowGreen']"
    if (app.is_element_present_main(locator_green, wait=1) == True):
        print("Карточка нового сеанса зеленая")
        print(str(datetime.datetime.now()))
    else:
        print("ОШИБКА: Карточка нового сеанса НЕ зеленая!!!")
    assert (app.is_element_present_main(locator_green) == True)
    print("Ожидание 30 сек...")

    time.sleep(30)
    locator_yellow = "//div[@class='Tick SessionRowActive SessionRowYellow']"
    print(str(datetime.datetime.now()))
    if (app.is_element_present_main(locator_yellow, wait=1) == True):
        print("Через 30 секунд зеленая карточка сеанса становится желтой (при отсутствии сообщений со стороны Агента)")
        print(str(datetime.datetime.now()))
    else:
        print(
            "ОШИБКА: Через 30 секунд зеленая карточка сеанса НЕ становится желтой (при отсутствии сообщений со стороны Агента)!!!")
    assert (app.is_element_present_main(locator_yellow) == True)

    mess_agent = "BasicATAgent_" + str(num)
    app.agent_send_message(mess_agent)

    print(str(datetime.datetime.now()))
    if (app.is_element_present_main(locator_green, wait=1) == True and app.is_element_present_main(locator_yellow,
                                                                                                   wait=1) == False):
        print("Желтая карточка становится зеленой при отправке Агентом сообщения - ТЕСТ УСПЕШНЫЙ")
        print(str(datetime.datetime.now()))
    else:
        print("ОШИБКА: Желтая карточка НЕ становится зеленой при отправке Агентом сообщения - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator_green, wait=1) == True)

    allure.dynamic.description('Желтая карточка становится зеленой при отправке Агентом сообщения - ТЕСТ УСПЕШНЫЙ!!!')

    app.logout_agent()
    print("test_change_chat_color_yellow_to_green.py is done successfully")


# Красная карточка становится зеленой при отправке Агентом сообщения

@allure.title("Красная карточка становится зеленой при отправке Агентом сообщения")
def test_change_chat_color_red_to_green(app):
    print("test_change_chat_color_red_to_green.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_completion_chat()
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_" + str(num)
    app.client_send_message(mess_client)
    app.is_client_message_in_ov_chat(mess_client)
    app.logout_client()

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    client_name = "866712#main_autotest"
    app.agent_search_chat(client_name)

    print(str(datetime.datetime.now()))
    locator_green = "//div[@class='Tick SessionRowActive SessionRowGreen']"
    if (app.is_element_present_main(locator_green, wait=1) == True):
        print("Карточка нового сеанса зеленая")
        print(str(datetime.datetime.now()))
    else:
        print("ОШИБКА: Карточка нового сеанса НЕ зеленая!!!")
    assert (app.is_element_present_main(locator_green) == True)
    print("Ожидание 30 сек...")

    time.sleep(30)
    locator_yellow = "//div[@class='Tick SessionRowActive SessionRowYellow']"
    print(str(datetime.datetime.now()))
    if (app.is_element_present_main(locator_yellow, wait=1) == True):
        print("Через 30 секунд зеленая карточка сеанса становится желтой (при отсутствии сообщений со стороны Агента)")
        print(str(datetime.datetime.now()))
    else:
        print(
            "ОШИБКА: Через 30 секунд зеленая карточка сеанса НЕ становится желтой (при отсутствии сообщений со стороны Агента)!!!")
    assert (app.is_element_present_main(locator_yellow) == True)

    time.sleep(30)
    locator_red = "//div[@class='Tick SessionRowActive SessionRowRed']"
    print(str(datetime.datetime.now()))
    if (app.is_element_present_main(locator_red, wait=1) == True):
        print("Через 30 секунд желтая карточка сеанса становится красной (при отсутствии сообщений со стороны Агента)")
        print(str(datetime.datetime.now()))
    else:
        print(
            "ОШИБКА: Через 30 секунд желтая карточка сеанса НЕ становится красной (при отсутствии сообщений со стороны Агента)!!!")
    assert (app.is_element_present_main(locator_red) == True)

    mess_agent = "BasicATAgent_" + str(num)
    app.agent_send_message(mess_agent)

    print(str(datetime.datetime.now()))
    if (app.is_element_present_main(locator_green, wait=1) == True and app.is_element_present_main(locator_yellow,
                                                                                                   wait=1) == False and app.is_element_present_main(
        locator_red, wait=1) == False):
        print("Красная карточка становится зеленой при отправке Агентом сообщения - ТЕСТ УСПЕШНЫЙ")
        print(str(datetime.datetime.now()))
    else:
        print("ОШИБКА: Красная карточка НЕ становится зеленой при отправке Агентом сообщения - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator_green, wait=1) == True)

    allure.dynamic.description('Красная карточка становится зеленой при отправке Агентом сообщения - ТЕСТ УСПЕШНЫЙ!!!')

    app.logout_agent()
    print("test_change_chat_color_red_to_green.py is done successfully")
