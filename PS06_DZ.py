import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Настройка Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')  # Запуск в фоновом режиме
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

# Автоматическое управление драйвером
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
url = "https://www.divan.ru/category/kresla"
driver.get(url)
time.sleep(5)

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