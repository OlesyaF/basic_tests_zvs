# -*- encoding: utf-8 -*-

import time
import allure
import pytest


# Проверка быстрых ответов

@allure.title("Проверка добавления быстрого ответа")
# @pytest.mark.skip(reason='This test is skipped as it is not need!')
def test_add_fast_answer(app):
    print("test_add_fast_answer.py is running")

    fast_answer = "Быстрый ответ #" + str(app.calc_check_sum_from_date()) + "(autotest)"

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_fast_answers()
    app.add_fast_answer(fast_answer)
    app.logout_agent()

    print("test_add_fast_answer.py is done successfully")


@allure.title("Проверка удаления быстрого ответа")
# @pytest.mark.skip(reason='This test is skipped as it is not need!')
def test_delete_fast_answer(app):
    print("test_delete_fast_answer.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_fast_answers()
    app.delete_fast_answer()
    app.logout_agent()

    print("test_delete_fast_answer.py is done successfully")


@allure.title("Проверка удаления быстрого ответа")
# @pytest.mark.skip(reason='This test is skipped as it is not need!')
def test_delete_fast_answer(app):
    print("test_delete_fast_answer.py is running")

    app.go_to_arm_ric()
    app.login_agent()
    time.sleep(7)
    app.go_to_fast_answers()
    app.delete_fast_answer()
    app.logout_agent()

    print("test_delete_fast_answer.py is done successfully")
