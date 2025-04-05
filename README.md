# Автоматизация тестирования сайта MMV MODUL s.r.o.

![UI Tests](https://github.com/dema28/CrashProof/actions/workflows/UI_Tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10-blue)
![Allure](https://img.shields.io/badge/Allure-enabled-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Описание проекта

Этот проект представляет собой автоматизацию тестирования сайта [MMV MODUL s.r.o.](https://modultest1.framer.website), компании, занимающейся модульными домами.  

Тестирование осуществляется по модели **Page Object Model (POM)** с использованием:
- `pytest`
- `selenium`
- `allure-pytest`
- `GitHub Actions` для CI/CD

---

## Стек технологий

| Категория      | Инструменты                               |
|----------------|--------------------------------------------|
| Язык           | Python 3.10                                |
| UI тесты       | Selenium + PyTest                          |
| Отчётность     | Allure Reports                             |
| CI/CD          | GitHub Actions                             |
| Скриншоты      | Автосоздание при падении                   |
| Логирование    | Allure + error_log.txt + терминал          |

---

## Структура проекта

```
CrashProof/
├── .github/workflows/             # GitHub Actions CI
│   └── UI_Tests.yml
├── pages/                         # Page Object классы
│   ├── base_page.py
│   ├── catalog_page.py
│   ├── contact_page.py
│   ├── gallery_album_page.py
│   ├── gallery_page.py
│   ├── main_page.py
│   └── not_found_page.py
├── tests/                         # Тесты PyTest
│   ├── test_contact_form_negative.py
│   ├── test_contact_form_positive.py
│   ├── test_contact_phone.py
│   ├── test_gallery_albums.py
│   ├── test_main_page.py
│   ├── test_main_page_mobile.py
│   └── test_not_found_page.py
├── configs/                       # (если используется)
├── reports/                       # (опционально, может хранить HTML-отчёты)
├── allure-results/                # Allure: результаты
├── allure-report/                 # Allure: HTML отчёты
├── conftest.py                    # Общие фикстуры, хуки, логика Allure
├── requirements.txt               # Все зависимости проекта
├── README.md                      # Описание проекта
├── README_AUTOTESTS.md            # Таблица команд и локальный запуск
├── LICENSE.txt                    # Лицензия
└── CrashProof.png                 # Логотип проекта
```

---

## Запуск тестов

См. [README_AUTOTESTS.md](./README_AUTOTESTS.md) — содержит все команды (Windows и Linux), включая:
- активацию виртуального окружения
- запуск с Allure
- отчёты
- удаление старых результатов
- запуск конкретного теста

---

## Поддержка

- Автоматическая очистка `allure-results`, `allure-report` и `error_log.txt` перед тестами
- Скриншот при падении каждого теста
- Лог ошибок в `error_log.txt`

---

## Лицензия

Проект распространяется под лицензией **MIT**.  
Автор: **Denis Novicov** | QA Manual & Automation Engineer 🇨🇿

