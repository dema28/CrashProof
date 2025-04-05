import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from pages.main_page import MainPage


@pytest.fixture
def mobile_driver():
    mobile_emulation = {"deviceName": "iPhone X"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.epic("Адаптивность")
@allure.feature("Главная страница")
@allure.title("Пункты меню кликабельны и ведут на нужные секции (мобильная версия)")
def test_mobile_nav_links_clickable(mobile_driver):
    page = MainPage(mobile_driver)

    with allure.step("Открываем главную страницу"):
        page.open()

    with allure.step("Открываем бургер-меню"):
        page.open_menu()

    links = page.get_nav_links()
    assert len(links) > 0, "Меню пустое"

    nav_items = [
        (link.text.strip(), link.get_attribute("href")) for link in links
    ]

    for link_text, href in nav_items:
        if not link_text or not href or "#" not in href:
            continue

        with allure.step(f"Кликаем по '{link_text}' и проверяем переход на {href}"):
            page.open()
            page.open_menu()
            page.click_nav_link_by_text(link_text)
            expected_anchor = href.split("#")[-1]

            assert page.current_url_contains(expected_anchor), f"URL не содержит якорь '{expected_anchor}'"

            try:
                element = mobile_driver.find_element("id", expected_anchor)
                assert element.is_displayed(), f"Элемент с id='{expected_anchor}' не отображается"
            except NoSuchElementException:
                assert False, f"Элемент с id='{expected_anchor}' не найден на странице"
