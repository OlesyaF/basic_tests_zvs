# -*- encoding: utf-8 -*-

import datetime
import random
import re
import time
import allure
from winreg import *
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# noinspection PyDeprecation
class Application:

    def __init__(self, ov_url, client_login, client_password, arm_ric_url, agent_login, agent_password, browser,
                 resource, kit):
        if browser == "chrome":
            self.driver = webdriver.Chrome()

        elif browser == "firefox":
            self.driver = webdriver.Firefox()

        elif browser == "opera":
            self.driver = webdriver.Opera()

        elif browser == "ie":

            # Отключение проверки защищенности зон Интернета через Capabilities не работает
            # (from selenium.webdriver.common.desired_capabilities import DesiredCapabilities)
            # cap = DesiredCapabilities().INTERNETEXPLORER.copy()
            # cap['ignoreProtectedModeSettings'] = True
            # cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
            # cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
            # self.driver = webdriver.Ie(capabilities=cap)

            # Включаем защищенный режим для всех зон Интернета (тоже странно работает):
            try:
                keyVal = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\1'
                key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
                SetValueEx(key, "2500", 0, REG_DWORD, 0)
                print("Включен защищенный режим для всех зон Интернета")
            except Exception:
                print("Ошибка включения защищенного режима для всех зон Интернета!!!")

            self.driver = webdriver.Ie()

        elif browser == "edge":
            self.driver = webdriver.Edge()

        else:
            raise ValueError("Неизвестный браузер %s" % browser)

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.ov_url = ov_url
        self.client_login = client_login
        self.client_password = client_password
        self.arm_ric_url = arm_ric_url
        self.agent_login = agent_login
        self.agent_password = agent_password
        self.resource = resource
        self.kit = kit
        self.browser = browser

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    # ОНЛАЙН_ВЕРСИЯ: КЛИЕНТ

    @allure.step('Онлайн-версия: Вход')
    def go_to_online_version(self):
        driver = self.driver
        ov_url = self.ov_url
        resource = self.resource
        if resource == "zv":
            driver.get(ov_url)
            if (self.is_element_present(driver, "//*[@id='logout']/div[1]") == True):
                print("ОВ доступна. Клиент авторизован. Видимо, предыдущий тест упал.")
                # Нажатие на кнопку "Выйти"
                button_logout = driver.find_element_by_xpath("//*[@id='logout']/div[1]")
                button_logout.click()
                # Переход во фрейм "Вы действительно хотите выйти из системы?"
                logout_frame = driver.find_element_by_css_selector("#dialogFrame1 iframe")
                driver.switch_to.frame(logout_frame)
                logout_confirm = driver.find_element_by_css_selector(
                    "#confirm > table > tbody > tr:nth-child(2) > td:nth-child(1) > button > span")
                logout_confirm.click()
                if (self.is_element_present(driver, "//input[@id='loginform-password']") == True):
                    print("Клиент вышел из ОВ")
                else:
                    print("ОШИБКА!!! Поле для ввода пароля не найдено. Клиент не разлогинился!")
                    assert (self.is_element_present(driver, "//input[@id='loginform-password']") == True)
            if (self.is_element_present(driver, "//input[@id='loginform-password']") == True):
                print("ОВ доступна")
            else:
                print("ОШИБКА!!! Онлайн Версия не доступна! - Не найдено поле 'Логин' для авторизации")
                assert (self.is_element_present(driver, "//input[@id='loginform-login']") == True)
        elif resource == "dt":
            driver.get(ov_url)
            if (self.is_element_present(driver, "//*[@id='logout']/div[1]") == True):
                print("ОВ доступна. Клиент авторизован. Видимо, предыдущий тест упал.")
                # Нажатие на кнопку "Выйти"
                button_logout = driver.find_element_by_xpath("//*[@id='logout']/div[1]")
                button_logout.click()
                # Переход во фрейм "Вы действительно хотите выйти из системы?"
                logout_frame = None
                if (self.is_element_present(driver, "//iframe[@name='dialogFrame2']") == True):
                    logout_frame = driver.find_element_by_xpath("//iframe[@name='dialogFrame2']")
                elif (self.is_element_present(driver, "//iframe[@name='dialogFrame1']") == True):
                    logout_frame = driver.find_element_by_xpath("//iframe[@name='dialogFrame1']")
                else:
                    print("ОШИБКА!!! Фрейм 'Вы действительно хотите выйти из системы?' не найден!")
                    assert (logout_frame != None)
                driver.switch_to.frame(logout_frame)
                logout_confirm = driver.find_element_by_css_selector(
                    "#confirm > table > tbody > tr:nth-child(2) > td:nth-child(1) > button > span")
                logout_confirm.click()
                if (self.is_element_present(driver, "//input[@id='login']") == True):
                    print("Клиент вышел из ОВ")
                else:
                    print("ОШИБКА!!! Поле для ввода пароля не найдено. Клиент не разлогинился!")
                    assert (self.is_element_present(driver, "//input[@id='login']") == True)
            if (self.is_element_present(driver, "//input[@id='login']") == True):
                print("ОВ доступна")
            else:
                print("ОШИБКА!!! Онлайн Версия не доступна! - Не найдено поле 'Логин' для авторизации")
                assert (self.is_element_present(driver, "//input[@id='login']") == True)
        else:
            raise ValueError("Неизвестный ресурс %s" % resource)

    @allure.step('Онлайн-версия: Авторизация')
    def login_client(self):
        driver = self.driver
        client_login = self.client_login
        client_password = self.client_password
        resource = self.resource
        if resource == "zv":
            input_field_login = driver.find_element_by_id("loginform-login")
            input_field_login.send_keys(client_login)
            input_field_password = driver.find_element_by_id("loginform-password")
            input_field_password.send_keys(client_password)
            button_login = driver.find_element_by_id("buttonLogin")
            button_login.click()
            if (self.is_element_present(driver, "//div[@id='logout']") == True):
                print("Клиент залогинился в ОВ")
            else:
                print("ОШИБКА!!! Клиент не залогинился в ОВ! - Не найдена кнопка 'Выйти'")
                assert (self.is_element_present(driver, "//div[@id='logout']") == True)
        elif resource == "dt":
            input_field_login = driver.find_element_by_id("login")
            input_field_login.send_keys(client_login)
            input_field_password = driver.find_element_by_id("pwd")
            input_field_password.send_keys(client_password)
            button_login = driver.find_element_by_id("btnOk")
            button_login.click()
            if (self.is_element_present(driver, "//div[@id='logout']") == True):
                print("Клиент залогинился в ОВ")
            else:
                print("ОШИБКА!!! Клиент не залогинился в ОВ! - Не найдена кнопка 'Выйти'")
                assert (self.is_element_present(driver, "//div[@id='logout']") == True)
            time.sleep(5)

    @allure.step('Онлайн-версия: Переход в окно сервиса Задать вопрос (окно "Сервис поддержки клиентов")')
    def go_to_customer_support_service(self):
        driver = self.driver
        button_zv = driver.find_element_by_xpath("//div[@class='topToolbar']/div[5]/div[2]")
        button_zv.click()
        # Переход во фрейм серевиса Задать вопрос
        chat = driver.find_element_by_css_selector("#livechat-dialog iframe")
        driver.switch_to.frame(chat)
        print("Клиент перешел в окно 'Сервис поддержки клиентов'")

    @allure.step('Онлайн-версия: Переход в окно сервиса Задать вопрос (нажатие на меню "Задать вопрос")')
    def go_to_customer_support_service_press_button(self):
        driver = self.driver
        button_zv = driver.find_element_by_xpath("//div[@class='topToolbar']/div[5]/div[2]")
        button_zv.click()
        print("Открыто окно 'Сервис поддержки клиентов'")

    @allure.step('Онлайн-версия: Переход в окно сервиса Задать вопрос (переход во фрейм серевиса Задать вопрос)')
    def go_to_customer_support_service_go_frame(self):
        driver = self.driver
        chat = driver.find_element_by_css_selector("#livechat-dialog iframe")
        driver.switch_to.frame(chat)
        print("Клиент перешел в окно 'Сервис поддержки клиентов'")

    @allure.step('Онлайн-версия: Переход в окно "Изменить контактные данные"')
    def go_to_client_info(self):
        driver = self.driver
        button_client_info = driver.find_element_by_css_selector("div.authEdit.ChangeUserInfo")
        button_client_info.click()
        if (self.is_element_present(driver,
                                    "//div[contains(@class, 'UserInfoHeader') and contains(text(),'Изменить контактные данные')]") == True):
            print("Клиент перешел в окно 'Изменить контактные данные'")
        else:
            print("ОШИБКА!!! Клиент не перешел в окно 'Изменить контактные данные'! - Не найдено название окна")
            assert (self.is_element_present(driver,
                                            "//div[contains(@class, 'UserInfoHeader') and contains(text(),'Изменить контактные данные')]") == True)

    @allure.step('Онлайн-версия: Нажатие кнопки "Сохранить" в окне "Изменить контактные данные"')
    def save_client_info(self):
        driver = self.driver
        button_submit = driver.find_element_by_id("CustomerDataSubmit")
        button_submit.click()
        print("Нажата кнопка 'Сохранить'")

    @allure.step('Онлайн-версия: Изменение имени Клиента')
    def changing_client_name(self, client_name):
        driver = self.driver
        input_field_name = driver.find_element_by_id("FormCustomerFullname")
        input_field_name.click()
        input_field_name.clear()
        input_field_name.send_keys(client_name)
        print("В поле 'Имя' введено новое значение")

    @allure.step('Онлайн-версия: Изменение email Клиента')
    def changing_client_email(self, email):
        driver = self.driver
        input_field_name = driver.find_element_by_id("FormCustomerEmail")
        input_field_name.click()
        input_field_name.clear()
        input_field_name.send_keys(email)
        print("В поле 'Email' введено новое значение")

    @allure.step('Онлайн-версия: Изменение номера телефона Клиента')
    def changing_client_phone(self, phone):
        driver = self.driver
        input_field_name = driver.find_element_by_id("FormCustomerPhone")
        input_field_name.click()
        input_field_name.clear()
        input_field_name.send_keys(Keys.HOME)
        time.sleep(3)
        input_field_name.send_keys(phone)
        print("В поле 'Телефон' введено новое значение")

    @allure.step(
        'Онлайн-версия: Выход из окна сервиса Задать вопрос')  # метод не используется, т.к. в ОВ ДТ не отрабатывает клик по //div[@class='icon livechatclose-16']
    def go_out_customer_support_service(self):
        driver = self.driver
        # Возврат в основной фрейм
        driver.switch_to.parent_frame()
        button_close_chat = driver.find_element_by_xpath("//div[@class='icon livechatclose-16']")
        ActionChains(driver).move_to_element(button_close_chat).click().perform()
        print("Клиент закрыл окно 'Сервис поддержки клиентов'")

    @allure.step('Онлайн-версия: Выход из окна "Изменить контактные данные"')
    def go_out_client_info(self):
        driver = self.driver
        button_close_client_info = driver.find_element_by_xpath("//div[@id='CustomerInfoCancel']")
        button_close_client_info.click()
        if (self.is_element_present(driver, "//textarea[@id='MsgInput']") == True):
            print("Клиент перешел в окно 'Сервис поддержки клиентов'")
        else:
            print(
                "ОШИБКА!!! Клиент НЕ перешел в окно 'Сервис поддержки клиентов' - Не найдено поле для ввода сообщения")
            assert (self.is_element_present(driver, "//textarea[@id='MsgInput']") == True)

    @allure.step('Онлайн-версия: Выход')
    def logout_client(self):
        driver = self.driver
        resource = self.resource
        # Возврат в основной фрейм
        driver.switch_to.parent_frame()
        # Нажатие на кнопку "Выйти"
        button_logout = driver.find_element_by_xpath("//*[@id='logout']/div[1]")
        button_logout.click()
        # Переход во фрейм "Вы действительно хотите выйти из системы?"
        if resource == "zv":
            logout_frame = driver.find_element_by_css_selector("#dialogFrame1 iframe")
            driver.switch_to.frame(logout_frame)
            logout_confirm = driver.find_element_by_css_selector(
                "#confirm > table > tbody > tr:nth-child(2) > td:nth-child(1) > button > span")
            logout_confirm.click()
            if (self.is_element_present(driver, "//input[@id='loginform-password']") == True):
                print("Клиент вышел из ОВ")
            else:
                print("ОШИБКА!!! Поле для ввода пароля не найдено. Клиент не разлогинился!")
                assert (self.is_element_present(driver, "//input[@id='loginform-password']") == True)
        elif resource == "dt":
            logout_frame = None
            if (self.is_element_present(driver, "//iframe[@name='dialogFrame2']") == True):
                logout_frame = driver.find_element_by_xpath("//iframe[@name='dialogFrame2']")
            elif (self.is_element_present(driver, "//iframe[@name='dialogFrame1']") == True):
                logout_frame = driver.find_element_by_xpath("//iframe[@name='dialogFrame1']")
            else:
                print("ОШИБКА!!! Фрейм 'Вы действительно хотите выйти из системы?' не найден!")
                assert (logout_frame != None)
            driver.switch_to.frame(logout_frame)
            logout_confirm = driver.find_element_by_css_selector(
                "#confirm > table > tbody > tr:nth-child(2) > td:nth-child(1) > button > span")
            logout_confirm.click()
            if (self.is_element_present(driver, "//input[@id='login']") == True):
                print("Клиент вышел из ОВ")
            else:
                print("ОШИБКА!!! Поле для ввода пароля не найдено. Клиент не разлогинился!")
                assert (self.is_element_present(driver, "//input[@id='login']") == True)

    @allure.step('Онлайн-версия: Переход на вкладку "Написать эксперту" в окне "Сервис поддержки клиентов"')
    def go_to_expcons(self):
        driver = self.driver
        button_expcons = driver.find_element_by_xpath("//div[contains(text(),'Написать эксперту')]")
        button_expcons.click()
        print("Клиент перешел на вкладку 'Написать эксперту' в окне 'Сервис поддержки клиентов'")

    @allure.step(
        'Онлайн-версия: Переход на вкладку "Горячая линия/Контактная информация РИЦ" в окне "Сервис поддержки клиентов"')
    def click_by_phone(self):
        driver = self.driver
        button_byphone = driver.find_element_by_xpath("//div[@id='tabLabelPhone']")
        button_byphone.click()
        print("Клиент перешел на вкладку 'Горячая линия/Контактная информация РИЦ' в окне 'Сервис поддержки клиентов'")

    @allure.step('Онлайн-версия: Проверка доступности сервиса Онлайн-диалог в окне "Сервис поддержки клиентов"')
    def check_hotline_availability(self):
        driver = self.driver
        print("Проверка доступности сервиса Онлайн-диалог:")
        if (self.is_element_present(driver, "//div[@class='message_log']") == True):
            print("1. Блок для отображения сообщений чата присутствует")
        else:
            print("ОШИБКА!!! Блок для отображения сообщений чата отсутствует!")
            assert (self.is_element_present(driver, "//div[@class='message_log']") == True)
        if (self.is_element_present(driver, "//textarea[@id='MsgInput']") == True):
            print("2. Поле для ввода сообщения присутствует")
        else:
            print("ОШИБКА!!! Поле для ввода сообщения отсутствует!")
            assert (self.is_element_present(driver, "//textarea[@id='MsgInput']") == True)
        if (self.is_element_present(driver, "//div[@id='ChatMsgSubmit']") == True):
            print("3. Кнопка для отправки сообщения присутствует")
        else:
            print("ОШИБКА!!! Кнопка для отправки сообщения отсутствует!")
            assert (self.is_element_present(driver, "//div[@id='ChatMsgSubmit']") == True)
        print("Сервис Онлайн-диалог доступен")

    @allure.step('Онлайн-версия: Проверка доступности сервиса Написать эксперту в окне "Сервис поддержки клиентов"')
    def check_expcons_availability(self):
        driver = self.driver
        print("Проверка доступности сервиса Написать эксперту:")
        if (self.is_element_present(driver,
                                    "//span[contains(@class, 'SmallSpace tabTextTitle') and contains(text(),'Здесь Вы можете написать и отправить свой вопрос')]") == True):
            print(
                "1. Пояснительный текст ('Здесь Вы можете написать и отправить свой вопрос') присутствует")
        else:
            print(
                "ОШИБКА!!! Пояснительный текст ('Здесь Вы можете написать и отправить свой вопрос') отсутствует!")
            assert (self.is_element_present(driver,
                                            "//span[contains(@class, 'SmallSpace tabTextTitle') and contains(text(),'Здесь Вы можете написать и отправить свой вопрос')]") == True)
        if (self.is_element_present(driver, "//div[@id='ExpconsBody']") == True):
            print("2. Поле для ввода вопроса присутствует")
        else:
            print("ОШИБКА!!! Поле для ввода вопроса отсутствует!")
            assert (self.is_element_present(driver, "div[@id='ExpconsBody']") == True)
        if (self.is_element_present(driver, "//div[@id='ExpconsSubmit']") == True):
            print("3. Кнопка для отправки сообщения присутствует")
        else:
            print("ОШИБКА!!! Кнопка для отправки сообщения отсутствует!")
            assert (self.is_element_present(driver, "//div[@id='ExpconsSubmit']") == True)
        print("Сервис Написать эксперту доступен")

    @allure.step(
        'Онлайн-версия: Проверка вида вкладки "Горячая линия/Контактная информация РИЦ" в окне "Сервис поддержки клиентов"')
    def check_byphone_availability(self):
        driver = self.driver
        print("Проверка вида вкладки 'Горячая линия/Контактная информация РИЦ' в окне 'Сервис поддержки клиентов':")
        if (self.is_element_present(driver, "//div[@class='ContactInfo-Hotline']") == True):
            print("1. Блок с контактами горячей линии присутствует")
        else:
            print("ОШИБКА!!! Блок с контактами горячей линии отсутствует!")
            assert (self.is_element_present(driver, "//div[@class='ContactInfo-Hotline']") == True)
        if (self.is_element_present(driver,
                                    "//div[contains(@class, 'ContactInfoSubtitle') and contains(text(),'ГОРЯЧАЯ ЛИНИЯ')]") == True):
            print("2. Текст 'ГОРЯЧАЯ ЛИНИЯ' присутствует")
        else:
            print("ОШИБКА!!! Текст 'ГОРЯЧАЯ ЛИНИЯ'  отсутствует!")
            assert (self.is_element_present(driver,
                                            "//div[contains(@class, 'ContactInfoSubtitle') and contains(text(),'ГОРЯЧАЯ ЛИНИЯ')]") == True)
        if (self.is_element_present(driver, "//div[@class='ContactInfoCompanyBlock']") == True):
            print("3. Блок с контактной информацией РИЦ присутствует")
        else:
            print("ОШИБКА!!! Блок с контактной информацией РИЦ отсутствует!")
            assert (self.is_element_present(driver, "//div[@class='ContactInfoCompanyBlock']") == True)
        if (self.is_element_present(driver,
                                    "//div[contains(@class, 'ContactInfoSubtitle p16t') and contains(text(),'КОНТАКТНАЯ ИНФОРМАЦИЯ')]") == True):
            print("4. Текст 'КОНТАКТНАЯ ИНФОРМАЦИЯ' присутствует")
        else:
            print("ОШИБКА!!! Текст 'КОНТАКТНАЯ ИНФОРМАЦИЯ' отсутствует!")
            assert (self.is_element_present(driver,
                                            "//div[contains(@class, 'ContactInfoSubtitle p16t') and contains(text(),'КОНТАКТНАЯ ИНФОРМАЦИЯ')]") == True)
        print("Вкладка 'Горячая линия/Контактная информация РИЦ' в окне 'Сервис поддержки клиентов' выглядит корректно")

    @allure.step('Онлайн-версия: Отправка Клиентом сообщения в Чат')
    def client_send_message(self, mess_client):
        driver = self.driver
        input_window = driver.find_element_by_id("MsgInput")
        input_window.send_keys(mess_client)
        button_msg_input = driver.find_element_by_id("ChatMsgSubmit")
        button_msg_input.click()
        print("Клиент отправил в Чат сообщение")

    @allure.step('Онлайн-версия: Проверка отображения отправленного Клиентом сообщения в окне Чата')
    def is_client_message_in_ov_chat(self, mess_client):
        driver = self.driver
        if (self.is_element_present(driver, "//div[contains(text(),'" + mess_client + "')]") == True):
            print("Сообщение, отправленное Клиентом, отображается в теле Чата ОВ")
        else:
            print("ОШИБКА!!! Сообщение, отправленное Клиентом, не отображается в теле Чата ОВ!")
            assert (self.is_element_present(driver, "//div[contains(text(),'" + mess_client + "')]") == True)

    @allure.step('Онлайн-версия: Проверка отображения отправленного Агентом сообщения в окне Чата')
    def is_agent_message_in_ov_chat(self, mess_agent):
        driver = self.driver
        if (self.is_element_present(driver, "//div[contains(text(),'" + mess_agent + "')]") == True):
            print("Сообщение, отправленное Агентом, отображается в теле Чата ОВ")
        else:
            print("ОШИБКА!!! Сообщение, отправленное Агентом, не отображается в теле Чата ОВ!")
            assert (self.is_element_present(driver, "//div[contains(text(),'" + mess_agent + "')]") == True)

    @allure.step('Онлайн-версия: Отправка Клиентом вопроса эксперту')
    def client_send_question(self, question_client):
        driver = self.driver
        input_window = driver.find_element_by_id("ExpconsBody")
        input_window.send_keys(question_client)
        time.sleep(5)
        button_msg_input = driver.find_element_by_id("ExpconsSubmit")
        button_msg_input.click()
        print("Клиент отправил вопрос эксперту")

    @allure.step('Онлайн-версия: Проверка вида вкладки "Написать эксперту" после отправки Клиентом вопроса эксперту')
    def check_expcons_after_question(self, question_client, client_name, client_email, client_phone):
        driver = self.driver

        locator1 = "//div[contains(@class, 'ExpconsResultTitle') and contains(text(),'Спасибо за Ваш вопрос!')]"
        locator2 = "//div[contains(@class, 'ExpconsResultInfoTop p16t p10b') and contains(text(),'Сотрудники Сервисного центра свяжутся с Вами.')]"
        locator3 = "//div[contains(@class, 'ExpconsResultTextBold') and contains(text(),'Текст вопроса')]"
        locator4 = "//textarea[contains(@class, 'ExpconsResultTextArea') and contains(text(),'" + question_client + "')]"
        locator5 = "//span[contains(@class, 'ExpconsResultText') and contains(text(),'" + client_name + "')]"
        locator6 = "//span[contains(@class, 'ExpconsResultText') and contains(text(),'" + client_email + "')]"
        locator7 = "//span[contains(@class, 'ExpconsResultText') and contains(text(),'" + client_phone + "')]"
        locator8 = "//div[contains(@class, 'ExpconsResultInfoBottom p10t') and contains(text(),'Копия вопроса направлена на Ваш email, просим сохранить это письмо.')]"
        locator9 = "//*[contains(text(),'Копия вопроса направлена на Ваш email, просим сохранить это письмо.')]"

        if (self.is_element_present(driver, locator1) == True and self.is_element_present(driver,
                                                                                          locator2) == True and self.is_element_present(
            driver, locator3) == True and self.is_element_present(driver,
                                                                  locator4) == True and self.is_element_present(
            driver, locator5) == True and self.is_element_present(driver,
                                                                  locator6) == True and self.is_element_present(
            driver, locator7) == True and self.is_element_present(driver, locator8) == True and self.is_element_present(
            driver, locator9) == True):
            print("Вид вкладки 'Написать эксперту' после отправки вопроса эксперту корректный")
        else:
            print("ОШИБКА!!! Вид вкладки 'Написать эксперту' после отправки вопроса эксперту НЕ корректный!")
            assert (self.is_element_present(driver, locator1) == True and self.is_element_present(driver,
                                                                                                  locator2) == True and self.is_element_present(
                driver, locator3) == True and self.is_element_present(driver,
                                                                      locator4) == True and self.is_element_present(
                driver, locator5) == True and self.is_element_present(driver,
                                                                      locator6) == True and self.is_element_present(
                driver, locator7) == True and self.is_element_present(driver,
                                                                      locator8) == True and self.is_element_present(
                driver, locator9) == True)

    @allure.step('Онлайн-версия: Получение имени Клиента')
    def get_client_name(self):
        driver = self.driver
        client_name_field = driver.find_element_by_xpath("//input[@id='FormCustomerFullname']")
        client_name = str(client_name_field.get_attribute("value"))
        print("client_name: ", client_name)
        return client_name

    @allure.step('Онлайн-версия: Получение email Клиента')
    def get_client_email(self):
        driver = self.driver
        client_email_field = driver.find_element_by_xpath("//input[@id='FormCustomerEmail']")
        client_email = str(client_email_field.get_attribute("value"))
        print("client_email: ", client_email)
        return client_email

    @allure.step('Онлайн-версия: Получение телефона Клиента')
    def get_client_phone(self):
        driver = self.driver
        client_phone_field = driver.find_element_by_xpath("//input[@id='FormCustomerPhone']")
        client_phone = str(client_phone_field.get_attribute("value"))
        print("client_phone: ", client_phone)
        return client_phone

    @allure.step('Онлайн-версия: Получение профиля Клиента')
    def get_profile(self):
        driver = self.driver
        client_profile = driver.find_element_by_xpath("//span[@class='text']")
        client_profile = str(client_profile.get_attribute("textContent"))
        client_profile = client_profile.replace(" ", "")
        print("client_profile: ", client_profile)
        return client_profile

    @allure.step(
        'Онлайн-версия: Получение информации о Горячей линии РИЦ со вкладки "Горячая линия/Контактная информация РИЦ" в окне "Сервис поддержки клиентов"')
    def get_hotline_info_ov(self):
        driver = self.driver
        # hotline_info = str(driver.find_element_by_xpath("//div[@class='p16t']/div[1]").get_attribute("textContent"))
        hotline_info = str(
            driver.find_element_by_xpath("//*[@id='ContactInfo']/div/div[1]/div[2]").get_attribute("textContent"))
        # //*[@id="ContactInfo"]/div/div[1]/div[2]/text()
        hotline_info = hotline_info.strip()
        hotline_info = re.sub("^\s+|\n|\r|\s+$", "", hotline_info)
        print(
            "Информация о Горячей линии РИЦ со вкладки Горячая линия/Контактная информация РИЦ в окне Сервис поддержки клиентов: ",
            hotline_info)
        return hotline_info

    # АРМ РИЦ: АГЕНТ

    @allure.step('АРМ РИЦ: Вход')
    def go_to_arm_ric(self):
        driver = self.driver
        arm_ric_url = self.arm_ric_url
        driver.get(arm_ric_url)
        if (self.is_element_present(driver, "//*[@id='LogoutButton']") == True):
            print("АРМ РИЦ доступно. Агент авторизован. Видимо, предыдущий тест упал.")
            # Нажатие на кнопку "Выйти", обработка alert
            button_logout = driver.find_element_by_id("LogoutButton")
            button_logout.click()
            try:
                driver.switch_to.alert.accept()
            except:
                NoAlertPresentException
            if (self.is_element_present(driver, "//input[@id='Password']") == True):
                print("Агент вышел из АРМ РИЦ")
            else:
                print("ОШИБКА!!! Поле для ввода пароля не найдено. Агент не разлогинился!")
                assert (self.is_element_present(driver, "//input[@id='Password']") == True)
        if (self.is_element_present(driver, "//input[@id='User']") == True):
            print("АРМ РИЦ доступно")
        else:
            print("ОШИБКА!!! АРМ РИЦ не доступно! - Не найдено поле 'Логин' для авторизации")
            assert (self.is_element_present(driver, "//input[@id='User']") == True)

    @allure.step('АРМ РИЦ: Авторизация (на серверах zv5/zv6)')
    def login_agent(self):
        driver = self.driver
        agent_login = self.agent_login
        agent_password = self.agent_password
        login_field = driver.find_element_by_id("User")
        login_field.send_keys(agent_login)
        password_field = driver.find_element_by_id("Password")
        password_field.send_keys(agent_password)
        button_login = driver.find_element_by_id("LoginButton")
        button_login.click()
        if (self.is_element_present(driver, "//li[@id='nav-Chat']") == True):
            print("Агент залогинился в АРМ РИЦ")
        else:
            button_login = driver.find_element_by_id("LoginButton")
            button_login.click()
            if (self.is_element_present(driver, "//li[@id='nav-Chat']") == True):
                print("Агент залогинился в АРМ РИЦ")
            else:
                print("ОШИБКА!!! Агент не залогинился в АРМ РИЦ - Не найдено меню 'Онлайн-диалог'")
                assert (self.is_element_present(driver, "//li[@id='nav-Chat']") == True)

    @allure.step('АРМ РИЦ: Переход на вкладку Настройка доступности сервиса ‎Задать вопрос')
    def go_to_service_settings(self):
        driver = self.driver
        menu_for_ov = driver.find_element_by_xpath("//li[@id='nav-RICMenu']")
        menu_for_ov.click()
        menu_service_settings = driver.find_element_by_xpath("//li[@id='nav-RICMenu-AgentDistrTabs']")
        menu_service_settings.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        if (self.is_element_present(driver,
                                    "//div[contains(text(),'Настройка доступности сервиса')]") == True and self.is_element_present(
            driver, "//div[@class='button blue fl-lt']") == True):
            print("Агент перешел на вкладку Настройка доступности сервиса ‎Задать вопрос")
        else:
            print("ОШИБКА!!! Агент не перешел на вкладку Настройка доступности сервиса ‎Задать вопрос")
            assert (self.is_element_present(driver,
                                            "//div[contains(text(),'Настройка доступности сервиса')]") == True and self.is_element_present(
                driver, "//div[@class='button blue fl-lt']") == True)

    @allure.step('АРМ РИЦ: Переход на вкладку Информация для кнопки Сервисный центр')
    def go_to_info_service_center(self):
        driver = self.driver
        menu_for_ov = driver.find_element_by_xpath("//li[@id='nav-RICMenu']")
        menu_for_ov.click()
        menu_info_service_center = driver.find_element_by_xpath("//li[@id='nav-RICMenu-AgentDistrContacts']")
        menu_info_service_center.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        if (self.is_element_present(driver,
                                    "//div[@class='title']/div[contains(text(),'Контактная информация о РИЦ')]") == True and self.is_element_present(
            driver, "//div[@class='button blue fl-lt']") == True):
            print("Агент перешел на вкладку Информация для кнопки Сервисный центр")
        else:
            print("ОШИБКА!!! Агент не перешел на вкладку Информация для кнопки Сервисный центрс")
            assert (self.is_element_present(driver,
                                            "//div[@class='title']/div[contains(text(),'Контактная информация о РИЦ')]") == True and self.is_element_present(
                driver, "//div[@class='button blue fl-lt']") == True)

    @allure.step('АРМ РИЦ: Нажатие "Настроить" на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def press_configure(self):
        driver = self.driver
        button_configure = driver.find_element_by_xpath("//div[@class='button blue fl-lt']")
        button_configure.click()

    @allure.step('АРМ РИЦ: Открытие фильтра на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def go_to_filter(self):
        driver = self.driver
        button_filter = driver.find_element_by_xpath("//div[@class='filter-name']")
        button_filter.click()

    @allure.step('АРМ РИЦ: Заполнение фильтра на вкладке Настройка доступности сервиса ‎Задать вопрос (Показать все)')
    def select_show_all(self):
        driver = self.driver
        button_show_all = driver.find_element_by_xpath("//div[@class='submenu']//div[@class='item all']")
        button_show_all.click()

    @allure.step('АРМ РИЦ: Заполнение фильтра на вкладке Настройка доступности сервиса ‎Задать вопрос (Показать комплекты на сопровождении)')
    def select_show_supported_kits(self):
        driver = self.driver
        button_show_supported_kits = driver.find_element_by_xpath("//div[@class='submenu']//div[@class='item unsupported rel']")
        button_show_supported_kits.click()

    @allure.step('АРМ РИЦ: Заполнение фильтра на вкладке Настройка доступности сервиса ‎Задать вопрос (Показать комплекты, отключенные от сопровождения)')
    def select_show_unsupported_kits(self):
        driver = self.driver
        button_show_unsupported_kits = driver.find_element_by_xpath("//div[@class='submenu']//div[@class='item supported rel']")
        button_show_unsupported_kits.click()

    @allure.step('АРМ РИЦ: Заполнение фильтра на вкладке Настройка доступности сервиса ‎Задать вопрос (Показать комплекты, которым недоступен ОД)')
    def select_show_hotline_off_kits(self):
        driver = self.driver
        button_show_hotline_off_kits = driver.find_element_by_xpath("//div[@class='submenu']//div[@class='item hotline-on rel']")
        button_show_hotline_off_kits.click()

    @allure.step('АРМ РИЦ: Заполнение фильтра на вкладке Настройка доступности сервиса ‎Задать вопрос (Показать комплекты, которым недоступно Написать эксперту)')
    def select_show_expcons_off_kits(self):
        driver = self.driver
        button_show_expcons_off_kits = driver.find_element_by_xpath("//div[@class='submenu']//div[@class='item expcons-on rel']")
        button_show_expcons_off_kits.click()

    @allure.step('АРМ РИЦ: Установка шага отображения комплектов =50 на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def show_50_kits(self):
        driver = self.driver
        button_show_50_kits = driver.find_element_by_xpath("//a[@href='#' and @class='pagesize pagesize_50']")
        button_show_50_kits.click()

    @allure.step('АРМ РИЦ: Установка шага отображения комплектов =100 на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def show_100_kits(self):
        driver = self.driver
        button_show_100_kits = driver.find_element_by_xpath("//a[@href='#' and @class='pagesize pagesize_100']")
        button_show_100_kits.click()

    @allure.step('АРМ РИЦ: Поиск комплекта на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def kit_search(self):
        driver = self.driver
        kit = self.kit
        field_kit_list = driver.find_element_by_xpath("//input[@type='text']")
        field_kit_list.click()
        field_kit_list.send_keys(kit)
        field_kit_list.send_keys(Keys.ENTER)
        if (self.is_element_present(driver,
                                    "//div[@class='tab-cell fl-lt tCell Supported' and contains(text(),'" + kit + "')]") == True):
            print("Комплект ", kit, " найден: строка комплекта отображается в результатах поиска")
        else:
            print("ОШИБКА!!! Комплект ", kit, " НЕ найден! - Строка комплекта НЕ отображается в результатах поиска")
            assert (self.is_element_present(driver,
                                            "//div[@class='tab-cell fl-lt tCell Supported' and contains(text(),'" + kit + "')]") == True)

    @allure.step('АРМ РИЦ: Получение id комплекта на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def get_kit_id(self):
        driver = self.driver
        kit = self.kit
        kit_id = driver.find_element_by_xpath(
            "//div[@class='tab-cell fl-lt tCell Supported' and contains(text(),'" + kit + "')]//input[1]").get_attribute(
            "value")
        print("kit_id = ", kit_id)
        return kit_id

    @allure.step('АРМ РИЦ: Получение общего количества комплектов на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def get_total_kits(self):
        driver = self.driver
        total_kits = driver.find_element_by_xpath("//div[@id='stat_total']//div[1]//strong[1]").get_attribute("textContent")
        print("total_kits = ", total_kits)
        return total_kits

    @allure.step('АРМ РИЦ: Получение количества комплектов на сопровождении на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def get_supported_kits(self):
        driver = self.driver
        supp_kits = driver.find_element_by_xpath("//div[@id='stat_supp']//div[1]//strong[1]").get_attribute("textContent")
        print("supp_kits = ", supp_kits)
        return supp_kits

    @allure.step('АРМ РИЦ: Получение количества не подключенных комплектов на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def get_unconnected_kits(self):
        driver = self.driver
        unconn_kits = driver.find_element_by_xpath("//div[@id='stat_unconn']//div[1]//strong[1]").get_attribute("textContent")
        if (unconn_kits is ''):
            print("Неподключенных комплектов = 0")
            unconn_kits = "0"
        else:
            print("Неподключенных комплектов = ", unconn_kits)
        return unconn_kits

    @allure.step('АРМ РИЦ: Получение количества выбранных комплектов на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def get_selected_kits(self):
        driver = self.driver
        selected_kits = driver.find_element_by_xpath("//div[@class='total fl-lt mr32 f-grey']//strong[@class='value']").get_attribute("textContent")
        print("Выбрано комплектов:", selected_kits)
        return selected_kits

    @allure.step('АРМ РИЦ: Получение количества комплектов, отображающихся на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def get_len_list_kits(self):
        driver = self.driver
        elements = driver.find_elements_by_xpath("//div[@class='table-content']//div//div//input[@name='distr_id']")
        len_list_kits = len(elements)
        print("Отображается комплектов:", len_list_kits, " комплектов")
        return len_list_kits

    @allure.step('АРМ РИЦ: Включение ОД у случайного комплекта на вкладке Настройка доступности сервиса ‎Задать вопрос')
    def reconn_hotline(self):
        driver = self.driver
        elements = driver.find_elements_by_xpath("//div[@class='CheckboxBlock']//label[@class='Hotline']")
        random.choice(elements).click()
        print("Случайному комплекту добавлен доступ к ОД")

    @allure.step('АРМ РИЦ: Настройка доступности сервиса ‎Задать вопрос для онлайн-версии (заполнение чек-боксов)')
    def setting_checkbox(self, checkbox_status, checkbox_field, checkbox_click):
        driver = self.driver
        checkbox = driver.find_element_by_xpath(checkbox_field)

        # Через checkbox.get_attribute('checked') - не работает в Edge
        # print("checkbox.get_attribute('checked')=", checkbox.get_attribute('checked'))
        # if (checkbox_status == "off") and (not checkbox.get_attribute('checked')):
        #     print("Чек-бокс в требуемом положении - выключен")
        # if (checkbox_status == "on") and (checkbox.get_attribute('checked') == 'true'):
        #     print("Чек-бокс в требуемом положении - включен")
        # if (checkbox_status == "off") and (checkbox.get_attribute('checked') == 'true'):
        #     driver.find_element_by_xpath(checkbox_click).click()
        #     print("Чек-бокс установлен в требуемое положение: выключен")
        # if (checkbox_status == "on") and (not checkbox.get_attribute('checked')):
        #     driver.find_element_by_xpath(checkbox_click).click()
        #     print("Чек-бокс установлен в требуемое положение: включен")

        if (checkbox_status == "off"):
            if (checkbox.is_selected()):
                driver.find_element_by_xpath(checkbox_click).click()
                print("Чек-бокс установлен в требуемое положение: выключен")
            else:
                print("Чек-бокс в требуемом положении - выключен")
        if (checkbox_status == "on"):
            if (checkbox.is_selected()):
                print("Чек-бокс в требуемом положении - включен")
            else:
                driver.find_element_by_xpath(checkbox_click).click()
                print("Чек-бокс установлен в требуемое положение: включен")

    @allure.step('АРМ РИЦ: Сохранение настроек доступности сервиса ‎Задать вопрос для онлайн-версии')
    def save_setting_checkbox(self):
        driver = self.driver
        button_save = driver.find_element_by_xpath("//div[@class='button blue save fl-rt']")
        button_save.click()
        if (self.is_element_present(driver, "//div[@class='button blue confirm fl-lt']") == True):
            driver.find_element_by_xpath("//div[@class='button blue confirm fl-lt']").click()
        print("Изменения настроек доступности сервиса ‎Задать вопрос для онлайн-версии сохранены")

    @allure.step('АРМ РИЦ: Выход')
    def logout_agent(self):
        driver = self.driver
        # Нажатие на кнопку "Выйти", обработка alert
        button_logout = driver.find_element_by_id("LogoutButton")
        button_logout.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        if (self.is_element_present(driver, "//input[@id='Password']") == True):
            print("Агент вышел из АРМ РИЦ")
        else:
            print("ОШИБКА!!! Поле для ввода пароля не найдено. Агент не разлогинился!")
            assert (self.is_element_present(driver, "//input[@id='Password']") == True)

    @allure.step('АРМ РИЦ: Поиск нужного Чата и подключение к сеансу')
    def agent_search_chat(self):
        driver = self.driver
        client_login = self.client_login
        locator_chat = "//*[text()='" + client_login + "']"
        locator_connect_to_session = "//button[@name='StartChat']"
        i = 0
        if (self.is_element_present(driver, locator_chat) == True):
            print("Агент нашел Чат Клиента среди активных чатов")
        else:
            while (self.is_element_present(driver, locator_connect_to_session) == True):
                connect_to_session_button = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "StartChat")))
                connect_to_session_button.click()
                i += 1
                if (self.is_element_present(driver, locator_chat) == True):
                    print("Агент нашел Чат Клиента в ", i, " очереди")
                    break
        time.sleep(5)
        if (self.is_element_present(driver, locator_chat) != True):
            print("ОШИБКА!!! Чат Клиента не обнаружен ни среди активных чатов, ни в очереди!")
        assert (self.is_element_present(driver, locator_chat) == True)
        # Подключение Агента к Чату
        chat_button = driver.find_element_by_xpath(locator_chat)
        chat_button.click()
        print("Агент подключился к Чату")

    @allure.step('АРМ РИЦ: Подключение ко всем сеансам из очереди')
    def agent_connect_to_all_chat(self):
        driver = self.driver
        locator_connect_to_session = "//button[@name='StartChat']"
        i = 0
        while (self.is_element_visible(driver, locator_connect_to_session) == True):
            connect_to_session_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "StartChat")))
            connect_to_session_button.click()
            i += 1
            time.sleep(5)
        if i > 0:
            print("Агент подключился к", i, "Чатам")
        else:
            print("Агент не подключился ни к одному Чату")

    @allure.step('АРМ РИЦ: Поиск нужного Чата и подключение к сеансу (с завершением всех прочих Чатов)')
    def agent_search_only_one_chat(self):
        driver = self.driver
        client_login = self.client_login
        locator_chat = "//*[text()='" + client_login + "']"
        print("locator_chat = ", locator_chat)
        locator_connect_to_session = "//button[@name='StartChat']"
        i = 0
        if (self.is_element_visible(driver, locator_chat) == True):
            print("Агент нашел Чат Клиента среди активных чатов")
        else:
            print("Агент не нашел Чат Клиента среди активных чатов")
            while (self.is_element_present(driver, locator_connect_to_session) == True):
                connect_to_session_button = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "StartChat")))
                connect_to_session_button.click()
                i += 1
                print("i = ", i)
                time.sleep(5)
                if (self.is_element_present(driver, locator_chat) == True):
                    print("Агент нашел Чат Клиента в ", i, " очереди")
                    break
                else:
                    button_close_chat = driver.find_element_by_xpath(
                        "//button[contains(@name,'CloseSession') and @class='HelperButton']")
                    button_close_chat.click()
                    try:
                        driver.switch_to.alert.accept()
                    except:
                        NoAlertPresentException
                    button_remove_chat = driver.find_element_by_xpath("//button[@class='RemoveSessionRow']")
                    button_remove_chat.click()
                    try:
                        driver.switch_to.alert.accept()
                    except:
                        NoAlertPresentException
        time.sleep(5)
        if (self.is_element_present(driver, locator_chat) != True):
            print("ОШИБКА!!! Чат Клиента не обнаружен ни среди активных чатов, ни в очереди!")
        assert (self.is_element_present(driver, locator_chat) == True)
        # Подключение Агента к Чату
        chat_button = driver.find_element_by_xpath(locator_chat)
        chat_button.click()
        print("Агент подключился к Чату")

    @allure.step('АРМ РИЦ: Проверка отображения отправленного Агентом сообщения в окне Чата')
    def is_agent_message_in_arm_ric_chat(self, mess_agent):
        driver = self.driver
        if (self.is_element_present(driver, "//span[contains(text(),'" + mess_agent + "')]") == True):
            print("Сообщение, отправленное Агентом, отображается в теле Чата АРМ РИЦ")
        else:
            print("ОШИБКА!!! Сообщение, отправленное Агентом, не отображается в теле Чата АРМ РИЦ!")
            assert (self.is_element_present(driver, "//span[contains(text(),'" + mess_agent + "')]") == True)

    @allure.step('АРМ РИЦ: Проверка отображения отправленного Клиентом сообщения в окне Чата')
    def is_client_message_in_arm_ric_chat(self, mess_client):
        driver = self.driver
        if (self.is_element_present(driver, "//span[contains(text(),'" + mess_client + "')]") == True):
            print("Сообщение, отправленное Клиентом, отображается в теле Чата АРМ РИЦ")
        else:
            print("ОШИБКА!!! Сообщение, отправленное Клиентом, не отображается в теле Чата АРМ РИЦ!")
            assert (self.is_element_present(driver, "//span[contains(text(),'" + mess_client + "')]") == True)

    @allure.step('АРМ РИЦ: Отправка Агентом сообщения в Чат')
    def agent_send_message(self, mess_agent):
        driver = self.driver
        input_window = driver.find_element_by_class_name("MsgInput")
        input_window.send_keys(mess_agent)
        button_msg_input = driver.find_element_by_css_selector("button.MsgSubmit[name=MsgSubmit]")
        button_msg_input.click()
        print("Агент отправил в Чат сообщение")

    @allure.step('АРМ РИЦ: Отправка Агентом быстрого ответа в Чат')
    def agent_send_fast_answer(self):
        driver = self.driver
        elements = driver.find_elements_by_xpath("//div[@class='AnswersList']//li")
        fast_answers_count = len(elements)
        print("Всего найдено быстрых ответов: ", fast_answers_count)
        if fast_answers_count > 0:
            list = [num for num in range(fast_answers_count)]
            fast_answer = driver.find_element_by_xpath(
                "//div[@class='AnswersList']//li['" + str(random.choice(list) + 1) + "']")
            quick_message = fast_answer.get_attribute("textContent")
            print("Выбран БО: ", quick_message)
            fast_answer.click()
            ActionChains(driver).send_keys(Keys.SHIFT + Keys.ENTER).perform()
            print("Агент отправил в Чат сообщение - быстрый ответ")
            if (self.is_element_present(driver, "//span[contains(text(),'" + quick_message + "')]") == True):
                print("Сообщение, отправленное Агентом, отображается в теле Чата АРМ РИЦ")
            else:
                print("ОШИБКА!!! Сообщение, отправленное Агентом, не отображается в теле Чата АРМ РИЦ!")
                assert (self.is_element_present(driver, "//span[contains(text(),'" + quick_message + "')]") == True)

    @allure.step('АРМ РИЦ: Завершение Агентом всех активных Чатов')
    def agent_completion_chat(self):
        driver = self.driver
        i = 0
        while len(driver.find_elements_by_xpath(
                "//button[contains(@name,'CloseSession') and @class='HelperButton']")) > 0:
            button_close_chat = driver.find_element_by_xpath(
                "//button[contains(@name,'CloseSession') and @class='HelperButton']")
            button_close_chat.click()

            time.sleep(5)

            try:
                alert = driver.switch_to.alert
                print("Alert text: " + alert.text)
                alert.accept()
                print("Alert detected, accept it.")
            except UnexpectedAlertPresentException:
                print("UnexpectedAlertPresentException!")
            except NoAlertPresentException:
                print("NoAlertPresentException!")

            button_remove_chat = driver.find_element_by_xpath("//button[@class='RemoveSessionRow']")
            button_remove_chat.click()

            time.sleep(5)

            try:
                alert = driver.switch_to.alert
                print("Alert text: " + alert.text)
                alert.accept()
                print("Alert detected, accept it.")
            except UnexpectedAlertPresentException:
                print("UnexpectedAlertPresentException!")
            except NoAlertPresentException:
                print("NoAlertPresentException!")

            i = i + 1
        print("Агент завершил Чатов:", i)

    @allure.step('АРМ РИЦ: Переход на вкладку Быстрые ответы')
    def go_to_fast_answers(self):
        driver = self.driver
        menu_online_dialog = driver.find_element_by_xpath("//a[@title='Онлайн-диалог']")
        menu_online_dialog.click()
        menu_fast_answers = driver.find_element_by_xpath("//a[@title='Быстрые ответы (n)']")
        menu_fast_answers.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        if (self.is_element_present(driver, "//h1[.='Быстрые ответы']") == True and self.is_element_present(driver,
                                                                                                            "//a[@class='CallForAction Plus']") == True):
            print("Агент перешел на вкладку Быстрые ответы")
        else:
            print("ОШИБКА!!! Агент не перешел на вкладку Быстрые ответы!")
            assert (self.is_element_present(driver, "//h1[.='Быстрые ответы']") == True and self.is_element_present(
                driver, "//a[@class='CallForAction Plus']") == True)

    @allure.step('АРМ РИЦ: Добавление быстрого ответа')
    def add_fast_answer(self, fast_answer):
        driver = self.driver

        fast_answers_count_before = len(driver.find_elements_by_xpath("//table[@id='User']/tbody/tr"))
        print("Количество БО до добавления: ", fast_answers_count_before)

        print("Текст добавляемого БО: ", fast_answer)

        button_add_fast_answer = driver.find_element_by_xpath("//a[@class='CallForAction Plus']")
        button_add_fast_answer.click()
        field_fast_answer = driver.find_element_by_xpath("//input[@id='AnswerValue']")
        field_fast_answer.click()
        field_fast_answer.clear()
        field_fast_answer.send_keys(fast_answer)
        button_submit = driver.find_element_by_xpath("//button[@id='Submit']")
        button_submit.click()

        fast_answers_count_after = len(driver.find_elements_by_xpath("//table[@id='User']/tbody/tr"))
        print("Количество БО после добавления: ", fast_answers_count_after)

        if (fast_answers_count_after == (fast_answers_count_before + 1)):
            print("Быстрый ответ добавлен - количество БО после добавления на 1 больше, чем до добавления")
        else:
            print(
                "ОШИБКА!!! Быстрый ответ не добавлен - количество БО после добавления отличается от количества БО до добавления не на +1!")
            assert (fast_answers_count_after == (fast_answers_count_before + 1))

        if (self.is_element_present(driver, "//a[contains(text(),'" + fast_answer + "')]") == True):
            print("Текст добавленного БО отображается корректно")
        else:
            print("ОШИБКА!!! Текст добавленного БО отображается не корректно или не найден!")
            assert (self.is_element_present(driver, "//a[contains(text(),'" + fast_answer + "')]") == True)

        i = 1

        while i <= fast_answers_count_after:
            fast_answer_text = driver.find_element_by_xpath(
                "//table[@id='User']/tbody/tr[" + str(i) + "]/td[1]/a").get_attribute("textContent")
            if fast_answer_text == fast_answer:
                fast_answer_priority = driver.find_element_by_xpath(
                    "//table[@id='User']/tbody/tr[" + str(i) + "]/td[2]").get_attribute("textContent")
                fast_answer_visibility = driver.find_element_by_xpath(
                    "//table[@id='User']/tbody/tr[" + str(i) + "]/td[3]").get_attribute("textContent")
                if fast_answer_priority == "0" and fast_answer_visibility == "показывать":
                    print(
                        "Приоритет и видимость добавленного быстрого ответа корректны - соответствуют значениям, заданным по-умолчанию")
                    break
                else:
                    print(
                        "ОШИБКА!!! Приоритет и видимость добавленного быстрого ответа не соответствуют значениям, заданным по-умолчанию!")
                    assert (fast_answer_priority == "0" and fast_answer_visibility == "показывать")
            i = i + 1

    @allure.step('АРМ РИЦ: Удаление быстрого ответа')
    def delete_fast_answer(self):
        driver = self.driver

        fast_answers_before = driver.find_elements_by_xpath("//a[@class='AsBlock' and contains(text(),'Удалить')]")
        fast_answers_count_before = len(fast_answers_before)
        print("Количество БО до добавления: ", fast_answers_count_before)

        if fast_answers_count_before > 0:
            list = [num for num in range(fast_answers_count_before)]
            deleted_fast_answer = fast_answers_before[random.choice(list)]
            deleted_fast_answer.click()
            time.sleep(5)

            try:
                alert = driver.switch_to.alert
                print("Alert text: " + alert.text)
                alert.accept()
                print("Alert detected, accept it.")
            except UnexpectedAlertPresentException:
                print("UnexpectedAlertPresentException!")
            except NoAlertPresentException:
                print("NoAlertPresentException!")

            time.sleep(5)

            fast_answers_count_after = len(
                driver.find_elements_by_xpath("//a[@class='AsBlock' and contains(text(),'Удалить')]"))
            print("Количество БО после добавления: ", fast_answers_count_after)

            if (fast_answers_count_before == (fast_answers_count_after + 1)):
                print("Удален 1 быстрый ответ")
            else:
                print(
                    "ОШИБКА!!! Быстрый ответ не удален - количество БО после добавления отличается от количества БО до добавления не на -1!")
                assert (fast_answers_count_before == (fast_answers_count_after + 1))
        else:
            print("Не найдено ни одно быстрого ответа - удалять нечего!")

    @allure.step('АРМ РИЦ: Изменение быстрого ответа')
    def change_fast_answer(self, fast_answer):
        driver = self.driver

        fast_answer_text_new = fast_answer + " changed"
        fast_answers_count_before = len(driver.find_elements_by_xpath("//table[@id='User']/tbody/tr"))
        print("Количество БО до изменения: ", fast_answers_count_before)

        driver.find_element_by_xpath("//a[contains(text(),'" + fast_answer + "')]").click()
        field_text_fast_answer = driver.find_element_by_xpath("//input[@id='AnswerValue']")
        field_text_fast_answer.click()
        field_text_fast_answer.clear()
        field_text_fast_answer.send_keys(fast_answer_text_new)
        field_priority_fast_answer = driver.find_element_by_xpath("//input[@id='Weight']")
        field_priority_fast_answer.click()
        field_priority_fast_answer.clear()
        field_priority_fast_answer.send_keys("10")
        field_visibility_fast_answer = driver.find_element_by_xpath("//select[@id='ValidID']")
        field_visibility_fast_answer.click()
        driver.find_element_by_xpath("//option[@value='2']").click()
        button_submit = driver.find_element_by_xpath("//button[@id='Submit']")
        button_submit.click()

        fast_answers_count_after = len(driver.find_elements_by_xpath("//table[@id='User']/tbody/tr"))
        print("Количество БО после изменения: ", fast_answers_count_after)

        if (fast_answers_count_after == fast_answers_count_before):
            print("Количество быстрых ответов до и после изменения параметров одного из них совпадает")
        else:
            print(
                "ОШИБКА!!! Количество быстрых ответов до и после изменения параметров одного из них не совпадает!")
            assert (fast_answers_count_after == fast_answers_count_before)

        if (self.is_element_present(driver, "//a[contains(text(),'" + fast_answer_text_new + "')]") == True):
            print("Измененный текст БО отображается корректно")
        else:
            print("ОШИБКА!!! Текст измененного БО отображается не корректно или не найден!")
            assert (self.is_element_present(driver, "//a[contains(text(),'" + fast_answer_text_new + "')]") == True)

        i = 1

        while i <= fast_answers_count_after:
            fast_answer_text = driver.find_element_by_xpath(
                "//table[@id='User']/tbody/tr[" + str(i) + "]/td[1]/a").get_attribute("textContent")
            if fast_answer_text == fast_answer_text_new:
                fast_answer_priority = driver.find_element_by_xpath(
                    "//table[@id='User']/tbody/tr[" + str(i) + "]/td[2]").get_attribute("textContent")
                fast_answer_visibility = driver.find_element_by_xpath(
                    "//table[@id='User']/tbody/tr[" + str(i) + "]/td[3]").get_attribute("textContent")
                if fast_answer_priority == "10" and fast_answer_visibility == "не показывать":
                    print("Измененные приоритет и видимость быстрого ответа отображаются корректно")
                    break
                else:
                    print("ОШИБКА!!! Приоритет и видимость измененного БО не соответствуют новым значениям!")
                    assert (fast_answer_priority == "10" and fast_answer_visibility == "не показывать")
            i = i + 1

    @allure.step('АРМ РИЦ: Переход на вкладку По телефону')
    def go_to_by_phone(self):
        driver = self.driver
        menu_by_phone = driver.find_element_by_xpath("//a[@title='По телефону']")
        menu_by_phone.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        if (self.is_element_present(driver,
                                    "//h1[contains(text(),'Настройка содержания вкладки')]") == True and self.is_element_present(
            driver,
            "//form[@id='ByPhoneMessageForm']") == True):
            print("Агент перешел на вкладку По телефону")
        else:
            print("ОШИБКА!!! Агент не перешел на вкладку По телефону!")
            assert (self.is_element_present(driver,
                                            "//h1[contains(text(),'Настройка содержания вкладки')]") == True and self.is_element_present(
                driver,
                "//form[@id='ByPhoneMessageForm']") == True)

    @allure.step('АРМ РИЦ: Переход на вкладку Онлайн-диалог')
    def go_to_online_dialog(self):
        driver = self.driver
        menu1_online_dialog = driver.find_element_by_xpath("//a[@title='Онлайн-диалог']")
        menu1_online_dialog.click()
        menu2_online_dialog = driver.find_element_by_xpath("//a[@title='Helper chat (n)']")
        menu2_online_dialog.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        time.sleep(3)
        if (self.is_element_present(driver,
                                    "//div[@class='Title' and contains(text(),'РИЦ №')]") == True and self.is_element_present(
            driver,
            "//div[@class='HelperQueue' and contains(text(),'В очереди')]") == True):
            print("Агент перешел на вкладку Онлайн-диалог")
        else:
            print("ОШИБКА!!! Агент не перешел на вкладку Онлайн-диалог!")
            assert (self.is_element_present(driver,
                                            "//div[@class='Title' and contains(text(),'РИЦ №')]") == True and self.is_element_present(
                driver,
                "//div[@class='HelperQueue' and contains(text(),'В очереди')]") == True)

    @allure.step('АРМ РИЦ: Переход на вкладку История сеансов общения')
    def go_to_history(self):
        driver = self.driver
        menu_online_dialog = driver.find_element_by_xpath("//a[@title='Онлайн-диалог']")
        menu_online_dialog.click()
        menu_history = driver.find_element_by_xpath("//a[@title='История сеансов общения']")
        menu_history.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        if (self.is_element_present(driver,
                                    "//h1[@class='Header' and contains(text(),'История сеансов общения')]") == True and self.is_element_present(
            driver, "//h2[contains(text(),'Список')]") == True):
            print("Агент перешел на вкладку История сеансов общения")
        else:
            print("ОШИБКА!!! Агент не перешел на вкладку История сеансов общения!")
            assert (self.is_element_present(driver,
                                            "//h1[@class='Header' and contains(text(),'История сеансов общения')]") == True and self.is_element_present(
                driver, "//h2[contains(text(),'Список')]") == True)

    @allure.step('АРМ РИЦ: Переход на вкладку Настройки рабочего времени РИЦ')
    def go_to_work_time_settings(self):
        driver = self.driver
        menu_online_dialog = driver.find_element_by_xpath("//a[@title='Онлайн-диалог']")
        menu_online_dialog.click()
        menu_work_time_settings = driver.find_element_by_xpath("//a[@title='Настройки рабочего времени РИЦ']")
        menu_work_time_settings.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        if (self.is_element_present(driver,
                                    "//div/h1[contains(text(),'Настройки рабочего времени РИЦ')]") == True and self.is_element_present(
            driver, "//div[@class='Header']/h2[contains(text(),'Форма')]") == True):
            print("Агент перешел на вкладку Настройки рабочего времени РИЦ")
        else:
            print("ОШИБКА!!! Агент не перешел на вкладку Настройки рабочего времени РИЦ!")
            assert (self.is_element_present(driver,
                                            "//div/h1[contains(text(),'Настройки рабочего времени РИЦ')]") == True and self.is_element_present(
                driver, "//div[@class='Header']/h2[contains(text(),'Форма')]") == True)

    @allure.step('АРМ РИЦ: Переход на вкладку Техническая документация')
    def go_to_tech_doc(self):
        driver = self.driver
        menu_online_dialog = driver.find_element_by_xpath("//a[@title='Онлайн-диалог']")
        menu_online_dialog.click()
        menu_tech_doc = driver.find_element_by_xpath("//a[@title='Техническая документация']")
        menu_tech_doc.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        if (self.is_element_present(driver,
                                    "//div[@class='download-name']/a[contains(text(),'ТЕХНИЧЕСКАЯ ИНСТРУКЦИЯ ДЛЯ РИЦ')]") == True):
            print("Агент перешел на вкладку Техническая документация")
        else:
            print("ОШИБКА!!! Агент не перешел на вкладку Техническая документация!")
            assert (self.is_element_present(driver,
                                            "//div[@class='download-name']/a[contains(text(),'ТЕХНИЧЕСКАЯ ИНСТРУКЦИЯ ДЛЯ РИЦ')]") == True)

    @allure.step('АРМ РИЦ: Переход на вкладку Отчеты для Лидера РИЦ')
    def go_to_reports(self):
        driver = self.driver
        menu_reports = driver.find_element_by_xpath("//a[@title='Отчёты для Лидера РИЦ']")
        menu_reports.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        if (self.is_element_present(driver,
                                    "//div/h1[contains(text(),'Статистика')]") == True and self.is_element_present(
            driver, "//div[@class='Header']/h2[contains(text(),'Список')]") == True):
            print("Агент перешел на вкладку Отчеты для Лидера РИЦ")
        else:
            print("ОШИБКА!!! Агент не перешел на вкладку Отчеты для Лидера РИЦ!")
            assert (self.is_element_present(driver,
                                            "//div/h1[contains(text(),'Статистика')]") == True and self.is_element_present(
                driver, "//div[@class='Header']/h2[contains(text(),'Список')]") == True)

    @allure.step('АРМ РИЦ: Изменение контактной информации о РИЦ на вкладке По телефону')
    def change_ric_info(self, contact_info):
        driver = self.driver
        browser = self.browser
        # Переход во фрейм визуального тестового редактора
        logout_frame = driver.find_element_by_xpath("//*[@id='cke_1_contents']/iframe")
        driver.switch_to.frame(logout_frame)
        field_contact_info = driver.find_element_by_xpath("//html/body")
        field_contact_info.click()
        ActionChains(driver).send_keys(Keys.CONTROL + 'a').perform()
        ActionChains(driver).send_keys(Keys.DELETE).perform()
        field_contact_info.click()
        if browser == "chrome":
            field_contact_info.send_keys(
                "123")  # не знаю почему, но в chrome без этой строчки последующий ввод символов не происходит
        field_contact_info.send_keys(contact_info)
        # Возврат в основной фрейм
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath("//button[@class='MsgSubmit']").click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        print("Информация о РИЦ изменена")

    @allure.step('АРМ РИЦ: Получение информации о Горячей линии РИЦ на вкладке По телефону')
    def get_hotline_info_arm_ric(self):
        driver = self.driver
        # Переход во фрейм, предназначенный для редактирования информации о РИЦ
        logout_frame = driver.find_element_by_xpath("//*[@id='cke_1_contents']/iframe")
        driver.switch_to.frame(logout_frame)
        hotline_info = driver.find_element_by_xpath("//html/body").get_attribute("textContent")
        # Выход из фрейма, предназначенного для редактирования информации о РИЦ
        driver.switch_to.default_content()
        return hotline_info

    @allure.step('АРМ РИЦ: Изменение настроек рабочего времени РИЦ')
    def set_up_work_time(self, weekday, hour, weekday_num):
        driver = self.driver
        if weekday_num == 0:
            i = 1
            while i <= 7:
                driver.find_element_by_xpath(
                    "//div[@class='Setting']/div[" + str(i) + "]/div[25]/label/input[@name='wholeDay']").click()
                i = i + 1
            driver.find_element_by_xpath("//button[@name='Submit']").click()
            print("Настройки рабочего времени изменены: периоды нерабочего времени не заданы")
        else:
            driver.find_element_by_xpath(
                "//div[@class='Setting']/div[" + str(weekday_num) + "]/div[25]/label/input[@name='wholeDay']").click()
            driver.find_element_by_xpath("//input[@name='" + weekday + "' and @value='" + hour + "']").click()
            driver.find_element_by_xpath("//button[@name='Submit']").click()
            print(
                "Настройки рабочего времени изменены. Установлено нерабочее время: " + weekday + " c " + hour + ":00 до " + str(
                    int(hour) + 1) + ":00")

    @allure.step(
        'АРМ РИЦ: Получение текста о недоступности РИЦ, задаваемого в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ')
    def get_agent_unavailable_text(self):
        driver = self.driver
        unavailable_text = driver.find_element_by_xpath("//textarea[@id='TextUnavailable']").get_attribute(
            "textContent")
        print("Текст о недоступности РИЦ, задаваемый в АРМ РИЦ на вкладке Настройки рабочего времени РИЦ: ",
              unavailable_text)
        return unavailable_text

    # BASIC METHODS

    @allure.step('Обновление страницы')
    def refresh(self):
        driver = self.driver
        driver.refresh()

    @allure.step('Определение контрольного числа на основе даты и времени')
    def calc_check_sum_from_date(self):
        now = str(datetime.datetime.now())
        print("Дата и время: now = " + now)
        now = now.replace("-", "")
        now = now.replace(" ", "")
        now = now.replace(":", "")
        now = now.replace(".", "")
        print("Дата и время после удаления {- :,} : now = " + now)
        control_num = now[:12]
        print("Контрольное число на основе даты и времени = ", control_num)
        return control_num

    @allure.step('Получение номера телефона из случайного набора цифр')
    def get_phone_as_random_set(self):
        list1 = [num for num in range(10)]
        i = 0
        list2 = []
        while i < 10:
            list2.append(str(random.choice(list1)))
            i = i + 1
        phone = ""
        for i in list2: phone = phone + str(i)
        print("phone: ", phone)
        phone_mask = "+7 (" + str(list2[0]) + str(list2[1]) + str(list2[2]) + ") " + str(list2[3]) + str(
            list2[4]) + str(
            list2[5]) + "-" + str(list2[6]) + str(list2[7]) + "-" + str(list2[8]) + str(list2[9])
        print("phone_mask: ", phone_mask)
        return phone, phone_mask

    # Проверка существования элемента(для использования в методах application.py)
    def is_element_present(self, driver, locator):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    # Проверка видимости элемента(для использования в методах application.py)
    def is_element_visible(self, driver, locator):
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    # Проверка существования элемента(для использования во внешних методах)
    def is_element_present_main(self, locator, wait=10):
        driver = self.driver
        try:
            WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    # Проверка существования элемента(для использования во внешних методах)
    def is_element_present_main_css(self, locator, wait=10):
        driver = self.driver
        try:
            WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except:
            return False

    # Проверка видимости элемента для использования во внешних методах)
    def is_element_visible_main(self, locator):
        driver = self.driver
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    # Подсчет количества эементов(для использования во внешних методах)
    def count_of_elements_main(self, elements):
        driver = self.driver
        count = len(driver.find_elements_by_xpath(elements))
        return count

    # Клик по объекту (для использования во внешних методах)
    def check_click(self, locator):
        driver = self.driver
        object_click = driver.find_element_by_xpath(locator)
        object_click.click()

    def destroy(self):
        self.driver.quit()
