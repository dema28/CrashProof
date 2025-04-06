# Automated Testing for MMV MODUL s.r.o. Website

![UI Tests](https://github.com/dema28/CrashProof/actions/workflows/UI_Tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10-blue)
![Allure](https://img.shields.io/badge/Allure-enabled-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Project Description

This project represents automated testing of the website [MMV MODUL s.r.o.](https://modultest1.framer.website), a company specializing in modular houses.  

Testing is based on the **Page Object Model (POM)** using the following tools:
- `pytest`
- `selenium`
- `allure-pytest`
- `GitHub Actions` для CI/CD

---

## Tech Stack

| Category       | Tools                                      |
|----------------|--------------------------------------------|
| Language        | Python 3.10                                |
| UI Tests        | Selenium + PyTest                          |
| Reporting       | Allure Reports                             |
| CI/CD          | GitHub Actions                             |
| Screenshots     | Auto-generated on failure                  |
| Logging         | Allure + error_log.txt + terminal          |

---

## Project Structure

```
CrashProof/
├── .github/workflows/             # GitHub Actions CI
│   └── UI_Tests.yml
├── pages/                         # Page Object classes
│   ├── base_page.py
│   ├── catalog_page.py
│   ├── contact_page.py
│   ├── gallery_album_page.py
│   ├── gallery_page.py
│   ├── main_page.py
│   └── not_found_page.py
├── tests/                         # PyTest tests
│   ├── test_contact_form_negative.py
│   ├── test_contact_form_positive.py
│   ├── test_contact_phone.py
│   ├── test_gallery_albums.py
│   ├── test_main_page.py
│   ├── test_main_page_mobile.py
│   └── test_not_found_page.py
├── configs/                       # (if used)
├── reports/                       # (optional, may store HTML reports)
├── allure-results/                # Allure: results
├── allure-report/                 # Allure: HTML reports
├── conftest.py                    # Shared fixtures, hooks, Allure logic
├── requirements.txt               # Все зависимости проекта
├── README.md                      # Project description
├── README_AUTOTESTS.md            # Command table and local run guide
├── LICENSE.txt                    # License
└── CrashProof.png                 # Логотип проекта
```

---

## Running Tests

See [README_AUTOTESTS.md](./README_AUTOTESTS.md) — contains all commands (Windows and Linux), including:
- activating virtual environment
- running with Allure
- reports
- deleting old results
- running a specific test

---

## Features

- Automatic cleanup of `allure-results`, `allure-report` и `error_log.txt` перед тестами
- Screenshot on each test failure
- Error log in `error_log.txt`

---

## License

The project is distributed under the **MIT**.  
Author: **Denis Novicov** | QA Manual & Automation Engineer 🇨🇿

