import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.ui.HomeWork_39_POM.pages.buttons_page import ButtonsPage
from tests.ui.HomeWork_39_POM.utils.driver_manager import DriverManager


class TestButtons(unittest.TestCase):
    def setUp(self):
        self.driver = DriverManager.create_driver()
        self.buttons_page = ButtonsPage(self.driver)
        self.buttons_page.open()
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def test_double_click(self):
        btn_double_click = self.wait.until(
            EC.element_to_be_clickable(self.buttons_page.DOUBLE_CLICK_BUTTON)
        )
        self.actions.double_click(btn_double_click).perform()

        message = self.wait.until(
            EC.visibility_of_element_located(self.buttons_page.DOUBLE_CLICK_MESSAGE)
        )
        self.assertEqual(message.text, "You have done a double click")

    def test_right_click(self):
        btn_right_click = self.wait.until(
            EC.element_to_be_clickable(self.buttons_page.RIGHT_CLICK_BUTTON)
        )
        self.actions.context_click(btn_right_click).perform()

        message = self.wait.until(
            EC.visibility_of_element_located(self.buttons_page.RIGHT_CLICK_MESSAGE)
        )
        self.assertEqual(message.text, "You have done a right click")

    def test_dynamic_click(self):
        btn_click = self.wait.until(
            EC.element_to_be_clickable(self.buttons_page.CLICK_ME_BUTTON)
        )
        self.actions.click(btn_click).perform()

        message = self.wait.until(
            EC.visibility_of_element_located(self.buttons_page.DYNAMIC_CLICK_MESSAGE)
        )
        self.assertEqual(message.text, "You have done a dynamic click")

    def tearDown(self):
        DriverManager.quit_driver(self.driver)


if __name__ == "__main__":
    unittest.main()