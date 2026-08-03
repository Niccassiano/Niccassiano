import requests
from bs4 import BeautifulSoup
import json

USERNAME = "Niccassiano"
URL = f"https://github.com/users/{USERNAME}/contributions"

print(f"Buscando contribuições de {USERNAME}...")
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

days = soup.find_all('td', class_='ContributionCalendar-day')
data = []

for day in days:
    date = day.get('data-date')
    level = day.get('data-level')
    if date and level:
        data.append({"date": date, "level": int(level)})

with open("data/contributions.json", "w") as f:
    json.dump(data, f)

print("Contribuições salvas em data/contributions.json!")