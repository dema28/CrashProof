import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SimpleUITest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        # chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=chrome_options)

    def test_btn_double_click(self):
        self.driver.get("https://demoqa.com/buttons")

        btn_double_click = self.driver.find_element(By.XPATH, "//*[@id='doubleClickBtn']")
        time.sleep(1)
        btn_right_click = self.driver.find_element(By.XPATH, "//*[@id='rightClickBtn']")
        time.sleep(1)
        btn_click = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
        time.sleep(1)

        actions = ActionChains(self.driver)

        actions.double_click(btn_double_click).perform()
        actions.context_click(btn_right_click).perform()
        actions.click(btn_click).perform()

        wait = WebDriverWait(self.driver, 1)

        message = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='doubleClickMessage']"))
        )

        message1 = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='rightClickMessage']"))
        )

        message2 = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='dynamicClickMessage']"))
        )

        self.assertTrue(message.is_displayed())
        self.assertEqual(message.text, "You have done a double click")

        self.assertTrue(message1.is_displayed())
        self.assertEqual(message1.text, "You have done a right click")

        self.assertTrue(message2.is_displayed())
        self.assertEqual(message2.text, "You have done a dynamic click")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()