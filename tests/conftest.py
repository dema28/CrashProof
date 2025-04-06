import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os
import allure
import shutil
import logging
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for folder in [os.path.join(project_root, 'allure-results'), os.path.join(project_root, 'allure-report')]:
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Error: {e}")
        else:
            os.makedirs(folder)

    error_log = os.path.join(project_root, "error_log.txt")
    if os.path.exists(error_log):
        try:
            os.remove(error_log)
            print("[INFO] Old error_log.txt deleted")
        except Exception as e:
            print(f"[WARNING] Failed to delete error_log.txt: {e}")


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("CI") == "true":
        options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Failed to take screenshot: {e}")
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        error_log = os.path.join(project_root, "error_log.txt")
        with open(error_log, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] Error in test: {item.nodeid}\n")


@pytest.fixture(autouse=True)
def log_test_start_and_end(request):
    logging.getLogger().handlers.clear()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info(f"🟢 START TEST: {request.node.name}")
    yield
    logging.info(f"🔴 END TEST: {request.node.name}")
