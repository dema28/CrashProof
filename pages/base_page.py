import time

from selenium.common import StaleElementReferenceException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)


    def retry_on_stale(retries=3, delay=0.5):
        def decorator(func):
            def wrapper(*args, **kwargs):
                last_exception = None
                for attempt in range(retries):
                    try:
                        return func(*args, **kwargs)
                    except StaleElementReferenceException as e:
                        last_exception = e
                        time.sleep(delay)
                raise last_exception

            return wrapper

        return decorator
