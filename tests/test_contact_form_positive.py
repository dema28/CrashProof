import allure
import pytest

from pages.contact_page import ContactPage


@allure.title("Форма обратной связи: Позитивный сценарий (валидные данные)")
def test_contact_form_positive(driver):
    page = ContactPage(driver)
    page.open()
    page.scroll_to_form()
    page.fill_form(name="Danny",
                   příjmení="Bellham",
                   email="dbellham0@mozilla.org",
                   telephon="(808) 4191693",
                   message="envisioneer impactful initiatives")
    try:
        page.select_subject("Dotaz na projekt")
    except:
        pytest.fail("выбор темы не удался")
    page.submit()

    assert page.is_success_alert_visible(), "Сообщение об успешной отправке не найдено"



