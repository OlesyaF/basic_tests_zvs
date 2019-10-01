# -*- encoding: utf-8 -*-

import allure
import math
import time


# Проверка вкладки 'Настройка доступности сервиса ‎Задать вопрос'

@allure.title("Проверка отображения общего количества комплектов на вкладке 'Настройка доступности сервиса ‎Задать вопрос'")
def test_view_total_kits(app):
    print("test_view_total_kits.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    time.sleep(2)
    total_kits = app.get_total_kits()

    print("Проверка отображения общего количества комплектов на вкладке 'Настройка доступности сервиса ‎Задать вопрос':")
    if (app.is_element_present_main("//div[@class='total fl-lt mr32 f-grey']//strong[@class='value' and text()='" + total_kits + "']") == True):
        print("Общее количество комплектов совпадает")
    else:
        print("ОШИБКА!!! Общее количество комплектов не совпадает!")
        assert (app.is_element_present_main("//div[@class='total fl-lt mr32 f-grey']//strong[@class='value' and text()='" + total_kits + "']") == True)

    app.press_configure()
    app.go_to_filter()
    app.select_show_all()

    print("Проверка отображения общего количества комплектов на вкладке 'Настройка доступности сервиса ‎Задать вопрос' после настройки фильтра:")
    if (app.is_element_present_main("//div[@class='total fl-lt mr32 f-grey']//strong[@class='value' and text()='" + total_kits + "']") == True):
        print("Общее количество комплектов совпадает")
    else:
        print("ОШИБКА!!! Общее количество комплектов не совпадает!")
        assert (app.is_element_present_main("//div[@class='total fl-lt mr32 f-grey']//strong[@class='value' and text()='" + total_kits + "']") == True)

    app.logout_agent()
    print("test_view_total_kits.py is done successfully")


@allure.title("Проверка отображения количества комплектов на сопровождении на вкладке 'Настройка доступности сервиса ‎Задать вопрос'")
def test_view_supp_kits(app):
    print("test_view_supp_kits.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    time.sleep(2)
    total_kits = app.get_total_kits()
    supp_kits = app.get_supported_kits()
    unsupp_kits = str(int(total_kits)-int(supp_kits))
    print("unsupp_kits = ", unsupp_kits)
    app.press_configure()
    app.go_to_filter()
    app.select_show_supported_kits()

    print("Проверка отображения общего количества комплектов на вкладке 'Настройка доступности сервиса ‎Задать вопрос' после настройки фильтра:")
    if (app.is_element_present_main("//div[@class='total fl-lt mr32 f-grey']//strong[@class='value' and text()='" + supp_kits + "']") == True):
        print("Общее количество комплектов совпадает")
    else:
        print("ОШИБКА!!! Общее количество комплектов не совпадает!")
        assert (app.is_element_present_main("//div[@class='total fl-lt mr32 f-grey']//strong[@class='value' and text()='" + supp_kits + "']") == True)

    print("Проверка отображения количества комплектов, отключенных от сопровождения, на вкладке 'Настройка доступности сервиса ‎Задать вопрос' после настройки фильтра:")
    if (app.is_element_present_main("//div[@class='unsupported f-orange']//span[@class='value' and text()='0']") == True):
        print("Количество комплектов, отключенных от сопровождения, совпадает")
    else:
        print("ОШИБКА!!! Количество комплектов, отключенных от сопровождения, не совпадает!")
        assert (app.is_element_present_main("//div[@class='unsupported f-orange']//span[@class='value' and text()='0']") == True)

    app.logout_agent()
    print("test_view_supp_kits.py is done successfully")

@allure.title("Проверка отображения количества комплектов, отключенных от сопровождения, на вкладке 'Настройка доступности сервиса ‎Задать вопрос'")
def test_view_unsupp_kits(app):
    print("test_view_unsupp_kits.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    time.sleep(2)
    total_kits = app.get_total_kits()
    supp_kits = app.get_supported_kits()
    unsupp_kits = str(int(total_kits)-int(supp_kits))
    print("unsupp_kits = ", unsupp_kits)

    print("Проверка отображения количества комплектов, отключенных от сопровождения, на вкладке 'Настройка доступности сервиса ‎Задать вопрос':")
    if (app.is_element_present_main("//div[@class='unsupported f-orange']//span[@class='value' and text()='" + unsupp_kits + "']") == True):
        print("Количество комплектов, отключенных от сопровождения, совпадает")
    else:
        print("ОШИБКА!!! Количество комплектов, отключенных от сопровождения, не совпадает!")
        assert (app.is_element_present_main("//div[@class='unsupported f-orange']//span[@class='value' and text()='" + unsupp_kits + "']") == True)

    app.press_configure()
    app.go_to_filter()
    app.select_show_unsupported_kits()

    print("Проверка отображения общего количества комплектов на вкладке 'Настройка доступности сервиса ‎Задать вопрос' после настройки фильтра:")
    if (app.is_element_present_main("//div[@class='total fl-lt mr32 f-grey']//strong[@class='value' and text()='" + unsupp_kits + "']") == True):
        print("Общее количество комплектов совпадает")
    else:
        print("ОШИБКА!!! Общее количество комплектов не совпадает!")
        assert (app.is_element_present_main("//div[@class='total fl-lt mr32 f-grey']//strong[@class='value' and text()='" + unsupp_kits + "']") == True)

    print("Проверка отображения количества комплектов, отключенных от сопровождения, на вкладке 'Настройка доступности сервиса ‎Задать вопрос' после настройки фильтра:")
    if (app.is_element_present_main("//div[@class='unsupported f-orange' and @style='display: none;']") == True):
        print("Количество комплектов, отключенных от сопровождения, совпадает")
    else:
        print("ОШИБКА!!! Количество комплектов, отключенных от сопровождения, не совпадает!")
        assert (app.is_element_present_main("//div[@class='unsupported f-orange' and @style='display: none;']") == True)

    app.logout_agent()
    print("test_view_unsupp_kits.py is done successfully")

@allure.title("Проверка отображения количества неподключенных комплектов на вкладке 'Настройка доступности сервиса ‎Задать вопрос'")
def test_view_unconn_kits(app):
    print("test_view_unconn_kits.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    time.sleep(2)
    unconn_kits = app.get_unconnected_kits()

    app.press_configure()
    app.go_to_filter()
    app.select_show_hotline_off_kits()
    app.select_show_expcons_off_kits()

    print("Проверка отображения общего количества комплектов на вкладке 'Настройка доступности сервиса ‎Задать вопрос' после настройки фильтра:")
    if (app.is_element_present_main("//div[@class='total fl-lt mr32 f-grey']//strong[@class='value' and text()='" + unconn_kits + "']") == True):
        print("Общее количество комплектов совпадает")
    else:
        print("ОШИБКА!!! Общее количество комплектов не совпадает!")
        assert (app.is_element_present_main(
            "//div[@class='total fl-lt mr32 f-grey']//strong[@class='value' and text()='" + unconn_kits + "']") == True)

    app.logout_agent()
    print("test_view_unconn_kits.py is done successfully")


@allure.title("Проверка расстраничивания на вкладке 'Настройка доступности сервиса ‎Задать вопрос'")
def test_page_settings(app):
    print("test_page_settings.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    time.sleep(2)
    total_kits = app.get_total_kits()
    pages_10 = math.ceil(int(total_kits)/10)
    pages_10_fail = pages_10 + 1
    print("pages_10 = ", pages_10)
    pages_50 = math.ceil(int(total_kits)/50)
    pages_50_fail = pages_50 + 1
    print("pages_50 = ", pages_50)
    pages_100 = math.ceil(int(total_kits)/100)
    pages_100_fail = pages_100 + 1
    print("pages_100 = ", pages_100)

    print("Проверка расстраничивания на вкладке 'Настройка доступности сервиса ‎Задать вопрос' (шаг=10):")
    if ((app.is_element_present_main("//a[@href='#' and @title='Показать страницу " + str(pages_10) + "']") == True) and (app.is_element_present_main("//a[@href='#' and @title='Показать страницу " + str(pages_10_fail) + "']") == False)):
        print("При шаге = 10", total_kits, "комплекта отображается на", pages_10, "страницах")
    else:
        print("ОШИБКА!!! При шаге = 10 расстраничивание не корректно!")
        assert ((app.is_element_present_main("//a[@href='#' and @title='Показать страницу " + str(pages_10) + "']") == True) and (app.is_element_present_main("//a[@href='#' and @title='Показать страницу " + str(pages_10_fail) + "']") == False))

    app.show_50_kits()

    print(
        "Проверка расстраничивания на вкладке 'Настройка доступности сервиса ‎Задать вопрос' (шаг=50):")
    if ((app.is_element_present_main(
            "//a[@href='#' and @title='Показать страницу " + str(pages_50) + "']") == True) and (
            app.is_element_present_main(
                    "//a[@href='#' and @title='Показать страницу " + str(pages_50_fail) + "']") == False)):
        print("При шаге = 50", total_kits, "комплекта отображается на", pages_50, "страницах")
    else:
        print("ОШИБКА!!! При шаге = 50 расстраничивание не корректно!")
        assert ((app.is_element_present_main(
            "//a[@href='#' and @title='Показать страницу " + str(pages_50) + "']") == True) and (
                            app.is_element_present_main(
                                "//a[@href='#' and @title='Показать страницу " + str(pages_50_fail) + "']") == False))

    app.show_100_kits()

    print(
        "Проверка расстраничивания на вкладке 'Настройка доступности сервиса ‎Задать вопрос' (шаг=100):")
    if ((app.is_element_present_main(
            "//a[@href='#' and @title='Показать страницу " + str(pages_100) + "']") == True) and (
            app.is_element_present_main(
                    "//a[@href='#' and @title='Показать страницу " + str(pages_100_fail) + "']") == False)):
        print("При шаге = 100", total_kits, "комплекта отображается на", pages_100, "страницах")
    else:
        print("ОШИБКА!!! При шаге = 100 расстраничивание не корректно!")
        assert ((app.is_element_present_main(
            "//a[@href='#' and @title='Показать страницу " + str(pages_100) + "']") == True) and (
                            app.is_element_present_main(
                                "//a[@href='#' and @title='Показать страницу " + str(pages_100_fail) + "']") == False))

    app.logout_agent()
    print("test_page_settings.py is done successfully")


@allure.title("Проверка изменения доступности ОД у случайного комплекта на вкладке 'Настройка доступности сервиса ‎Задать вопрос'")
def test_change_hotline(app):
    print("test_change_hotline.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    app.go_to_service_settings()
    time.sleep(2)
    app.press_configure()
    app.go_to_filter()
    app.select_show_hotline_off_kits()
    print("Настройка фильтра: показать комплекты с выключенным ОД")
    time.sleep(2)
    before_selected_kits = app.get_selected_kits()


    if int(before_selected_kits) == 0:
        print("Комплекты с выключенным ОД не найдены")
        app.go_to_service_settings()
        time.sleep(2)
        app.press_configure()
        app.go_to_filter()
        app.select_show_hotline_kits()
        print("Настройка фильтра: показать комплекты с включенным ОД")
        time.sleep(2)
        before_selected_kits = app.get_selected_kits()
        if int(before_selected_kits) == 0:
            print("Не найдены комплекты ни с выключенным, ни с включенным ОД!")
        elif (int(before_selected_kits) > 0 and int(before_selected_kits) <= 100):
            app.show_100_kits()
            time.sleep(2)
            before_len_list_kits = app.get_len_list_kits()
            app.reconn_hotline()
            print("Случайному комплекту добавлен доступ к ОД")
            app.save_setting_checkbox()
            time.sleep(2)
            after_len_list_kits = app.get_len_list_kits()
            if (int(before_len_list_kits) == after_len_list_kits + 1):
                print("Количество комплектов, отображающихся после включения ОД (", after_len_list_kits,
                      "), на 1 меньше, количества комплектов, отображавшихся до включения ОД (", before_len_list_kits,
                      ")")
            else:
                print("ОШИБКА!!! Количество отображающихся комплектов некорректно: после включения ОД -",
                      after_len_list_kits, ", до включения ОД -", before_len_list_kits)
                assert (int(before_len_list_kits) == after_len_list_kits + 1)
        else:
            print("Найдено более 100 комплектов с включенным ОД!")
    elif (int(before_selected_kits) > 0 and int(before_selected_kits) <= 100):
        app.show_100_kits()
        time.sleep(2)
        before_len_list_kits = app.get_len_list_kits()
        app.reconn_hotline()
        print("У случайного комплекта удален доступ к ОД")
        app.save_setting_checkbox()
        time.sleep(2)
        after_len_list_kits = app.get_len_list_kits()
        if (int(before_len_list_kits) == after_len_list_kits + 1):
            print("Количество комплектов, отображающихся после отключения ОД (", after_len_list_kits, "), на 1 меньше, количества комплектов, отображавшихся до отключения ОД (", before_len_list_kits, ")")
        else:
            print("ОШИБКА!!! Количество отображающихся комплектов некорректно: после отключения ОД -", after_len_list_kits, ", до отключения ОД -", before_len_list_kits)
            assert (int(before_len_list_kits) == after_len_list_kits + 1)
    else:
        print("Найдено более 100 комплектов с выключенным ОД!")

    app.logout_agent()
    print("test_change_hotline.py is done successfully")