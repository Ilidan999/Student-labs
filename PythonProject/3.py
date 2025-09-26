import requests
import time

page = 1
total = 0

while True:
    res = requests.get(f"https://quotes.toscrape.com/api/quotes?page={page}")
    if res.status_code != 200:
        break

    data = res.json()
    quotes = data.get('quotes', [])

    if not quotes:
        break

    for q in quotes:
        print(f"«{q['text']}» — {q['author']['name']} (Теги: {', '.join(q['tags'])})")
        total += 1

    if not data.get('has_next'):
        break
    page += 1
    time.sleep(0.5)

print(f"\nСбор завершён. Всего цитат: {total}")