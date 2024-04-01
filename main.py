import os
from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

GIT_URL = 'https://github.com/Urunar/hh-bot/blob/1ae6f110d0147e0bc0ea013e1bb70310770e40fa/main.py'
BASE_URL = 'https://dzerzhinskij.hh.ru/account/login?backurl=%2F%3FcustomDomain%3D1&hhtmFrom=main'
URL = 'https://hh.ru/search/vacancy?employment=full&employment=part&schedule=remote&ored_clusters=true&items_on_page=100&search_field=name&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line&enable_snippets=false&experience=between1And3&text=QA%2C+%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80*'
LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']
letter = f"Резюме направлено автокликером, написанным мной.\nкод на гитхабе: {GIT_URL}\n\nЕсли мою резюме не подходит, извините, что потратил ваше время"

class HH_clicker:

    def __init__(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_experimental_option("detach", True)
        chrome_opts.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=chrome_opts)

    def login(self):
        url = BASE_URL
        self.driver.get(url)
        sleep(1)
        self.driver.execute_script("window.stop();")
        # принять куки
        self.driver.find_element(By.CSS_SELECTOR, value='button[data-qa="cookies-policy-informer-accept"]').click()
        #принять локацию
        self.driver.find_element(By.CSS_SELECTOR, value='button[data-qa="region-clarification-confirm"]').click()
        sleep(0.5)

        # press 'войти с паролем'
        self.driver.find_element(By.CSS_SELECTOR, value='button[data-qa="expand-login-by-password"]').click()
        sleep(0.5)
        field_login = self.driver.find_element(By.CSS_SELECTOR, value='input[data-qa="login-input-username"]')
        field_login.send_keys(LOGIN)
        field_login.send_keys(Keys.TAB)
        sleep(0.5)
        field_pass = self.driver.switch_to.active_element
        field_pass.send_keys(PASSWORD)
        sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR, value='button[data-qa="account-login-submit"]').click()
        sleep(0.5)

    def find_vacancies(self):
        self.driver.get(URL)
        sleep(10)

    def ot_click(self):
        self.driver.find_element(By.CSS_SELECTOR, value='a[data-qa="vacancy-serp__vacancy_response"]').click()
        try:
            self.driver.find_element(By.CSS_SELECTOR, value='button["data-qa="vacancy-response-letter-toggle""]').click()
            sleep(0.5)
            self.driver.find_element(By.CSS_SELECTOR, value='textarea[name="text"]').send_keys()
        except NoSuchElementException:
            pass
        # найти все кнопки "откликнуться" на странице
        # all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='a[data-qa="vacancy-serp__vacancy_response"]')
        # # если такие есть, длина списка больше 0
        # if len(all_buttons) > 0:
        #     # клик на каждую. Если есть поле для сопроводительного письма, вставляем текст, отправляем
        #     for button in all_buttons:
        #         button.click()









bot = HH_clicker()
bot.login()
bot.find_vacancies()
bot.ot_click()








