def test_site_loads(driver):
    driver.get("https://modultest1.framer.website")
    assert "Modulconstruct - Líšnice" in driver.title
