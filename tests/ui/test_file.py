from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
import json

def save_to_txt(data, filename="products.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        for item in data:
            file.write(f"Название: {item['name']}\n")
            file.write(f"Описание: {item['description']}\n")
            file.write(f"Цена: {item['price']}\n")
            file.write("----\n")
    print(f"Данные сохранены в {filename}")

def save_to_json(data, filename="products.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Данные сохранены в файл {filename}")

def click_element(xpath, wait, driver):
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        return True
    except (TimeoutException, NoSuchElementException) as ex:
        print(f"Ошибка при клике на {xpath}: {ex}")
        return False

def extract_product_data(driver, wait):
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='product-box']")))
        products = driver.find_elements(By.XPATH, "//*[@class='product-box']")
        product_data = []

        for product in products:
            try:
                name = product.find_element(By.XPATH, ".//h3[@class='item-title']/a").text.strip()
                description = product.find_element(By.XPATH, ".//div[contains(@class, 'item-description')]//p").text.strip()
                price = product.find_element(By.XPATH, ".//div[contains(@class, 'actual')]").text.strip()

                if name and price:
                    product_data.append({"name": name, "description": description, "price": price})
            except NoSuchElementException:
                print("Элемент не найден, пропуск товара")
            except StaleElementReferenceException:
                print("Элемент устарел, повторный поиск...")
                products = driver.find_elements(By.XPATH, "//*[@class='product-box']")
                continue

        return product_data
    except Exception as ex:
        print(f"Ошибка при извлечении данных о товарах: {ex}")
        return []

def price_sorting(driver, wait):
    driver.get("https://www.datart.cz/")
    click_element("//button[@id='c-p-bn']", wait, driver)
    click_element("//nav//li[contains(.//strong, 'Telefony')]", wait, driver)
    click_element("//snippet//div[4]/a/div", wait, driver)
    # click_element("//*[@class='sort-panel-slider-item']/a[normalize-space(text())='Nejlevnější']", wait, driver)
    # click_element("//*[@id='sort-panel-slider-tabs']/li[1]/a", wait, driver)

    # wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='product-box']")))

    data = extract_product_data(driver, wait)
    save_to_txt(data)
    save_to_json(data)

options = webdriver.ChromeOptions()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

price_sorting(driver, wait)

driver.quit()