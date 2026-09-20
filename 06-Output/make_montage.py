#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成某集 18 图总览拼图 + 尺寸校验。用法:python make_montage.py [S01E01]"""
import os
import sys
from PIL import Image

EP = sys.argv[1] if len(sys.argv) > 1 else "S01E01"
BASE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(BASE, f"img-{EP}")
if not os.path.isdir(DIR):
    print(f"no such dir: {DIR}")
    sys.exit(1)
paths = sorted(
    os.path.join(DIR, f)
    for f in os.listdir(DIR)
    if f.endswith(".png") and f.startswith(f"{EP}-")
)
assert len(paths) == 18, f"expect 18, got {len(paths)}"

# 尺寸校验
for p in paths:
    with Image.open(p) as im:
        assert im.size == (1080, 1440), (p, im.size)

# 4x5 拼图(第 18 张右下留空),每格加序号标签
CELL_W, CELL_H = 312, 416
GAP = 14
cols, rows = 5, 4
W = cols * CELL_W + (cols + 1) * GAP
H = rows * CELL_H + (rows + 1) * GAP
sheet = Image.new("RGB", (W, H), (60, 52, 44))
img = Image.open(paths[0])
th = img.resize((CELL_W, CELL_H))
sheet.paste(th, (GAP, GAP))

for idx in range(18):
    col = idx % cols
    row = idx // cols
    x = GAP + col * (CELL_W + GAP)
    y = GAP + row * (CELL_H + GAP)
    im = Image.open(paths[idx]).resize((CELL_W, CELL_H))
    sheet.paste(im, (x, y))

sheet.save(os.path.join(DIR, "_montage.png"))
print("montage:", os.path.join(DIR, "_montage.png"))
for p in paths:
    print(" ", os.path.basename(p), Image.open(p).size, os.path.getsize(p) // 1024, "KB")