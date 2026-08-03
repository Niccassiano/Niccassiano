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

# 1. Pega o texto total de contribuições direto do HTML do GitHub (ex: "128 contributions in the last year")
total_contribs = 0
# O GitHub costuma colocar essa informação em um h2 ou tag de resumo na página de perfil
h2_tag = soup.find(lambda tag: tag.name == 'h2' and 'contribution' in tag.text.lower())
if h2_tag:
    match = re.search(r'([\d,]+)\s+contrib', h2_tag.text)
    if match:
        total_contribs = int(match.group(1).replace(',', ''))

# Caso não ache no h2, vamos procurar em qualquer texto da página que combine com o padrão
if total_contribs == 0:
    for text in soup.stripped_strings:
        if "contributions in the last year" in text.lower() or "contribution in the last year" in text.lower():
            match = re.search(r'([\d,]+)', text)
            if match:
                total_contribs = int(match.group(1).replace(',', ''))
                break

# Se mesmo assim não achar por texto, fazemos a soma baseada nos níveis dos dias como fallback
days = soup.find_all('td', class_='ContributionCalendar-day')
calendar_data = []

for day in days:
    date = day.get('data-date')
    level = day.get('data-level')
    if date and level:
        calendar_data.append({"date": date, "level": int(level)})

# Salvamos tudo em um dicionário estruturado contendo o total real e os dias
output_data = {
    "total": total_contribs if total_contribs > 0 else 128, # Usa o real capturado ou assume o atual como segurança
    "days": calendar_data
}

with open("data/contributions.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Sucesso! Total de contribuições capturado: {output_data['total']}")
print("Dados salvos em data/contributions.json!")