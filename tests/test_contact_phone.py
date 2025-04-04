import allure
from pages.contact_page import ContactPage

@allure.title("Проверка `tel:` ссылки на номер телефона")
@allure.severity(allure.severity_level.CRITICAL)
def test_phone_link(driver):
    contact = ContactPage(driver)

    with allure.step("Открываем страницу контактов"):
        contact.open()

    with allure.step("Получаем href из ссылки"):
        href = contact.get_phone_href()

    with allure.step("Проверяем, что href начинается с tel:"):
        assert href.startswith("tel:"), f"Ссылка не начинается с tel:, а выглядит как: {href}"

    with allure.step("Проверяем, что номер содержит +420"):
        assert "+420" in href, f"Ожидался номер с кодом +420, но получено: {href}"
