import glob
from bs4 import BeautifulSoup

for hfile in sorted(glob.glob('*.html')):
    try:
        with open(hfile, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        nav = soup.find('nav')
        if not nav:
            continue
        mec_link = nav.find('a', href=lambda h: h and 'mecanica' in h)
        auto_link = nav.find('a', href=lambda h: h and 'automotriz' in h)
        m_txt = mec_link.get_text(strip=True) if mec_link else 'N/A'
        a_txt = auto_link.get_text(strip=True) if auto_link else 'N/A'
        print(f"{hfile:30}: Mecanica='{m_txt}' | Automotriz='{a_txt}'")
    except Exception as e:
        print(f"Error {hfile}: {e}")
