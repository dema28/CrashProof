import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class ContactPage(BasePage):

    URL = "https://modultest1.framer.website/kontakty"

    NAME_INPUT = (By.XPATH, "//input[@name='Křestní jméno']")
    PŘÍJMENÍ= (By.XPATH, "//*[@name='Příjmení']")
    EMAIL_INPUT = (By.XPATH, "//*[@name='E-mailová adresa']")
    TELEFON = (By.XPATH, "//*[@name='Telefon']")
    DROPDOWN_SUBJECT = (By.XPATH, "//select[@name='Předmět']")
    MESSAGE_INPUT = (By.XPATH, "//*[@name='Zpráva']")
    SUBMIT_BTN = (By.XPATH, "//button[@data-framer-name='Default']")
    SUCCESS_ALERT = (By.XPATH, "//p[contains(@class, 'framer-text') and contains(text(), 'Děkujeme')]")
    ERROR_MSG = (By.XPATH, "//div[contains(@class,'error')]")
    PHONE_LINK = (By.XPATH, "//a[starts-with(@href, 'tel:')]")

    @allure.step("Opening contact page")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Scrolling to the form via XPath")
    def scroll_to_form(self):
        form_element = self.driver.find_element(By.XPATH, "//*[@id='formulář']")
        self.scroll_to(form_element)

    @allure.step("Selecting subject: {option_text}: {option_text}")
    def select_subject(self, option_text):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.DROPDOWN_SUBJECT)
            )
            dropdown = Select(self.driver.find_element(*self.DROPDOWN_SUBJECT))
            self.scroll_to(dropdown._el)
            dropdown.select_by_visible_text(option_text)
        except Exception as e:
            allure.attach(str(e), name="Error selecting from list", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Filling out the form: name='{name}', email='{email}', message='{message}'")
    def fill_form(self, name, email, message, příjmení, telephon):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.PŘÍJMENÍ).send_keys(příjmení)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.TELEFON).send_keys(telephon)
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(message)

    @allure.step("Submitting the form")
    def submit(self):
        self.driver.find_element(*self.SUBMIT_BTN).click()

    @allure.step("Verifying success message")
    def is_success_alert_visible(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUCCESS_ALERT)
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step("Checking for error")
    def is_error_displayed(self):
        return bool(self.driver.find_elements(*self.ERROR_MSG))

    @allure.step("Verifying the form is invalid when required fields are empty")
    def is_form_invalid(self):
        try:
            form = self.driver.find_element(By.XPATH, "//form")
            is_valid = self.driver.execute_script("return arguments[0].checkValidity();", form)
            if not is_valid:
                invalid_fields = self.driver.find_elements(By.CSS_SELECTOR,
                                                           "input:invalid, textarea:invalid, select:invalid")
                allure.attach(
                    f"Invalid fields: {len(invalid_fields)}",
                    name="HTML5 invalid fields",
                    attachment_type=allure.attachment_type.TEXT
                )
                return True
            return False
        except Exception as e:
            allure.attach(str(e), name="Error during form validation check",
                          attachment_type=allure.attachment_type.TEXT)
            return False

    @allure.step("Getting phone link href")
    def get_phone_href(self):
        try:
            phone = self.driver.find_element(*self.PHONE_LINK)
            href = phone.get_attribute("href")
            allure.attach(href, name="Phone link", attachment_type=allure.attachment_type.TEXT)
            return href
        except Exception as e:
            allure.attach(str(e), name="Error retrieving phone link",
                          attachment_type=allure.attachment_type.TEXT)
            raise