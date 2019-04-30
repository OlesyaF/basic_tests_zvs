# -*- encoding: utf-8 -*-

import time

import allure


# Проверка навигации по меню АРМ РИЦ

@allure.title("Проверка перехода на вкладку По телефону")
def test_go_by_phone(app):
    print("test_go_by_phone.py is running")
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_by_phone()
    app.logout_agent()
    print("test_go_by_phone.py is done successfully")


@allure.title("Проверка перехода на вкладку Онлайн-диалог")
def test_go_online_dialog(app):
    print("test_go_online_dialog.py is running")
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_online_dialog()
    app.logout_agent()
    print("test_go_online_dialog.py is done successfully")


@allure.title("Проверка перехода на вкладку Быстрые ответы")
def test_go_fast_answers(app):
    print("test_go_fast_answers.py is running")
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_fast_answers()
    app.logout_agent()
    print("test_go_fast_answers.py is done successfully")


@allure.title("Проверка перехода на вкладку История сеансов общения")
def test_go_history(app):
    print("test_go_history.py is running")
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_history()
    app.logout_agent()
    print("test_go_history.py is done successfully")


@allure.title("Проверка перехода на вкладку Настройки рабочего времени РИЦ")
def test_go_work_time_settings(app):
    print("test_go_work_time_settings.py is running")
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_work_time_settings()
    app.logout_agent()
    print("test_go_work_time_settings.py is done successfully")


@allure.title("Проверка перехода на вкладку Техническая документация")
def test_go_tech_doc(app):
    print("test_go_tech_doc.py is running")
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_tech_doc()
    app.logout_agent()
    print("test_go_tech_doc.py is done successfully")


@allure.title("Проверка перехода на вкладку Отчеты для Лидера РИЦ")
def test_go_reports(app):
    print("test_go_reports.py is running")
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_reports()
    app.logout_agent()
    print("test_go_reports.py is done successfully")


@allure.title("Проверка перехода на вкладку Настройка доступности сервиса Задать вопрос")
def test_go_service_settings(app):
    print("test_go_service_settings.py is running")
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_service_settings()
    app.logout_agent()
    print("test_go_service_settings.py is done successfully")


@allure.title("Проверка перехода на вкладку Информация для кнопки Сервисный центр")
def test_go_info_service_center(app):
    print("test_go_info_service_center.py is running")
    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_info_service_center()
    app.logout_agent()
    print("test_go_info_service_center.py is done successfully")
