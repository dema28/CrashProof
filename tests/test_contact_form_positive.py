from time import sleep
import allure
import pytest
from selenium.webdriver.common.by import By

from pages.contact_page import ContactPage
from configs.test_data import VALID_USER


@allure.title("Форма обратной связи: Позитивный сценарий (валидные данные)")
def test_contact_form_positive(driver):
    page = ContactPage(driver)
    page.open()
    page.scroll_to_form()
    sleep(1)

    page.fill_form(name=VALID_USER["name"],
                   příjmení=VALID_USER["surname"],
                   email=VALID_USER["email"],
                   telephon=VALID_USER["telephon"],
                   message=VALID_USER["message"])

    try:
        page.select_subject("Dotaz na projekt")
    except:
        pytest.fail("Выбор темы не удался")

    page.submit()

    with allure.step("Проверка наличия сообщения об успешной отправке"):
        if not page.is_success_alert_visible():
            # Вставляем скриншот в Allure
            allure.attach(driver.get_screenshot_as_png(),
                          name="no_success_alert",
                          attachment_type=allure.attachment_type.PNG)

            # Выводим все p.framer-text
            paragraphs = driver.find_elements(By.CSS_SELECTOR, "p.framer-text")
            print("🔍 Содержимое всех <p class='framer-text'> элементов:")
            for i, p in enumerate(paragraphs):
                print(f"  [{i}] {p.text.strip()}")

            # Сохраняем html (можно потом загрузить через CI)
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)

            pytest.fail("Сообщение об успешной отправке не найдено")

        else:
            print("Успешное сообщение отображается корректно")
