import time

import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class GalleryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav_link = (By.XPATH, "//a[@href='./albums']")
        self.album_links = (By.XPATH, "//a[contains(@href, 'albums/')]")

    @allure.step("Переход на страницу галереи")
    def go_to_gallery(self):
        wait = WebDriverWait(self.driver, 10)
        max_attempts = 3

        for attempt in range(max_attempts):
            try:
                element = wait.until(EC.presence_of_element_located(self.nav_link))
                element = wait.until(EC.element_to_be_clickable(self.nav_link))
                self.scroll_to(element)
                element.click()
                return
            except StaleElementReferenceException as e:
                if attempt < max_attempts - 1:
                    print(f"[RETRY] Попытка {attempt + 1}/3: пойман StaleElement. Повтор...")
                    time.sleep(1)
                else:
                    raise e

    @allure.step("Получаем все альбомы")
    def get_album_elements(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.album_links)
        )
        return self.driver.find_elements(*self.album_links)

    @allure.step("Открываем альбом по индексу {index}")
    def open_album_by_index(self, index):
        albums = self.get_album_elements()
        if index < len(albums):
            ActionChains(self.driver).move_to_element(albums[index]).click().perform()

    @allure.step("Прокручиваем к альбому по индексу {index}")
    def scroll_to_album_by_index(self, index):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located(self.album_links))

        albums = self.get_album_elements()
        if index < len(albums):
            self.scroll_to(albums[index])
