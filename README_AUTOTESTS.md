# Инструкции по запуску автотестов с Allure

## Для Windows (CMD / PowerShell)

| №  | Действие                                  | Команда                                                             |
|----|-------------------------------------------|---------------------------------------------------------------------|
| 1  | Активировать виртуальное окружение        | `.venv\Scripts\activate`                                            |
| 2  | Установить зависимости                    | `pip install -r requirements.txt`                                   |
| 3  | Запустить все тесты (без Allure)          | `pytest tests/`                                                     |
| 4  | Запустить тесты с Allure-результатами     | `pytest tests/ --alluredir=allure-results`                          |
| 5  | Сгенерировать Allure-отчёт                | `allure generate allure-results --clean -o allure-report`           |
| 6  | Открыть Allure-отчёт в браузере           | `allure open allure-report`                                         |
| 7  | Запустить один конкретный тест            | `pytest tests/test_main_page.py::test_smoke_main_page`              |
| 8  | Запуск с логами в консоли                 | `pytest tests/ --capture=tee-sys -v`                                |
| 9  | Удалить старые Allure-результаты и отчёты | `rmdir /s /q allure-results`<br>`rmdir /s /q allure-report`         |


## Для Linux / macOS / CI

| №  | Действие                                  | Команда                                                             |
|----|-------------------------------------------|---------------------------------------------------------------------|
| 1  | Активировать виртуальное окружение        | `source .venv/bin/activate`                                         |
| 2  | Установить зависимости                    | `pip install -r requirements.txt`                                   |
| 3  | Запустить все тесты (без Allure)          | `pytest tests/`                                                     |
| 4  | Запустить тесты с Allure-результатами     | `pytest tests/ --alluredir=allure-results`                          |
| 5  | Сгенерировать Allure-отчёт                | `allure generate allure-results --clean -o allure-report`           |
| 6  | Открыть Allure-отчёт в браузере           | `allure open allure-report`                                         |
| 7  | Запустить один конкретный тест            | `pytest tests/test_main_page.py::test_smoke_main_page`              |
| 8  | Запуск с логами в консоли                 | `pytest tests/ --capture=tee-sys -v`                                |
| 9  | Удалить старые Allure-результаты и отчёты | `rm -rf allure-results allure-report`                               |
