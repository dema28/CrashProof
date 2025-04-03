class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
