import allure
from pages.main_page import MainPage


@allure.title("Smoke: Загрузка главной страницы")
def test_smoke_main_page(driver):
    page = MainPage(driver)

    with allure.step("Открываем главную страницу"):
        page.open()

    with allure.step("Проверяем, что заголовок содержит 'Modulconstruct - Líšnice'"):
        assert page.page_title_is_present()



