import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class GalleryAlbumPage:
    def __init__(self, driver):
        self.driver = driver
        self.image_items = (By.TAG_NAME, "img")
        self.back_button = (By.XPATH, "//*[@class='framer-1epduey-container']")

    @allure.step("Подсчитываем количество изображений в альбоме")
    def get_images_count(self):
        return len(self.driver.find_elements(*self.image_items))

    @allure.step("Возвращаемся к списку альбомов")
    def go_back_to_gallery(self):
        wait = WebDriverWait(self.driver, 10)
        max_attempts = 3

        for attempt in range(max_attempts):
            try:
                element = wait.until(EC.presence_of_element_located(self.back_button))
                element = wait.until(EC.element_to_be_clickable(self.back_button))
                element.click()
                return
            except StaleElementReferenceException as e:
                if attempt < max_attempts - 1:
                    print(f"[RETRY] Попытка {attempt + 1}/3: пойман StaleElement при возврате в галерею. Повтор...")
                    time.sleep(1)
                else:
                    raise e
