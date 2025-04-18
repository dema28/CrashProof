
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

class MainPage(BasePage):
    URL = "https://modultest1.framer.website"
    MENU_BUTTON = (By.XPATH, "//*[@class='framer-sjc5ez']")
    NAV_LINKS = (By.CSS_SELECTOR, "div[data-framer-name='Links'] a[href]")

    @staticmethod
    def retry_on_stale(retries=3, delay=0.5):
        def decorator(func):
            def wrapper(*args, **kwargs):
                last_exception = None
                for attempt in range(retries):
                    try:
                        return func(*args, **kwargs)
                    except StaleElementReferenceException as e:
                        last_exception = e
                        time.sleep(delay)
                raise last_exception
            return wrapper
        return decorator

    @allure.step("Opening the main page")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Checking for keyword in page title")
    def page_title_is_present(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.title_contains("Modulconstruct - Líšnice"))
            return True
        except:
            return False

    @allure.step("Checking burger menu button visibility")
    def is_menu_button_visible(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.MENU_BUTTON)
            )
            return element.is_displayed()
        except:
            return False

    @allure.step("Opening the menu")
    def open_menu(self):
        for _ in range(3):  # Manual retry
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(self.MENU_BUTTON)
                )
                element.click()
                return
            except StaleElementReferenceException:
                time.sleep(0.5)
        raise Exception("Failed to click the menu button — stale element")

    @allure.step("Retrieving menu items")
    @retry_on_stale()
    def get_nav_links(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.NAV_LINKS)
        )

    @allure.step("Clicking the link '{link_text}'")
    @retry_on_stale()
    def click_nav_link_by_text(self, link_text):
        links = self.get_nav_links()
        for link in links:
            if link_text.lower() in link.text.strip().lower():
                link.click()
                return
        raise Exception(f"Link with text '{link_text}' not found")

    @allure.step("Verifying that URL contains '{expected_part}'")
    def current_url_contains(self, expected_part):
        WebDriverWait(self.driver, 5).until(
            EC.url_contains(expected_part)
        )
        return expected_part in self.driver.current_url
