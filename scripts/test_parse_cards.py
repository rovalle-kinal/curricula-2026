import re

with open("TSU/auditoria_curricular.html", "r", encoding="utf-8") as f:
    text = f.read()

# Pattern for audit-card
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
print(f"Matched {len(matches)} cards")
for cid, b, l, bb, code, eje, title, sub, body in matches[:3]:
    print(f"Card {cid}: {code} - {title.strip()} ({sub}) | Bimestre: {b}, Linea: {l}")
