import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os

# Добавляем корень проекта в PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()



# Добавим хук для скриншотов в отчёт Allure при падении
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Не удалось сделать скриншот: {e}")



# Логирование действий во время тестов
import logging

@pytest.fixture(autouse=True)
def log_test_start_and_end(request):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info(f"🟢 START TEST: {request.node.name}")
    yield
    logging.info(f"🔴 END TEST: {request.node.name}")

