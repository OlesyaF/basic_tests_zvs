# -*- encoding: utf-8 -*-

import time

import allure


# Проверка отображения карточки Клиента в АРМ РИЦ

@allure.title("Проверка отображения карточки Клиента в АРМ РИЦ")
def test_client_card(app):
    print("test_client_card.py is running")

    # PRECONDITION: Изменение имени Клиента, получение email и профиля, отправка Клиентом сообщения
    app.go_to_online_version()
    app.login_client()
    client_profile = app.get_profile()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    client_name = "Петрова-Чансю Вероника-АБуака Трезоивна"
    app.changing_client_name(client_name)
    app.save_client_info()
    time.sleep(2)
    app.go_to_client_info()
    if (app.is_element_present_main("//input[@id='FormCustomerFullname' and contains(text(),'" + client_name + "')]") == True):
        print("В ОД имя Клиента совпадает с новым значением")
    else:
        print("ОШИБКА: В ОД имя Клиента не совпадает с новым значением!!!")
    assert (app.is_element_present_main("//input[@id='FormCustomerFullname' and contains(text(),'" + client_name + "')]") == True)
    time.sleep(3)
    client_email = app.get_client_email()
    app.go_out_client_info()
    time.sleep(3)
    num = app.calc_check_sum_from_date()
    mess_client = "BasicATClient_" + str(num)
    app.client_send_message(mess_client)
    app.is_client_message_in_ov_chat(mess_client)
    app.logout_client()

    # TEST
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(10)
    app.agent_search_only_one_chat()
    locator1 = "//strong[contains(text(),'" + client_name + "')]"
    locator2 = "//*[text()='профиль: ']"
    locator3 = "//strong[contains(text(),'" + client_profile + "')]"
    #locator4 = "//div[@class='distr-majorsys' and text()='КонсультантБухгалтер']"
    locator5 = "//*[text()='№']"
    #locator6 = "//span[@class='DistrNo' and contains(text(),'109_866712')]"
    #locator7 = "//*[text()='ОИВ']"
    locator8 = "//strong[text()='" + client_email + "']"

    if (app.is_element_present_main(locator1) == True):
        print("В карточке Клиента имя отображается корректно - ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: В карточке Клиента некорректно отображается имя - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        assert (app.is_element_present_main(locator1) == True)

    # if (app.is_element_present_main(locator2) == True and app.is_element_present_main(
    #         locator3) == True and app.is_element_present_main(locator4) == True):
    #     print("В карточке Клиента профиль отображается корректно - ТЕСТ УСПЕШНЫЙ")
    # else:
    #     print("ОШИБКА: В карточке Клиента некорректно отображается профиль - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    #     assert (app.is_element_present_main(locator2) == True and app.is_element_present_main(
    #         locator3) == True and app.is_element_present_main(locator4) == True)
    #
    # if (app.is_element_present_main(locator5) == True and app.is_element_present_main(locator6) == True):
    #     print("В карточке Клиента номер дистрибутива отображается корректно - ТЕСТ УСПЕШНЫЙ")
    # else:
    #     print("ОШИБКА: В карточке Клиента некорректно отображается номер дистрибутива - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    #     assert (app.is_element_present_main(locator5) == True and app.is_element_present_main(locator6) == True)
    #
    # if (app.is_element_present_main(locator7) == True):
    #     print("В карточке Клиента тип версии отображается корректно - ТЕСТ УСПЕШНЫЙ")
    # else:
    #     print("ОШИБКА: В карточке Клиента некорректно отображается тип версии - ТЕСТ НЕ УСПЕШНЫЙ!!!")
    #     assert (app.is_element_present_main(locator7) == True)

    if (app.is_element_present_main(locator8) == True):
        print("В карточке Клиента email отображается корректно - ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: В карточке Клиента некорректно отображается email - ТЕСТ НЕ УСПЕШНЫЙ!!!")
        assert (app.is_element_present_main(locator8) == True)

    allure.dynamic.description('В карточке Клиента параметры отображаются корректно - ТЕСТ УСПЕШНЫЙ')

    app.logout_agent()
    print("test_client_card.py is done successfully")
