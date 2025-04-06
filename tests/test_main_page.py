import allure
from pages.main_page import MainPage


@allure.title("Smoke: Loading the Main Page")
def test_smoke_main_page(driver):
    page = MainPage(driver)

    with allure.step("Opening the main page"):
        page.open()

    with allure.step("Verifying that the title contains 'Modulconstruct - Líšnice'"):
        assert page.page_title_is_present(), "The page title does not contain the expected text 'Modulconstruct - Líšnice'"


