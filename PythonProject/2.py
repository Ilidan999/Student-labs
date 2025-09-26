# Добавляем библиотеку Selenium для работы с браузером
# Задание не меняется

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()#Важно чтобы приложение Chrome было скачено
try:
    driver.get('https://www.pomorie.ru/news/')
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.select('a.info')

    if not links:
        print("Теги <a> с классом 'info' не найдены.")
    else:
        for i, tag in enumerate(links, 1):
            text = tag.get_text(strip=True)
            href = tag.get('href', 'нет ссылки')
            print(f"{i}. {text} | Ссылка: {href}")

finally:
    driver.quit()