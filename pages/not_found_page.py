from selenium.webdriver.common.by import By

class NotFoundPage:
    def __init__(self, driver):
        self.driver = driver
        self.heading = (By.XPATH, "//*[text()='404 - Stránka nebyla nalezena']")

    def get_heading_text(self):
        return self.driver.find_element(*self.heading).text
