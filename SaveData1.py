# data = [
#     ['100', '200', '300'],
#     ['400', '500', '600']
#     ]
#     # С сайта мы получаем именно списки.
# numbers = []
# for row in data:
#     for text in row:
#         number = int(text)
#         numbers.append(number)
# print(numbers)

# import time
# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
# url = "https://www.divan.ru/category/kresla"
# driver.get(url)
# time.sleep(5)

# divans = driver.find_elements(By.CSS_SELECTOR, ".ProductCardMain_card__KQzzn")

# parsed_data = []
# for divan in divans:
#     try:
#         # Название товара извлекаем из alt атрибута изображения
#         name = divan.find_element(By.CSS_SELECTOR, 'img[itemProp="image"]').get_attribute("alt")
#         price = divan.find_element(By.CSS_SELECTOR, 'span[data-testid="price"]').text
#         link = divan.find_element(By.CSS_SELECTOR, 'link[itemProp="url"]').get_attribute("href")
#     except Exception as e:
#         print(f'произошла ошибка при парсинге данных: {e}')
#         continue
#     parsed_data.append([name, price, link])

# driver.quit()

# with open('divans2.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['name', 'price', 'link'])
#     writer.writerows(parsed_data)
# print('данные успешно сохранены в файл divans2.csv')