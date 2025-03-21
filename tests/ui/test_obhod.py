import random

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")  # Режим без графического интерфейса
# options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def get_cart_count():
    """
    Получает количество товаров в корзине из элемента.
    """
    try:
        cart_count_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@id="checkout_items" and @class="checkout_items"]'))
        )
        cart_count = int(cart_count_element.text)
        return cart_count
    except Exception as e:
        print(f"Не удалось получить количество товаров в корзине: {e}")
        return None


def check_cart_count(expected_count):
    """
    Проверяет, совпадает ли количество товаров в корзине с ожидаемым значением.
    """
    cart_count = get_cart_count()
    if cart_count is not None:
        if cart_count != expected_count:
            print(f"Ошибка: количество товаров в корзине ({cart_count}) не совпадает с ожидаемым ({expected_count})")
        else:
            print(f"Количество товаров в корзине совпадает: {cart_count}")
    else:
        print("Не удалось получить количество товаров в корзине.")


def add_to_cart_test():
    """
    Основная функция для добавления товаров в корзину и проверки их количества.
    """
    driver.get("https://www.dracek.cz/")

    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='__cookiesNlink __cookiesSuccess']"))
        )
        cookie_button.click()
    except TimeoutException:
        print("Куки уже приняты или кнопка не найдена.")

    try:
        categories = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[@class='mega-drop-down']"))
        )

        if categories:
            random_category = random.choice(categories)
            random_category.click()
            print("Перешли в случайную категорию.")
        else:
            print("Категории не найдены.")
            driver.quit()
            return

        added_products = 0
        total_product_count = 32
        added_product_ids = set()

        while added_products < total_product_count:
            products = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-item']"))
            )

            for product in products:
                if added_products >= total_product_count:
                    break

                try:
                    product_id = product.get_attribute("data-product-id")
                    if not product_id:
                        product_id = product.find_element(By.XPATH, ".//*[@class='list_code']").text

                    if product_id in added_product_ids:
                        print(f"Товар {product_id} уже добавлен, пропускаем.")
                        continue

                    add_to_cart_button = product.find_element(By.XPATH, ".//a[@class='btn main-action buyButton']")

                    time.sleep(1)
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
                    driver.execute_script("arguments[0].click();", add_to_cart_button)

                    try:
                        back_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//a[@class='btn modalGreyButton btn-lg dCloseModal']"))
                        )
                        back_button.click()
                        time.sleep(1)
                    except Exception:
                        pass

                    added_product_ids.add(product_id)
                    added_products += 1
                    print(f"Добавлено товаров: {added_products} (ID: {product_id})")

                except Exception as e:
                    print(f"Ошибка при добавлении товара: {e}")
                    continue

            if added_products < total_product_count:
                try:
                    next_page_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn j-more-products nextProducts']"))
                    )
                    next_page_button.click()
                    print("Переход на следующую страницу.")
                    time.sleep(2)
                except Exception:
                    print("Не удалось перейти на следующую страницу.")
                    break

        check_cart_count(added_products)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        driver.quit()

add_to_cart_test()