# 📊 Парсинг и обработка данных

## 🎯 Заключительный урок по теме парсинга

Этот урок завершает изучение темы парсинга данных с веб-страниц. Мы научились получать информацию, теперь изучаем как её сохранять и обрабатывать для дальнейшего использования.

## 📚 Что мы изучим

- ✅ Обработку данных (очистка, преобразование, фильтрация)
- ✅ Различные методы сохранения данных
- ✅ Когда и какие форматы хранения данных использовать

---

## 🧹 1. Обработка данных

Когда мы парсим данные с веб-страниц, часто получаем **сырые данные**, которые нуждаются в обработке.

### 🔧 Виды обработки данных

#### 1️⃣ **Очистка данных**
- Удаление лишних пробелов и специальных символов
- Удаление лишней информации
- Исправление некорректных, повреждённых данных

#### 2️⃣ **Преобразование данных**
- Перевод строк в числа
- Изменение типов данных

#### 3️⃣ **Фильтрация данных**
- Отбор только нужных случаев

---

## 💻 Практические примеры

### 🧽 Очистка данных

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find_all("tr")  # tr - каждый ряд таблицы
# td - каждая ячейка внутри ряда таблицы

data = []

for row in rows:
    cols = row.find_all("td")
    # Используем укороченный вариант цикла for
    # Для удаления пробелов используем функцию strip()
    cleaned_cols = [col.text.strip() for col in cols]
    # Чтобы удалить пробелы, оставляем ()
    # Чтобы удалить символы из начала и конца: strip('символы')
    data.append(cleaned_cols)

print(data)
```

### 🔄 Преобразование данных (цены)

```python
# Данные с сайта (вложенные списки)
data = [
    ['100', '200', '300'],
    ['400', '500', '600']
]

numbers = []

# Преобразуем строки в числа
for row in data:
    for text in row:
        number = int(text)  # или float(text) для десятичных чисел
        numbers.append(number)

print(numbers)  # [100, 200, 300, 400, 500, 600]
```

### 🔍 Фильтрация данных

```python
# Двумерный список
data = [
    [100, 110, 120],
    [400, 500, 600],
    [150, 130, 140]
]

filtered_list = []

# Фильтруем элементы больше 190
for row in data:
    for item in row:
        if item > 190:
            filtered_list.append(item)

print(filtered_list)  # [400, 500, 600]
```

---

## 💾 2. Сохранение данных

После обработки данных их необходимо сохранить для дальнейшего анализа.

### 📁 Форматы хранения данных

| Формат | Описание | Преимущества | Недостатки |
|--------|----------|--------------|------------|
| **TXT** | Текстовый формат | Простота | Ограниченная структура |
| **CSV** | Comma-Separated Values | Простота, совместимость с Excel | Не подходит для больших объёмов |
| **JSON** | JavaScript Object Notation | Удобен для сложных структур | Может быть избыточным |
| **SQLite** | Легковесная база данных | Масштабируемость, запросы | Требует знания SQL |
| **Электронные таблицы** | Google Sheets, Excel | Визуализация, доступ с устройств | Ограничения по объёму |

### 📊 CSV формат - пример использования

```python
import csv

# Сохранение данных в CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])  # Заголовки
    writer.writerows(parsed_data)  # Данные
```

---

## 🚀 3. Практический пример: Парсинг вакансий с HH.ru

### 🔧 Современный код с актуальными селекторами

```python
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(3)

# Поиск карточек вакансий
vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.vacancy-info--umZA61PpMY07JVJtomBA')

parsed_data = []

for vacancy in vacancies:
    try:
        # Название вакансии и ссылка
        title_element = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-2')
        title = title_element.text
        link = title_element.get_attribute('href')
        
        # Компания
        company = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text

        # Зарплата (может отсутствовать)
        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-labels--cR9OD8ZegWd3f7Mzxe6z').text
        except:
            salary = "Не указана"

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

# Сохранение в CSV
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)
```

### 🛡️ Обработка ошибок

```python
try:
    # Код парсинга
    title = vacancy.find_element(By.CSS_SELECTOR, 'селектор').text
except Exception as e:
    print(f"Произошла ошибка при парсинге: {e}")
    continue  # Продолжаем с следующей итерацией
```

---

## 📋 4. Результаты урока

### ✅ Что мы изучили:

1. **Обработку данных**:
   - Очистка от лишних символов
   - Преобразование типов данных
   - Фильтрация по условиям

2. **Методы сохранения данных**:
   - CSV для табличных данных
   - JSON для сложных структур
   - Базы данных для больших объёмов

3. **Выбор форматов**:
   - Понимание когда использовать каждый формат
   - Учёт преимуществ и недостатков

### 🎯 Практические навыки:

- ✅ Парсинг данных с веб-страниц
- ✅ Очистка и обработка полученных данных
- ✅ Сохранение данных в различных форматах
- ✅ Обработка ошибок при парсинге
- ✅ Работа с Selenium WebDriver

---

## 📁 Структура проекта

```
ScrapinSaveData/
├── PS06_DZ.py          # Основной скрипт парсинга divan.ru
├── SaveData.py         # Дополнительные скрипты сохранения
├── SaveData1.py        # Альтернативные методы
├── divans.csv          # Результат парсинга
└── README.md           # Документация проекта
```

---

## 🔗 Полезные ссылки

- [Selenium WebDriver Documentation](https://selenium-python.readthedocs.io/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Python CSV Module](https://docs.python.org/3/library/csv.html)
- [JSON in Python](https://docs.python.org/3/library/json.html)

---

## ⚠️ Важные замечания

1. **Селекторы могут изменяться** - сайты обновляют свою структуру
2. **Соблюдайте robots.txt** - уважайте правила сайтов
3. **Используйте задержки** - не перегружайте серверы
4. **Обрабатывайте ошибки** - всегда используйте try-except блоки

---

*Урок завершён! Теперь вы умеете парсить, обрабатывать и сохранять данные с веб-страниц.* 🎉
