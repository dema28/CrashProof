
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ButtonsPage:
    DOUBLE_CLICK_BUTTON = (By.XPATH, "//*[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.XPATH, "//*[@id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    DOUBLE_CLICK_MESSAGE = (By.XPATH, "//*[@id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.XPATH, "//*[@id='rightClickMessage']")
    DYNAMIC_CLICK_MESSAGE = (By.XPATH, "//*[@id='dynamicClickMessage']")

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get("https://demoqa.com/buttons")

    def double_click_button(self):
        button = self.driver.find_element(self.DOUBLE_CLICK_BUTTON)
        self.actions.double_click(button).perform()

    def right_click_button(self):
        button = self.driver.find_element(self.RIGHT_CLICK_BUTTON)
        self.actions.context_click(button).perform()

    def click_me_button(self):
        button = self.driver.find_element(self.CLICK_ME_BUTTON)
        self.actions.click(button).perform()


    def get_double_click_message(self):
        return self.driver.find_element(self.DOUBLE_CLICK_MESSAGE).text

    def get_right_click_message(self):
        return self.driver.find_element(self.RIGHT_CLICK_MESSAGE).text

    def get_dynamic_click_message(self):
        return self.driver.find_element(self.DYNAMIC_CLICK_MESSAGE).text