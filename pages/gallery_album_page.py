import allure
from selenium.webdriver.common.by import By

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
        self.driver.find_element(*self.back_button).click()
