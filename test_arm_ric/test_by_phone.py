# -*- encoding: utf-8 -*-

import time
import allure


# Проверка изменения контактных данных о РИЦ на вкладке По телефону

@allure.title("Проверка изменения контактных данных о РИЦ на вкладке По телефону")
def test_by_phone(app):
    print("test_by_phone.py is running")

    contact_info1 = "RIC autotest contact info (part 1) " + str(app.calc_check_sum_from_date())
    contact_info2 = "RIC autotest contact info (part 2) " + str(app.calc_check_sum_from_date())

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_by_phone()
    app.change_ric_info(contact_info1, contact_info2)
    app.logout_agent()

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.click_by_phone()

    print("Проверка отображения в Чате ОВ контактной информации о РИЦ:")
    if (app.is_element_present_main("//*[contains(text(),'" + contact_info1 + "')]") == True and app.is_element_present_main("//*[contains(text(),'" + contact_info2 + "')]") == True):
        print("Измененная контактная информация РИЦ корректно отображается на вкладке 'Горячая линия/Контактная информация РИЦ' ОВ")
    else:
        print("ОШИБКА!!!Информация о РИЦ после изменения не корректно отображается на вкладке 'Горячая линия/Контактная информация РИЦ' ОВ!")
        time.sleep(20)
        assert (app.is_element_present_main("//*[contains(text(),'" + contact_info1 + "')]") == True and app.is_element_present_main("//*[contains(text(),'" + contact_info2 + "')]") == True)

    #//*[@id="ContactInfo"]/div/div[1]/div[2]/text()[2]
    print("test_by_phone.py is done successfully")