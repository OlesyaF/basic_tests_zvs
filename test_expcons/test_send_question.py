# -*- encoding: utf-8 -*-

import time
import allure


# Проверка отправка Клиентом вопроса эксперту

@allure.title("Проверка отправка Клиентом вопроса эксперту")
def test_send_question(app):
    print("test_send_question.py is running")

    app.go_to_online_version()
    app.login_client()
    app.go_to_customer_support_service()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    client_name = app.get_client_name()
    client_email = app.get_client_email()
    client_phone = app.get_client_phone()
    time.sleep(2)
    app.go_to_expcons()
    question_client = str(app.calc_check_sum_from_date()) + "#question"
    print("question_client: ", question_client)
    app.client_send_question(question_client)
    app.check_expcons_after_question(question_client, client_name, client_email, client_phone)
    app.logout_client()
    print("test_send_question.py is done successfully")
