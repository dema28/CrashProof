import allure
from pages.contact_page import ContactPage

@allure.title("Check `tel:` link to phone number")
@allure.severity(allure.severity_level.CRITICAL)
def test_phone_link(driver):
    contact = ContactPage(driver)

    with allure.step("Opening contact page"):
        contact.open()

    with allure.step("Getting href from link"):
        href = contact.get_phone_href()

    with allure.step("Verifying that href starts with tel:"):
        assert href.startswith("tel:"), f"Link doesn't start with tel:, actual:  {href}"

    with allure.step("Verifying the number contains +420"):
        assert "+420" in href, f"Expected number with +420, got:  {href}"
