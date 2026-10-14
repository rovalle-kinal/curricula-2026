with open('mecanica_temporal.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('href="automotriz.html"', 'href="automotriz_temporal.html"')
c = c.replace('href="mecanica.html"', 'href="mecanica_temporal.html"')

with open('mecanica_temporal.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated links in mecanica_temporal.html')
