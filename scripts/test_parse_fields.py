import re

with open("TSU/auditoria_curricular.html", "r", encoding="utf-8") as f:
    text = f.read()

card_pattern = re.compile(
    r'<article class="audit-card" id="([^"]+)" data-bimestre="([^"]+)" data-linea="([^"]+)">\s*'
    r'<div class="audit-card-header">\s*'
    r'<div class="audit-meta">\s*'
    r'<span class="badge-bimestre">([^<]+)</span>\s*'
    r'<span class="badge-code">([^<]+)</span>\s*'
    r'<span class="badge-eje">([^<]+)</span>\s*'
    r'</div>\s*'
    r'<h3>(.*?)</h3>\s*'
    r'<div class="audit-sub">([^<]+)</div>\s*'
    r'</div>\s*'
    r'<div class="audit-body">(.*?)</div>\s*'
    r'</article>',
    re.DOTALL
)

matches = card_pattern.findall(text)
for cid, b, l, bb, code, eje, title, sub, body in matches:
    red = re.search(r'class="audit-callout callout-red">\s*(?:<strong>[^<]+</strong>)?\s*(.*?)\s*</div>', body, re.DOTALL)
    yellow = re.search(r'class="audit-callout callout-yellow">\s*(?:<strong>[^<]+</strong>)?\s*(.*?)\s*</div>', body, re.DOTALL)
    blue = re.search(r'class="audit-callout callout-blue">\s*(?:<strong>[^<]+</strong>)?\s*(.*?)\s*</div>', body, re.DOTALL)
    
    red_txt = red.group(1).strip() if red else "N/A"
    yellow_txt = yellow.group(1).strip() if yellow else "N/A"
    blue_txt = blue.group(1).strip() if blue else "N/A"
    print(f"[{code}] red: {red_txt[:40]}... | yellow: {yellow_txt[:40]}... | blue: {blue_txt[:40]}...")

