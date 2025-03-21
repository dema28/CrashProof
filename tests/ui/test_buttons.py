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
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_btn_double_click(self):
        self.driver.get("https://demoqa.com/buttons")

        # Ожидание кликабельности перед кликом
        btn_double_click = self.wait.until(
            EC.element_to_be_clickable((By.ID, "doubleClickBtn"))
        )

        actions = ActionChains(self.driver)
        actions.double_click(btn_double_click).perform()

        time.sleep(1)  # Временное ожидание для диагностики

        # Выводим страницу в лог, если элемент не найден
        try:
            message = self.wait.until(
                EC.visibility_of_element_located((By.ID, "doubleClickMessage"))
            )
            self.assertEqual(message.text, "You have done a double click")
        except Exception as e:
            print("Page Source:", self.driver.page_source)
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
