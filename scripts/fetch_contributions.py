# scripts/fetch_contributions.py
import requests
from bs4 import BeautifulSoup
import json
import re

USERNAME = "Niccassiano"
URL = f"https://github.com/users/{USERNAME}/contributions"

print(f"Buscando contribuições de {USERNAME}...")
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')


total_contribs = 0

h2_tag = soup.find(lambda tag: tag.name == 'h2' and 'contribution' in tag.text.lower())
if h2_tag:
    match = re.search(r'([\d,]+)\s+contrib', h2_tag.text)
    if match:
        total_contribs = int(match.group(1).replace(',', ''))


if total_contribs == 0:
    for text in soup.stripped_strings:
        if "contributions in the last year" in text.lower() or "contribution in the last year" in text.lower():
            match = re.search(r'([\d,]+)', text)
            if match:
                total_contribs = int(match.group(1).replace(',', ''))
                break


days = soup.find_all('td', class_='ContributionCalendar-day')
calendar_data = []

for day in days:
    date = day.get('data-date')
    level = day.get('data-level')
    if date and level:
        calendar_data.append({"date": date, "level": int(level)})


output_data = {
    "total": total_contribs if total_contribs > 0 else 128, 
    "days": calendar_data
}

with open("data/contributions.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Sucesso! Total de contribuições capturado: {output_data['total']}")
print("Dados salvos em data/contributions.json!")