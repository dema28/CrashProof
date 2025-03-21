import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class SimpleUITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        cls.wait = WebDriverWait(cls.driver, 10)

    def setUp(self):
        self.driver.get("https://demoqa.com/buttons")

    def test_btn_double_click(self):
        btn_double_click = self.wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
        btn_right_click = self.wait.until(EC.element_to_be_clickable((By.ID, "rightClickBtn")))
        btn_click = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click Me']")))

        actions = ActionChains(self.driver)
        actions.double_click(btn_double_click).perform()
        actions.context_click(btn_right_click).perform()
        actions.click(btn_click).perform()

        message = self.wait.until(EC.visibility_of_element_located((By.ID, "doubleClickMessage")))
        message1 = self.wait.until(EC.visibility_of_element_located((By.ID, "rightClickMessage")))
        message2 = self.wait.until(EC.visibility_of_element_located((By.ID, "dynamicClickMessage")))

        self.assertEqual(message.text, "You have done a double click")
        self.assertEqual(message1.text, "You have done a right click")
        self.assertEqual(message2.text, "You have done a dynamic click")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
