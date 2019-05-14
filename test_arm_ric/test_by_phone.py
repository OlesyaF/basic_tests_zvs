# -*- encoding: utf-8 -*-

import time
import allure


# Проверка изменения информации о Горячей линии РИЦ на вкладке По телефону

@allure.title("Проверка изменения информации о Горячей линии РИЦ на вкладке По телефону")
def test_change_hotline_info(app):
    print("test_change_hotline_info.py is running")

    num = str(app.calc_check_sum_from_date())

    hotline_info1 = "RIC autotest contact info (part 1) " + num
    hotline_info2 = "RIC autotest contact info (part 2) " + num
    hotline_info = str(hotline_info1 + hotline_info2)

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_by_phone()
    time.sleep(2)
    app.change_ric_info(hotline_info1, hotline_info2)
    app.go_to_by_phone()
    hotline_info_form = app.get_hotline_info_arm_ric()

    print("Информация о Горячей линии РИЦ, отображающаяся на вкладке По телефону:", hotline_info_form)
    print("Новая информация о Горячей линии РИЦ:", hotline_info)

    if (hotline_info_form == hotline_info):
        print("Измененная информация о Горячей линии РИЦ корректно отображается на вкладке По телефону")
    else:
        print("ОШИБКА!!! Измененная информации о Горячей линии РИЦ не корректно отображается на вкладке По телефону!")
        assert (hotline_info_form == hotline_info)

    app.logout_agent()

    print("test_change_hotline_info.py is done successfully")
