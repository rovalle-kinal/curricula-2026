import sys
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('automotriz_temporal.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("Title:", soup.find('title').get_text(strip=True))

# Check navbar
nav = soup.find('nav')
print("\nNavbar buttons:")
for a in nav.find_all('a'):
    print(f"  {a.get('href')} -> '{a.get_text(strip=True)}'")

# Check each course pane
panes = soup.find_all('div', id=re.compile(r'^course-pane-'))
print(f"\nTotal course panes: {len(panes)}")
for p in panes:
    cid = p.get('id')
    h2 = p.find('h2')
    h2_text = h2.get_text(strip=True) if h2 else cid
    
    # Check Section 3
    sec3 = None
    for s in p.find_all('section'):
        if '3. Distribución Modular Auditada' in s.get_text():
            sec3 = s
            break
            
    if not sec3:
        print(f"[FAIL] No sec3 for {cid}")
        continue
        
    cards = sec3.find_all('div', class_=re.compile(r'rounded-xl border border-slate-300'))
    items = sec3.find_all('div', class_=re.compile(r'\bcontent-item\b'))
    
    del_items = [it for it in items if it.get('data-status') == 'delete']
    upd_items = [it for it in items if it.get('data-status') == 'update']
    new_items = [it for it in items if it.get('data-status') == 'new']
    keep_items = [it for it in items if it.get('data-status') == 'keep']
    
    print(f"\n{cid} ({h2_text[:45]}):")
    print(f"  Module cards: {len(cards)}")
    print(f"  Total items: {len(items)} (🔴 {len(del_items)}, 🟡 {len(upd_items)}, 🔵 {len(new_items)}, 🟢 {len(keep_items)})")
    
    # Check first card structure
    if cards:
        c1 = cards[0]
        header = c1.find('div', class_=re.compile(r'bg-slate-900'))
        h4 = header.find('h4').get_text(strip=True) if header and header.find('h4') else "NO H4"
        logro = header.find('p').get_text(strip=True) if header and header.find('p') else "NO LOGRO"
        print(f"  First Card -> H4: '{h4}' | {logro[:60]}...")
