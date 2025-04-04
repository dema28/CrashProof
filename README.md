# 🧪 Автоматизация тестирования сайта MMV MODUL s.r.o.

![UI Tests](https://github.com/dema28/CrashProof/actions/workflows/UI_Tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10-blue)
![Allure](https://img.shields.io/badge/Allure-enabled-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Описание проекта

Этот проект представляет собой автоматизацию тестирования сайта [MMV MODUL s.r.o.](https://modultest1.framer.website), компании, занимающейся модульными домами.  

Тестирование осуществляется по модели **Page Object Model (POM)** с использованием:
- `pytest`
- `selenium`
- `allure-pytest`
- `GitHub Actions` для CI/CD

---

## ⚙ Стек технологий

| Категория      | Инструменты                               |
|----------------|--------------------------------------------|
| Язык           | Python 3.10                                |
| UI тесты       | Selenium + PyTest                          |
| Отчётность     | Allure Reports                             |
| CI/CD          | GitHub Actions                             |
| Скриншоты      | Автосоздание при падении                   |
| Логирование    | Allure + error_log.txt + терминал          |

---

## 📂 Структура проекта

```
CrashProof/
├── pages/                  # Page Object классы
│   ├── base_page.py
│   ├── main_page.py
│   └── contact_page.py
├── tests/                  # Тесты PyTest
│   ├── test_main_page.py
│   └── test_contact_form_*.py
├── conftest.py             # Общие фикстуры, хуки, логика Allure
├── requirements.txt        # Все зависимости проекта
├── .github/workflows/      # GitHub Actions CI
│   └── ui-tests.yml
├── README.md               # Описание проекта
└── README_AUTOTESTS.md     # Таблица команд и локальный запуск
```

---

## 🚀 Запуск тестов

📄 См. [README_AUTOTESTS.md](./README_AUTOTESTS.md) — содержит все команды (Windows и Linux), включая:
- активацию виртуального окружения
- запуск с Allure
- отчёты
- удаление старых результатов
- запуск конкретного теста

---

## 🧼 Поддержка

- Автоматическая очистка `allure-results`, `allure-report` и `error_log.txt` перед тестами
- Скриншот при падении каждого теста
- Лог ошибок в `error_log.txt`

---

## 📄 Лицензия

Проект распространяется под лицензией **MIT**.  
Автор: **Denis Novicov** | QA Manual & Automation Engineer 🇨🇿

