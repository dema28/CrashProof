import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class ContactPage(BasePage):

    URL = "https://modultest1.framer.website/kontakty"

    NAME_INPUT = (By.XPATH, "//*[@name='Křestní jméno']")
    PŘÍJMENÍ= (By.XPATH, "//*[@name='Příjmení']")
    EMAIL_INPUT = (By.XPATH, "//*[@name='E-mailová adresa']")
    TELEFON = (By.XPATH, "//*[@name='Telefon']")
    DROPDOWN_SUBJECT = (By.XPATH, "//select[@name='Předmět']")
    MESSAGE_INPUT = (By.XPATH, "//*[@name='Zpráva']")
    SUBMIT_BTN = (By.XPATH, "//button[@data-framer-name='Default']")
    SUCCESS_ALERT = (By.XPATH, "//p[text()='Děkujeme']")
    ERROR_MSG = (By.XPATH, "//div[contains(@class,'error')]")

    @allure.step("Открываем страницу контактов")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Прокручиваем к форме по XPath")
    def scroll_to_form(self):
        form_element = self.driver.find_element(By.XPATH, "//*[@id='formulář']")
        self.scroll_to(form_element)

    @allure.step("Выбираем тему обращения: {option_text}")
    def select_subject(self, option_text):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.DROPDOWN_SUBJECT)
            )
            dropdown = Select(self.driver.find_element(*self.DROPDOWN_SUBJECT))
            self.scroll_to(dropdown._el)
            dropdown.select_by_visible_text(option_text)
        except Exception as e:
            allure.attach(str(e), name="Ошибка при выборе из списка", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Заполняем форму: имя='{name}', email='{email}', сообщение='{message}'")
    def fill_form(self, name, email, message, příjmení, telephon):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.PŘÍJMENÍ).send_keys(příjmení)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.TELEFON).send_keys(telephon)
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(message)

    @allure.step("Отправляем форму")
    def submit(self):
        self.driver.find_element(*self.SUBMIT_BTN).click()

    @allure.step("Проверка успешного сообщения")
    def is_success_alert_visible(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.SUCCESS_ALERT))
            return True
        except:
            return False

    @allure.step("Проверка наличия ошибки")
    def is_error_displayed(self):
        return bool(self.driver.find_elements(*self.ERROR_MSG))
