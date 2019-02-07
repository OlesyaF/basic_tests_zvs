# -*- encoding: utf-8 -*-

import time
import datetime
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import random
import allure

# noinspection PyDeprecation
class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    @allure.step('Вход в ОВ')
    def go_to_online_version(self, ov_link):
        driver = self.driver
        driver.get(ov_link)
        # КЛИЕНТ Проверяем, что ОВ доступна
        if (self.is_element_present(driver, "//input[@id='loginform-login']") != True):
            print("ОШИБКА!!! Онлайн Версия не доступна! - Не найдено поле 'Логин' для авторизации")
            assert (self.is_element_present(driver, "//input[@id='loginform-login']") == True)

    @allure.step('Авторизация в ОВ')
    def login_client(self, client_name, client_password):
        driver = self.driver
        input_field_login = driver.find_element_by_id("loginform-login")
        input_field_login.send_keys(client_name)
        input_field_password = driver.find_element_by_id("loginform-password")
        input_field_password.send_keys(client_password)
        button_login = driver.find_element_by_id("buttonLogin")
        button_login.click()
        # КЛИЕНТ Логин: Проверяем, что Клиент залогинился
        if (self.is_element_present(driver, "//div[@id='logout']") == True):
            print("Клиент залогинился в ОВ")
        else:
            print("ОШИБКА!!! Клиент не залогинился в ОВ! - Не найдена кнопка 'Выйти'")
            assert (self.is_element_present(driver, "//div[@id='logout']") == True)

    @allure.step('Переход в Онлайн-Диалог')
    def go_to_online_dialog(self):
        driver = self.driver
        # КЛИЕНТ Нажимаем кнопку "Задать вопрос"
        button_zv = driver.find_element_by_xpath("//div[@class='topToolbar']/div[5]/div[2]")
        button_zv.click()
        # КЛИЕНТ Переходим во фрейм "Задать вопрос"
        chat = driver.find_element_by_css_selector("#livechat-dialog iframe")
        driver.switch_to.frame(chat)
        # КЛИЕНТ Проверяем, что перешли в ОД
        if (self.is_element_present(driver, "//textarea[@id='MsgInput']") == True):
            print("Клиент перешел в ОД (найдено поле для ввода сообщения)")
        else:
            print("ОШИБКА!!! Онлайн Диалог не доступен! - Не найдено поле для ввода сообщения")
            assert (self.is_element_present(driver, "//textarea[@id='MsgInput']") == True)

    @allure.step('Переход в окно "Изменить контактные данные"')
    def go_to_client_info(self):
        driver = self.driver
        button_client_info = driver.find_element_by_css_selector("div.authEdit.ChangeUserInfo")
        button_client_info.click()
        # КЛИЕНТ Проверяем, что перешли в окно "Изменить контактные данные"
        if (self.is_element_present(driver,
                                    "//div[contains(@class, 'UserInfoHeader') and contains(text(),'Изменить контактные данные')]") == True):
            print("Клиент перешел в окно 'Изменить контактные данные'")
        else:
            print("ОШИБКА!!! Клиент не перешел в окно 'Изменить контактные данные'! - Не найдено название окна")
            assert (self.is_element_present(driver,
                                            "//div[contains(@class, 'UserInfoHeader') and contains(text(),'Изменить контактные данные')]") == True)

    @allure.step('Изменение имени Клиента')
    def changing_client_name(self, client_name):
        driver = self.driver
        input_field_name = driver.find_element_by_id("FormCustomerFullname")
        input_field_name.click()
        input_field_name.clear()
        input_field_name.send_keys(client_name)
        print("В поле 'Имя' введено новое значение")
        button_submit = driver.find_element_by_id("CustomerDataSubmit")
        button_submit.click()
        print("Нажата кнопка 'Сохранить'")

    @allure.step('Изменение email Клиента')
    def changing_client_email(self, email):
        driver = self.driver
        input_field_name = driver.find_element_by_id("FormCustomerEmail")
        input_field_name.click()
        input_field_name.clear()
        input_field_name.send_keys(email)
        print("В поле 'Email' введено новое значение")
        button_submit = driver.find_element_by_id("CustomerDataSubmit")
        button_submit.click()
        print("Нажата кнопка 'Сохранить'")

    @allure.step('Изменение номера телефона Клиента')
    def changing_client_phone(self, phone):
        driver = self.driver
        input_field_name = driver.find_element_by_id("FormCustomerPhone")
        input_field_name.click()
        input_field_name.clear()
        input_field_name.send_keys(Keys.HOME)
        input_field_name.send_keys(phone)
        print("В поле 'Телефон' введено новое значение")
        button_submit = driver.find_element_by_id("CustomerDataSubmit")
        button_submit.click()
        print("Нажата кнопка 'Сохранить'")

    def client_send_message(self, mess_client):
        driver = self.driver
        input_window = driver.find_element_by_id("MsgInput")
        input_window.send_keys(mess_client)
        button_msg_input = driver.find_element_by_id("ChatMsgSubmit")
        button_msg_input.click()
        print("Клиент отправил в Чат сообщение")

    # Клиент ожидает сообщение Агента
    def client_wait_agent_message(self, mess_agent):
        driver = self.driver
        print("Клиент ожидает сообщение Агента")
        mess_agent_in_chat = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'message_text') and contains(text(),'" + mess_agent + "')]")))
        print("Клиент получил сообщение Агента")

    def is_client_message_in_online_dialog(self, mess_client):
        driver = self.driver
        if (self.is_element_present(driver, "//div[contains(text(),'" + mess_client + "')]") == True):
            print("Сообщение, отправленное Клиентом, отображается в теле Чата ОВ")
        else:
            print("ОШИБКА!!! Сообщение, отправленное Клиентом, не отображается в теле Чата ОВ!")
            assert (self.is_element_present(driver, "//div[contains(text(),'" + mess_client + "')]") == True)

    def go_out_online_dialog(self):
        driver = self.driver
        # КЛИЕНТ Логаут: Возвращаемся в основной фрейм
        driver.switch_to.parent_frame()
        button_close_chat = driver.find_element_by_xpath("//div[@class='icon livechatclose-16']")
        button_close_chat.click()
        driver.refresh()

    @allure.step('Выход из ОВ')
    def logout_client(self):
        driver = self.driver
        # КЛИЕНТ Логаут: Возвращаемся в основной фрейм
        driver.switch_to.parent_frame()
        # КЛИЕНТ Логаут: Нажимаем кнопку "Выйти"
        button_logout = driver.find_element_by_xpath("//*[@id='logout']/div[1]")
        button_logout.click()
        # КЛИЕНТ Логаут: Переходим во фрейм "Вы действительно хотите выйти из системы?"
        logout_frame = driver.find_element_by_css_selector("#dialogFrame1 iframe")
        driver.switch_to.frame(logout_frame)
        logout_confirm = driver.find_element_by_css_selector(
            "#confirm > table > tbody > tr:nth-child(2) > td:nth-child(1) > button > span")
        logout_confirm.click()
        # КЛИЕНТ Логаут: Проверяем, что Клиент разлогинился
        if (self.is_element_present(driver, "//input[@id='loginform-password']") == True):
            print("Клиент вышел из ОВ")
        else:
            print("ОШИБКА!!! Поле для ввода пароля не найдено. Клиент не разлогинился!")
            assert (self.is_element_present(driver, "//input[@id='loginform-password']") == True)

    def go_to_consultant_plus_agent(self, cp_link):
        driver = self.driver
        driver.get(cp_link)
        # АГЕНТ Проверяем, что К+ доступен
        if (self.is_element_present(driver, "//input[@id='User']") != True):
            print("ОШИБКА!!! Консультант+ не доступен! - Не найдено поле 'Логин' для авторизации")
            assert (self.is_element_present(driver, "//input[@id='User']") == True)

    # АГЕНТ Авторизация в Консультант+ на zv5/zv6
    def login_agent(self, agent_login, agent_password):
        driver = self.driver
        login_field = driver.find_element_by_id("User")
        login_field.send_keys(agent_login)
        password_field = driver.find_element_by_id("Password")
        password_field.send_keys(agent_password)
        button_login = driver.find_element_by_id("LoginButton")
        button_login.click()
        # АГЕНТ Логин: Проверяем, что Агент залогинился
        if (self.is_element_present(driver, "//li[@id='nav-Chat']") == True):
            print("Агент залогинился в К+")
        else:
            button_login = driver.find_element_by_id("LoginButton")
            button_login.click()
            if (self.is_element_present(driver, "//li[@id='nav-Chat']") == True):
                print("Агент залогинился в К+")
            else:
                print("ОШИБКА!!! Агент не залогинился в К+! - Не найдено меню 'Онлайн-диалог'")
                assert (self.is_element_present(driver, "//li[@id='nav-Chat']") == True)

    # АГЕНТ Авторизация в Консультант+ на ПП (HTTP Basic Authentication)
    def login_agent_pp(self, cp_link):
        driver = self.driver
        driver.get(cp_link)
        # driver.get("https://" + agent_login + ":" + agent_password + "@ric.consultant.ru/")
        # АГЕНТ Переход к сервису "Задать вопрос"
        button_zv = driver.find_element_by_id("2050")
        button_zv.click()

    def agent_search_chat_and_mess(self, mess_client, wait):
        driver = self.driver
        # АГЕНТ Поиск Чата
        locator_mess_client = "//span[contains(text(),'" + mess_client + "')]"
        agent = "109_866712"
        locator_agent = "//span[contains(text(),'" + agent + "')]"
        locator_connect_to_session = "//*[@id='Sessions']/div[3]/button"
        i = 0
        if (self.is_element_present(driver, locator_agent) == True):
            print("Агент нашел Чат Клиента среди активных чатов К+")
        else:
            while (self.is_element_present(driver, locator_connect_to_session) == True):
                connect_to_session_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "StartChat")))
                connect_to_session_button.click()
                i += 1
                if (self.is_element_present(driver, locator_agent) == True):
                    print("Агент нашел Чат Клиента в ", i, " очереди")
                    break
        # АГЕНТ Проверяем, что Чат Клиента-автотеста найден
        time.sleep(wait)
        if (self.is_element_present(driver, locator_agent) != True):
            print("ОШИБКА!!! Чат Клиента не обнаружен ни среди активных чатов, ни в очереди!")
        assert (self.is_element_present(driver, locator_agent) == True)

        # АГЕНТ Подключение к Чату
        chat_button = driver.find_element_by_xpath(locator_agent)
        chat_button.click()
        print("Агент подключился к Чату")

        # АГЕНТ Проверка наличия в Чате сообщения от Клиента
        if (self.is_element_present(driver, locator_mess_client) == True):
            print("Сообщение, отправленное Клиентом, найдено в Чате К+")
        else:
            print("ОШИБКА!!! Сообщение от Клиента в Чате К+ не найдено!")
        assert (self.is_element_present(driver, locator_mess_client) == True)

    def agent_search_chat(self, wait, client_name):
        driver = self.driver
        # АГЕНТ Поиск Чата
        locator_chat = "//strong[contains(text(),'" + client_name + "')]"
        locator_connect_to_session = "//*[@id='Sessions']/div[3]/button"
        i = 0
        if (self.is_element_present(driver, locator_chat) == True):
            print("Агент нашел Чат Клиента среди активных чатов К+")
        else:
            while (self.is_element_present(driver, locator_connect_to_session) == True):
                connect_to_session_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "StartChat")))
                connect_to_session_button.click()
                i += 1
                if (self.is_element_present(driver, locator_chat) == True):
                    print("Агент нашел Чат Клиента в ", i, " очереди")
                    break
        # АГЕНТ Проверяем, что Чат Клиента-автотеста найден
        time.sleep(wait)
        if (self.is_element_present(driver, locator_chat) != True):
            print("ОШИБКА!!! Чат Клиента не обнаружен ни среди активных чатов, ни в очереди!")
        assert (self.is_element_present(driver, locator_chat) == True)
        # АГЕНТ Подключение к Чату
        chat_button = driver.find_element_by_xpath(locator_chat)
        chat_button.click()
        print("Агент подключился к Чату")

    def agent_send_message(self, mess_agent):
        driver = self.driver
        input_window = driver.find_element_by_class_name("MsgInput")
        input_window.send_keys(mess_agent)
        button_msg_input = driver.find_element_by_css_selector("button.MsgSubmit[name=MsgSubmit]")
        button_msg_input.click()
        print("Агент отправил в Чат сообщение")

    def is_agent_message_in_consultant_plus(self, mess_agent):
        driver = self.driver
        if (self.is_element_present(driver, "//span[contains(text(),'" + mess_agent + "')]") == True):
            print("Сообщение, отправленное Агентом, отображается в теле Чата К+")
        else:
            print("ОШИБКА!!! Сообщение, отправленное Агентом, не отображается в теле Чата К+!")
            assert (self.is_element_present(driver, "//span[contains(text(),'" + mess_agent + "')]") == True)

    def is_client_message_in_consultant_plus(self, mess_client):
        driver = self.driver
        if (self.is_element_present(driver, "//span[contains(text(),'" + mess_client + "')]") == True):
            print("Сообщение, отправленное Клиентом, отображается в теле Чата К+")
        else:
            print("ОШИБКА!!! Сообщение, отправленное Клиентом, не отображается в теле Чата К+!")
            assert (self.is_element_present(driver, "//span[contains(text(),'" + mess_client + "')]") == True)

    def is_client_message_in_consultant_plus(self, mess_client):
        driver = self.driver
        if (self.is_element_present(driver, "//span[contains(text(),'" + mess_client + "')]") == True):
            print("Сообщение, отправленное Клиентом, отображается в теле Чата К+")
        else:
            print("ОШИБКА!!! Сообщение, отправленное Клиентом, не отображается в теле Чата К+!")
            assert (self.is_element_present(driver, "//span[contains(text(),'" + mess_client + "')]") == True)

    # Агент ожидает сообщение Клиента
    def agent_wait_client_message(self, mess_client):
        driver = self.driver
        print("Агент ожидает сообщение Клиента")
        mess_client_in_chat = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'" + mess_client + "')]")))
        print("Агент получил сообщение Клиента")

    def logout_agent(self):
        driver = self.driver
        # АГЕНТ Логаут: Нажимаем на кнопку "Выйти", обрабатываем alert
        button_logout = driver.find_element_by_id("LogoutButton")
        button_logout.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        # АГЕНТ Логаут: Проверяем, что Агент разлогинился
        if (self.is_element_present(driver, "//input[@id='Password']") == True):
            print("Агент вышел из К+")
        else:
            print("ОШИБКА!!! Поле для ввода пароля не найдено. Агент не разлогинился!")
            assert (self.is_element_present(driver, "//input[@id='Password']") == True)

    def is_agent_message_in_online_dialog(self, mess_agent):
        driver = self.driver
        if (self.is_element_present(driver, "//div[contains(text(),'" + mess_agent + "')]") == True):
            print("Сообщение, отправленное Агентом, отображается в теле Чата ОВ")
        else:
            print("ОШИБКА!!! Сообщение, отправленное Агентом, не отображается в теле Чата ОВ!")
            assert (self.is_element_present(driver, "//div[contains(text(),'" + mess_agent + "')]") == True)

    def is_element_present(self, driver, locator):
        try:
            driver.find_element_by_xpath(locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_present_main(self, locator):
        driver = self.driver
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    # Расчет контрольной суммы на основе даты и времени
    @allure.step('Расчет контрольной суммы на основе даты и времени')
    def calc_check_sum_from_date(self):
        now = str(datetime.datetime.now())
        print("Дата и время: now = " + now)
        now = now.replace("-", "")
        now = now.replace(" ", "")
        now = now.replace(":", "")
        now = now.replace(".", "")
        print("Дата и время после удаления {- :,} : now = " + now)
        check_list = list(now)
        print("Список символов даты и времени check_list: ", check_list)
        i = 0
        for chr in check_list:
            i = i + ord(chr)
        print("Контрольная сумма даты и времени = ", i)
        return i

    # Получение номера телефона из случайного набора цифр
    @allure.step('Получение номера телефона из случайного набора цифр')
    def get_phone_as_random_set(self):
        list1 = [num for num in range(10)]
        print("list1: ", list1)
        i = 0
        list2 = []
        while i < 10:
            list2.append(str(random.choice(list1)))
            i = i + 1
        print("list2: ", list2)
        phone = ""
        for i in list2: phone = phone + str(i)
        print("phone: ", phone)
        phone_mask = "+7 (" + str(list2[0]) + str(list2[1]) + str(list2[2]) + ") " + str(list2[3]) + str(
            list2[4]) + str(
            list2[5]) + "-" + str(list2[6]) + str(list2[7]) + "-" + str(list2[8]) + str(list2[9])
        print("phone_mask: ", phone_mask)
        return phone, phone_mask

    def destroy(self):
        self.driver.quit()
