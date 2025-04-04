import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os
import allure
import shutil
import logging
from datetime import datetime


# Безопасно очищаем содержимое папок Allure и удаляем error_log.txt
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
                    print(f"Не удалось удалить {file_path}. Ошибка: {e}")
        else:
            os.makedirs(folder)

    # Удаляем старый лог ошибок
    error_log = os.path.join(project_root, "error_log.txt")
    if os.path.exists(error_log):
        try:
            os.remove(error_log)
            print("[INFO] Удалён старый error_log.txt")
        except Exception as e:
            print(f"[WARNING] Не удалось удалить error_log.txt: {e}")


# Добавляем корень проекта в PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))


# Фикстура для WebDriver
@pytest.fixture
def driver():
    options = Options()
    if os.getenv("CI") == "true":
        options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# Скриншот + лог ошибок в Allure и файл
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
                print(f"Не удалось сделать скриншот: {e}")
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        error_log = os.path.join(project_root, "error_log.txt")
        with open(error_log, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] Ошибка в тесте: {item.nodeid}\n")


# Логирование начала и завершения тестов
@pytest.fixture(autouse=True)
def log_test_start_and_end(request):
    logging.getLogger().handlers.clear()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info(f"🟢 START TEST: {request.node.name}")
    yield
    logging.info(f"🔴 END TEST: {request.node.name}")
