import sys
import re
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

with open('automotriz.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

panes = soup.find_all('div', id=re.compile(r'^course-pane-'))
for p in panes:
    cid = p.get('id')
    item = p.find('div', class_=re.compile(r'\bcontent-item\b'))
    print(f"\nSample item for {cid}:")
    if item:
        print(item.prettify()[:600])
