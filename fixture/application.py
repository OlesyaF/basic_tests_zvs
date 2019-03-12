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

    def __init__(self, ov_url, client_login, client_password, arm_ric_url, agent_login, agent_password):
        self.driver = WebDriver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.ov_url = ov_url
        self.client_login = client_login
        self.client_password = client_password
        self.arm_ric_url = arm_ric_url
        self.agent_login = agent_login
        self.agent_password = agent_password

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
            print("ОВ доступна.")
        else:
            print("ОШИБКА!!! Онлайн Версия не доступна! - Не найдено поле 'Логин' для авторизации")
            assert (self.is_element_present(driver, "//input[@id='loginform-login']") == True)

    @allure.step('Онлайн-версия: Авторизация')
    def login_client(self):
        driver = self.driver
        client_login = self.client_login
        client_password = self.client_password
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

    @allure.step('Онлайн-версия: Переход в окно сервиса Задать вопрос (окно "Сервис поддержки клиентов")')
    def go_to_customer_support_service(self):
        driver = self.driver
        button_zv = driver.find_element_by_xpath("//div[@class='topToolbar']/div[5]/div[2]")
        button_zv.click()
        #Переход во фрейм серевиса Задать вопрос
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
        input_field_name.send_keys(phone)
        print("В поле 'Телефон' введено новое значение")

    @allure.step('Онлайн-версия: Выход из окна сервиса Задать вопрос')
    def go_out_customer_support_service(self):
        driver = self.driver
        #Возврат в основной фрейм
        driver.switch_to.parent_frame()
        button_close_chat = driver.find_element_by_xpath("//div[@class='icon livechatclose-16']")
        button_close_chat.click()
        driver.refresh()

    @allure.step('Онлайн-версия: Выход')
    def logout_client(self):
        driver = self.driver
        #Возврат в основной фрейм
        driver.switch_to.parent_frame()
        #Нажатие на кнопку "Выйти"
        button_logout = driver.find_element_by_xpath("//*[@id='logout']/div[1]")
        button_logout.click()
        #Переход во фрейм "Вы действительно хотите выйти из системы?"
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

    @allure.step('Онлайн-версия: Переход на вкладку "Написать эксперту" в окне "Сервис поддержки клиентов"')
    def go_to_expcons(self):
        driver = self.driver
        button_expcons = driver.find_element_by_xpath("//div[contains(text(),'Написать эксперту')]")
        button_expcons.click()
        print("Клиент перешел на вкладку 'Написать эксперту' в окне 'Сервис поддержки клиентов'")

    @allure.step('Онлайн-версия: Переход на вкладку "Горячая линия/Контактная информация РИЦ" в окне "Сервис поддержки клиентов"')
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
                                    "//span[contains(@class, 'SmallSpace tabTextTitle') and contains(text(),'Здесь Вы можете задать вопрос, который требует консультации эксперта')]") == True):
            print("1. Пояснительный текст ('Здесь Вы можете задать вопрос, который требует консультации эксперта') присутствует")
        else:
            print("ОШИБКА!!! Пояснительный текст ('Здесь Вы можете задать вопрос, который требует консультации эксперта') отсутствует!")
            assert (self.is_element_present(driver,
                                            "//span[contains(@class, 'SmallSpace tabTextTitle') and contains(text(),'Здесь Вы можете задать вопрос, который требует консультации эксперта')]") == True)
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

    @allure.step('Онлайн-версия: Проверка вида вкладки "Горячая линия/Контактная информация РИЦ" в окне "Сервис поддержки клиентов"')
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

    # АРМ РИЦ: АГЕНТ

    @allure.step('АРМ РИЦ: Вход')
    def go_to_arm_ric(self):
        driver = self.driver
        arm_ric_url = self.arm_ric_url
        driver.get(arm_ric_url)
        if (self.is_element_present(driver, "//*[@id='LogoutButton']") == True):
            print("АРМ РИЦ доступно. Агент авторизован. Видимо, предыдущий тест упал.")
            #Нажатие на кнопку "Выйти", обработка alert
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
            print("АРМ РИЦ доступно.")
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

    @allure.step('АРМ РИЦ: Переход в настройки доступности сервиса ‎Задать вопрос для онлайн-версии')
    def go_to_service_settings(self):
        driver = self.driver
        menu_ric_menu = driver.find_element_by_xpath("//li[@id='nav-RICMenu']")
        menu_ric_menu.click()
        menu_agent_distr_tabs = driver.find_element_by_xpath("//li[@id='nav-RICMenu-AgentDistrTabs']")
        menu_agent_distr_tabs.click()
        try:
            driver.switch_to.alert.accept()
        except:
            NoAlertPresentException
        if (self.is_element_present(driver, "//div[contains(text(),'Доступность сервиса «Задать вопрос»')]") == True):
            print("Агент перешел в настройки доступности сервиса ‎Задать вопрос для онлайн-версии")
        else:
           print("ОШИБКА!!! Агент не перешел в настройки доступности сервиса ‎Задать вопрос для онлайн-версии")
           assert (self.is_element_present(driver,
                                           "//div[contains(text(),'Доступность сервиса «Задать вопрос»‎')]") == True)

    @allure.step('АРМ РИЦ: Поиск комплекта BUHUL_866712')
    def kit_search(self):
        driver = self.driver
        button_configure = driver.find_element_by_xpath("//div[@class='button blue fl-lt']")
        button_configure.click()
        field_kit_list = driver.find_element_by_xpath("//input[@type='text']")
        field_kit_list.click()
        field_kit_list.send_keys("BUHUL_866712")
        field_kit_list.send_keys(Keys.ENTER)
        if (self.is_element_present(driver, "//div[@id='3124332_Row']") == True):
            print("Комплект BUHUL_866712 найден: строка комплекта отображается в результатах поиска")
        else:
           print("ОШИБКА!!! Комплект BUHUL_866712 НЕ найден! - Строка комплекта НЕ отображается в результатах поиска")
           assert (self.is_element_present(driver, "//div[@id='3124332_Row']") == True)

    @allure.step('АРМ РИЦ: Настройка доступности сервиса ‎Задать вопрос для онлайн-версии (заполнение чек-боксов)')
    def setting_checkbox(self, checkbox_status, checkbox_field, checkbox_click):
        driver = self.driver
        checkbox = driver.find_element_by_xpath(checkbox_field)
        print("checkbox.get_attribute('checked')=", checkbox.get_attribute('checked'))
        if (checkbox_status == "off") and (not checkbox.get_attribute('checked')):
            print("Чек-бокс в требуемом положении - выключен")
        if (checkbox_status == "on") and (checkbox.get_attribute('checked') == 'true'):
            print("Чек-бокс в требуемом положении - включен")
        if (checkbox_status == "off") and (checkbox.get_attribute('checked') == 'true'):
            driver.find_element_by_xpath(checkbox_click).click()
            print("Чек-бокс установлен в требуемое положение: выключен")
        if (checkbox_status == "on") and (not checkbox.get_attribute('checked')):
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
        #Нажатие на кнопку "Выйти", обработка alert
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
    def agent_search_chat(self, client_name):
        driver = self.driver
        locator_chat = "//strong[contains(text(),'" + client_name + "')]"
        locator_connect_to_session = "//*[@id='Sessions']/div[3]/button"
        i = 0
        if (self.is_element_present(driver, locator_chat) == True):
            print("Агент нашел Чат Клиента среди активных чатов")
        else:
            while (self.is_element_present(driver, locator_connect_to_session) == True):
                connect_to_session_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "StartChat")))
                connect_to_session_button.click()
                i += 1
                if (self.is_element_present(driver, locator_chat) == True):
                    print("Агент нашел Чат Клиента в ", i, " очереди")
                    break
        time.sleep(5)
        if (self.is_element_present(driver, locator_chat) != True):
            print("ОШИБКА!!! Чат Клиента не обнаружен ни среди активных чатов, ни в очереди!")
        assert (self.is_element_present(driver, locator_chat) == True)
        #Подключение Агента к Чату
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

    @allure.step('АРМ РИЦ: Завершение Агентом всех активных Чатов')
    def agent_completion_chat(self):
        driver = self.driver
        i = 0
        while len(driver.find_elements_by_xpath("//button[contains(@name,'CloseSession') and @class='HelperButton']")) > 0:
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
            i = i + 1
        print("Агент завершил Чатов:", i)

    # BASIC METHODS

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

    #Проверка существования элемента(для использования в методах application.py)
    def is_element_present(self, driver, locator):
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    #Проверка существования элемента(для использования во внешних методах)
    def is_element_present_main(self, locator, wait=10):
        driver = self.driver
        try:
            WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    #Проверка видимости элемента для использования во внешних методах)
    def is_element_visible_main(self, locator):
        driver = self.driver
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    #Подсчет количества эементов(для использования во внешних методах)
    def count_of_elements_main(self, elements):
        driver = self.driver
        count = len(driver.find_elements_by_xpath(elements))
        return count

    def destroy(self):
        self.driver.quit()