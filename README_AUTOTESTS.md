# Instructions for Running Automated Tests with Allure

## For Windows (CMD / PowerShell)

| №  | Action                                  | Команда                                                             |
|----|-------------------------------------------|---------------------------------------------------------------------|
| 1  | Activate virtual environment        | `.venv\Scripts\activate`                                            |
| 2  | Install dependencies                    | `pip install -r requirements.txt`                                   |
| 3  | Run all tests (without Allure)          | `pytest tests/`                                                     |
| 4  | Run tests with Allure results     | `pytest tests/ --alluredir=allure-results`                          |
| 5  | Generate Allure report                | `allure generate allure-results --clean -o allure-report`           |
| 6  | Open Allure report in browser           | `allure open allure-report`                                         |
| 7  | Run a specific test            | `pytest tests/test_main_page.py::test_smoke_main_page`              |
| 8  | Run with logs in console                 | `pytest tests/ --capture=tee-sys -v`                                |
| 9  | Delete old Allure results and reports | `rmdir /s /q allure-results`<br>`rmdir /s /q allure-report`         |


## For Linux / macOS / CI

| №  | Action                                  | Команда                                                             |
|----|-------------------------------------------|---------------------------------------------------------------------|
| 1  | Activate virtual environment        | `source .venv/bin/activate`                                         |
| 2  | Install dependencies                    | `pip install -r requirements.txt`                                   |
| 3  | Run all tests (without Allure)          | `pytest tests/`                                                     |
| 4  | Run tests with Allure results     | `pytest tests/ --alluredir=allure-results`                          |
| 5  | Generate Allure report                | `allure generate allure-results --clean -o allure-report`           |
| 6  | Open Allure report in browser           | `allure open allure-report`                                         |
| 7  | Run a specific test            | `pytest tests/test_main_page.py::test_smoke_main_page`              |
| 8  | Run with logs in console                 | `pytest tests/ --capture=tee-sys -v`                                |
| 9  | Delete old Allure results and reports | `rm -rf allure-results allure-report`                               |
