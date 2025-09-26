# Инструкция для Шохи
# Заменить URL ссылку и после исправить events поиск по тегам

import requests
from bs4 import BeautifulSoup
import time

url = "https://quicktickets.ru/pomorskaya-filarmoniya" # <-- Это URL
response = requests.get(url)

print("Происходит проверка связи...")
time.sleep(1)
if response.status_code == 200:
    print("Cвязь установлена!")
else:
    print(f"Cвязь не установлена!, ошибка {response.status_code}")

html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

title = soup.title.text
time.sleep(1)
print(f"Название страницы: {title}")

time.sleep(1)
events = soup.find_all("div", class_="elem") # <-- Это EVENTS с общим тегом

for event in events: # <-- Это EVENTS для каждой отдельной карточки
    ev_title = event.find("span", class_="underline")
    ev_title = ev_title.get_text(strip=True)

    ev_time = event.find("div", class_="sessions")
    ev_time = ev_time.get_text(separator=", ", strip=True)

    print(f"Название мероприятия: {ev_title}, Время мероприятия: {ev_time}")