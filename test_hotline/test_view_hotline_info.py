# -*- encoding: utf-8 -*-

import time

import allure


# Отображение информации о Горячей линии РИЦ на вкладке "Горячая линия/Контактная информация РИЦ" в окне "Сервис поддержки клиентов"

@allure.title(
    "Отображение информации о Горячей линии РИЦ на вкладке 'Горячая линия/Контактная информация РИЦ' в окне 'Сервис поддержки клиентов'")
def test_view_hotline_info(app):
    print("test_view_hotline_info.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_by_phone()
    hotline_info_arm_ric = app.get_hotline_info_arm_ric()
    print("hotline_info_arm_ric = ", hotline_info_arm_ric)
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.click_by_phone()
    hotline_info_ov = app.get_hotline_info_ov()
    print("hotline_info_ov = ", hotline_info_ov)
    app.logout_client()

    if (hotline_info_arm_ric == hotline_info_ov):
        print(
            "Информация о Горячей линии РИЦ на вкладке 'Горячая линия/Контактная информация РИЦ' в окне 'Сервис поддержки клиентов' в ОВ совпадает с информацией о Горячей линии РИЦ, указанной на вкладке 'По телефону' в АРМ РИЦ")
    else:
        print(
            "ОШИБКА!!! Информация о Горячей линии РИЦ на вкладке 'Горячая линия/Контактная информация РИЦ' в окне 'Сервис поддержки клиентов' в ОВ не совпадает с информацией о Горячей линии РИЦ, указанной на вкладке 'По телефону' в АРМ РИЦ!")
        assert (hotline_info_arm_ric == hotline_info_ov)

    print("test_view_hotline_info.py is done successfully")
