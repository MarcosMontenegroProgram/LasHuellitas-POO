import os
with open('main.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Valor del Dólar obtenido de la API: \\n', 'Valor del Dólar obtenido de la API: \\n')
content = content.replace('Valor del Dólar obtenido de la API:  \\n', 'Valor del Dólar obtenido de la API: \\n')

with open('main.py', 'w', encoding='utf-8') as f:
    f.write(content)
