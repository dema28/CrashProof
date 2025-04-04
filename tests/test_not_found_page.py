import pytest
import requests
import allure
from selenium.common import NoSuchElementException

from pages.not_found_page import NotFoundPage

@allure.title("Проверка, что несуществующая страница возвращает статус 404")
@allure.severity(allure.severity_level.CRITICAL)
def test_404_status_code():
    url = "https://notmodultest1.framer.website"
    response = requests.get(url)
    assert response.status_code == 404, f"Ожидался статус 404, но получен: {response.status_code}"

@allure.title("Проверка UI отображения кастомной страницы 404")
@allure.description("Проверяется наличие заголовка '404 - Stránka nebyla nalezena'")
@allure.severity(allure.severity_level.CRITICAL)
def test_404_page_ui(driver):
    url = "https://modultest1.framer.website/nic-tady-neni"
    driver.get(url)

    page = NotFoundPage(driver)
    try:
        heading = page.get_heading_text()
        assert "404 - Stránka nebyla nalezena" in heading, f"Найден заголовок: {heading}"
    except NoSuchElementException as e:
        allure.attach(driver.get_screenshot_as_png(),
            name="404 - Stránka nebyla nalezena",
            attachment_type=allure.attachment_type.PNG)
        pytest.fail("Элемент с заголовком 404 не найден", pytrace=True)
