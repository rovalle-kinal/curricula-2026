#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import glob

FOLDER_ID = "1OKOstGlGTgtmRl0zN4L_y8_kME6k7Y_1"
PDF_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output", "curricula_2026_cursos_pdfs")

pdf_files = sorted(glob.glob(os.path.join(PDF_DIR, "*.pdf")), key=lambda x: int(os.path.basename(x).split('_')[0]))

print(f"Total PDFs to upload: {len(pdf_files)}")

results = []
for p in pdf_files:
    fname = os.path.basename(p)
    cmd = ["gdrive", "mutate", "upload", p, "--parent", FOLDER_ID]
    print(f"Uploading: {fname}...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode == 0:
        out = res.stdout.strip()
        print(f"  -> {out}")
        results.append((fname, out))
    else:
        print(f"  ERROR: {res.stderr.strip()}")

print("\n--- UPLOAD SUMMARY ---")
for fn, out in results:
    print(f"{fn} -> {out}")
