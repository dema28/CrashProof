from time import sleep

import allure
import pytest

from pages.contact_page import ContactPage

@allure.title("Форма обратной связи: Негативный сценарий (пустые обязательные поля)")
def test_contact_form_negative(driver):
    page = ContactPage(driver)
    page.open()
    page.scroll_to_form()
    sleep(1)
    page.fill_form(name="",
                   příjmení="Bellham",
                   email="",
                   telephon="(808)4191693",
                   message="envisioneer impactful initiatives")
    try:
        page.select_subject("Dotaz na projekt")
    except:
        pytest.fail("выбор темы не удался")
    page.submit()

    assert page.is_form_invalid(), "Ожидалась невалидная форма при пустых полях"
