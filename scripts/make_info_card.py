# scripts/make_info_card.py

svg_content = '''<svg width="530" height="380" xmlns="http://www.w3.org/2000/svg">
  <style>
    /* Tema Dark moderno de editor de codigo */
    .bg { fill: #0d1117; }
    .text { font-family: "Courier New", Courier, monospace; font-size: 13px; fill: #c9d1d9; opacity: 0; animation: fadeIn 0.8s forwards; }
    
    /* Cores do Syntax Highlighting */
    .key { fill: #79c0ff; font-weight: bold; }
    .string { fill: #a5d6ff; }
    .highlight { fill: #ff7b72; font-weight: bold; font-size: 14px; text-shadow: 0 0 5px rgba(255,123,114,0.4); }
    .role-highlight { fill: #7ee787; font-weight: bold; }
    .array { fill: #f2cc60; }
    
    @keyframes fadeIn { to { opacity: 1; } }
  </style>
  
  <!-- Fundo da Janela -->
  <rect width="100%" height="100%" class="bg" rx="8" stroke="#30363d" />
  
  <!-- Botoes da janela (estilo Mac) -->
  <circle cx="20" cy="20" r="6" fill="#ff5f56"/>
  <circle cx="40" cy="20" r="6" fill="#ffbd2e"/>
  <circle cx="60" cy="20" r="6" fill="#27c93f"/>

  <!-- Escrita simulando um Objeto de Codigo (JSON) -->
  <g transform="translate(20, 48)">
    <text y="15" class="text" style="animation-delay: 0.1s">{</text>
    
    <text y="37" class="text" style="animation-delay: 0.2s">  <tspan class="key">"role"</tspan>: <tspan class="role-highlight">"Desenvolvedora Full Stack"</tspan>,</text>

    <text y="59" class="text" style="animation-delay: 0.25s">  <tspan class="key">"experience"</tspan>: <tspan class="highlight">"1+ ano de experiência"</tspan>,</text>
    
    <text y="81" class="text" style="animation-delay: 0.3s">  <tspan class="key">"education"</tspan>: <tspan class="string">"Cursando Ciência da Computação"</tspan>,</text>
    
    <text y="103" class="text" style="animation-delay: 0.35s">  <tspan class="key">"about"</tspan>: <tspan class="string">"Apaixonada por tecnologia &amp; eng. de software"</tspan>,</text>
    
    <text y="125" class="text" style="animation-delay: 0.4s">  <tspan class="key">"acting"</tspan>: <tspan class="string">"Back-end, Front-end, DevOps, Infraestrutura"</tspan>,</text>
    
    <text y="147" class="text" style="animation-delay: 0.45s">  <tspan class="key">"stack"</tspan>: [</text>
    <text y="167" class="text" style="animation-delay: 0.5s">    <tspan class="array">"PHP (Laravel)"</tspan>, <tspan class="array">"JavaScript"</tspan>, <tspan class="array">"Python"</tspan>, <tspan class="array">"C"</tspan>,</text>
    <text y="187" class="text" style="animation-delay: 0.5s">    <tspan class="array">"SQL"</tspan>, <tspan class="array">"Docker"</tspan>, <tspan class="array">"Jenkins"</tspan></text>
    <text y="207" class="text" style="animation-delay: 0.5s">  ],</text>
    
    <text y="229" class="text" style="animation-delay: 0.55s">  <tspan class="key">"certification"</tspan>: <tspan class="string">"Cisco CCNAv7 (Redes &amp; Troubleshooting)"</tspan>,</text>
    
    <text y="251" class="text" style="animation-delay: 0.6s">  <tspan class="key">"languages"</tspan>: <tspan class="string">"Português (Nativo), Inglês (Intermediário)"</tspan>,</text>
    
    <text y="273" class="text" style="animation-delay: 0.65s">  <tspan class="key">"quote"</tspan>: <tspan class="string">"Sempre evoluindo, uma linha de código por vez."</tspan>,</text>

    <text y="295" class="text" style="animation-delay: 0.7s">  <tspan class="key">"version"</tspan>: <tspan class="string">"v2.1.0 // Always shipping improvements."</tspan></text>
    
    <text y="317" class="text" style="animation-delay: 0.75s">}</text>
  </g>
</svg>'''

with open("info-card.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
    
print("Cartao info-card.svg atualizado com a versao final!")