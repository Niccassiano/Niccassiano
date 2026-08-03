import json

with open("data/contributions.json", "r") as f:
    data = json.load(f)

svg_start = '''<svg width="860" height="200" xmlns="http://www.w3.org/2000/svg">
  <style>
    .rect { animation: wave 0.8s ease-in-out forwards; opacity: 0; }
    @keyframes wave { 0% { opacity: 0; transform: scale(0.3); } 100% { opacity: 1; transform: scale(1); } }
  </style>
  <rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d" />
  <g transform="translate(20, 20)">
'''

svg_end = '''
  </g>
  <text x="20" y="180" fill="#c9d1d9" font-family="monospace" font-size="14">90 contributions in the last year</text>
</svg>'''

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

rects = ""
x = 0
y = 0
for day in data:
    color = PALETTE[min(day['level'], 5)]
    delay = (x + y) * 0.03
    rects += f'<rect x="{x*15}" y="{y*15}" width="11" height="11" fill="{color}" rx="2" class="rect" style="animation-delay: {delay}s" />\n'
    y += 1
    if y == 7:
        y = 0
        x += 1

with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
    f.write(svg_start + rects + svg_end)

print("Gráfico contrib-heatmap.svg criado com sucesso!")