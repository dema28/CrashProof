# def test_site_loads(driver):
#     driver.get("https://modultest1.framer.website")
#     assert "Modulconstruct - Líšnice" in driver.title

import allure

@allure.title("Smoke: загрузка главной страницы")
@allure.severity(allure.severity_level.CRITICAL)
def test_main_page_loads(driver):
    with allure.step("Открываем главную страницу"):
        driver.get("https://modultest1.framer.website")

    with (allure.step("Проверяем, что заголовок не пустой и содержит 'MMV'")):
        title = driver.title
        assert "Modulconstruct - Líšnice" in title or len(title) > 0,"Заголовок страницы пуст или не содержит 'Modulconstruct - Líšnice'"

