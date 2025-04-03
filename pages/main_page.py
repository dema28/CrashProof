import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By




class MainPage(BasePage):
    URL = "https://modultest1.framer.website"

    @allure.step("Открываем главную страницу")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Проверяем наличие ключевого слова в заголовке")
    def page_title_is_present(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.title_contains("Modulconstruct - Líšnice"))
            return True
        except:
            return False
