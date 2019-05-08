# -*- encoding: utf-8 -*-

import time
import allure


# Проверка изменения информации о Горячей линии РИЦ на вкладке По телефону

@allure.title("Проверка изменения информации о Горячей линии РИЦ на вкладке По телефону")
def test_change_hotline_info(app):
    print("test_change_hotline_info.py is running")

    hotline_info1 = "RIC autotest contact info (part 1) " + str(app.calc_check_sum_from_date())
    hotline_info2 = "RIC autotest contact info (part 2) " + str(app.calc_check_sum_from_date())
    hotline_info = str(hotline_info1 + hotline_info2)
    print("Новая информация о Горячей линии РИЦ: ", hotline_info)

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_by_phone()
    app.change_ric_info(hotline_info1, hotline_info2)
    app.go_to_by_phone()

    print("app.get_hotline_info_arm_ric()=", app.get_hotline_info_arm_ric())
    print("hotline_info=", hotline_info)

    if (app.get_hotline_info_arm_ric() == hotline_info):
        print("Измененная информация о Горячей линии РИЦ корректно отображается на вкладке По телефону")
    else:
        print("ОШИБКА!!! Измененная информации о Горячей линии РИЦ не корректно отображается на вкладке По телефону!")
        assert (app.get_hotline_info_arm_ric() == hotline_info)

    app.logout_agent()

    print("test_change_hotline_info.py is done successfully")
