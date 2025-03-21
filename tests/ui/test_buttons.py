import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class SimpleUITest(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")

        # Используем webdriver-manager для автоматической установки ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def test_btn_double_click(self):
        self.driver.get("https://demoqa.com/buttons")

        # Ожидание и поиск элементов
        wait = WebDriverWait(self.driver, 10)

        btn_double_click = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='doubleClickBtn']"))
        )
        btn_right_click = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='rightClickBtn']"))
        )
        btn_click = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Click Me']"))
        )

        # Выполнение действий
        actions = ActionChains(self.driver)
        actions.double_click(btn_double_click).perform()
        actions.context_click(btn_right_click).perform()
        actions.click(btn_click).perform()

        # Проверка сообщений
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
