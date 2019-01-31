# -*- encoding: utf-8 -*-

import time


# Изменение email клиента (негативный тест): нельзя сохранить поле 'Email' незаполненным

def test_changing_client_email_nt1(app):
    locator1 = "//div[contains(@class, 'FormCustomerEmailError') and contains(text(),'Заполните это поле')]"
    locator2 = "//input[@id='FormCustomerEmail'][@placeholder='Введите Ваш email']"

    print("changing_client_email_nt1.py is running")

    app.go_to_online_version(ov_link="https://login.consultant.ru")
    app.login_client(client_name="866712#autotest4", client_password="cDKgrqe7")
    app.go_to_online_dialog()
    time.sleep(7)
    app.go_to_client_info()
    time.sleep(2)
    app.changing_client_email(email="")
    if (app.is_element_present_main(locator1) == True and app.is_element_present_main(locator2) == True):
        print(
            "Нельзя сохранить пустой email Клиента (в поле 'Email' отображается 'Введите Ваш email', "
            "под полем 'Email' - 'Заполните это поле', после нажатия на 'Сохранить' остались в окне 'Изменить контактные данные') "
            "- ТЕСТ УСПЕШНЫЙ")
    else:
        print("ОШИБКА: Не найдено: в поле 'Email' - 'Введите Ваш email', под полем 'Email' - 'Заполните это поле' "
                 "- ТЕСТ НЕ УСПЕШНЫЙ!!!")
    assert (app.is_element_present_main(locator1) == True and app.is_element_present_main(locator2) == True)

    app.logout_client()
    print("changing_client_email_nt1.py is done successfully")
