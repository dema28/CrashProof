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


@allure.epic("Responsiveness")
@allure.feature("Main Page")
@allure.title("Menu items are clickable and lead to correct sections (mobile)")
def test_mobile_nav_links_clickable(mobile_driver):
    page = MainPage(mobile_driver)

    with allure.step("Opening the main page"):
        page.open()

    with allure.step("Opening burger menu"):
        page.open_menu()

    links = page.get_nav_links()
    assert len(links) > 0, "Menu is empty"

    nav_items = [
        (link.text.strip(), link.get_attribute("href")) for link in links
    ]

    for link_text, href in nav_items:
        if not link_text or not href or "#" not in href:
            continue

        with allure.step(f"Clicking on '{link_text}' and verifying navigation to {href}"):
            page.open()
            page.open_menu()
            page.click_nav_link_by_text(link_text)
            expected_anchor = href.split("#")[-1]

            assert page.current_url_contains(expected_anchor), f"URL does not contain anchor '{expected_anchor}'"

            try:
                element = mobile_driver.find_element("id", expected_anchor)
                assert element.is_displayed(), f"Element with id='{expected_anchor}' is not visible"
            except NoSuchElementException:
                assert False, f"Element with id='{expected_anchor}' not found on the page"
