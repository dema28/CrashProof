from time import sleep
import allure
import pytest

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
        assert page.is_success_alert_visible(), "Сообщение об успешной отправке не найдено"

