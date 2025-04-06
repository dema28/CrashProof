from time import sleep

import allure
import pytest

from pages.contact_page import ContactPage
from configs.test_data import INVALID_USER

@allure.title("Contact Form: Negative Scenario (empty required fields)")
def test_contact_form_negative(driver):
    page = ContactPage(driver)
    page.open()
    page.scroll_to_form()
    sleep(1)
    page.fill_form(name=INVALID_USER["name"],
                   příjmení=INVALID_USER["surname"],
                   email=INVALID_USER["email"],
                   telephon=INVALID_USER["telephon"],
                   message=INVALID_USER["message"])
    try:
        page.select_subject("Dotaz na projekt")
    except:
        pytest.fail("Topic selection failed")
    page.submit()

    assert page.is_form_invalid(), "Expected the form to be invalid with empty fields"
