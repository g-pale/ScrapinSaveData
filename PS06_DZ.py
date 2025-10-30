import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Настройка Chrome
chrome_options = Options()
chrome_options.add_argument('--headless=new')  # современный headless-режим
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
chrome_options.add_argument('--remote-allow-origins=*')
chrome_options.page_load_strategy = 'none'  # не ждать полной загрузки

# Инициализация через Selenium Manager (без webdriver_manager)
driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(90)
driver.implicitly_wait(5)
url = "https://www.divan.ru/category/kresla"
driver.get(url)
try:
    WebDriverWait(driver, 45).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ProductCardMain_card__KQzzn"))
    )
except TimeoutException:
    pass
time.sleep(1)

divans = driver.find_elements(By.CSS_SELECTOR, ".ProductCardMain_card__KQzzn")

parsed_data = []
for divan in divans:
    try:
        # Название товара извлекаем из alt атрибута изображения
        name = divan.find_element(By.CSS_SELECTOR, 'img[itemProp="image"]').get_attribute("alt")
        price = divan.find_element(By.CSS_SELECTOR, 'span[data-testid="price"]').text
        link = divan.find_element(By.CSS_SELECTOR, 'link[itemProp="url"]').get_attribute("href")
    except Exception as e:
        print(f'произошла ошибка при парсинге данных: {e}')
        continue
    parsed_data.append([name, price, link])

driver.quit()

with open('divans.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'price', 'link'])
    writer.writerows(parsed_data)
print('данные успешно сохранены в файл divans.csv')