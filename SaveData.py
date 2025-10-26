import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find_all("tr")

data = []
for row in rows:
    cols = row.find_all("td")
    cleand_cols = [col.text.strip() for col in cols]
    data.append(cleand_cols)

print(data)