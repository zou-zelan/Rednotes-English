#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""老友记小红书图文渲染引擎(1080x1440, 3:4)。"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1440
ML, MR = 96, 96
CW = W - ML - MR

FDIR = "/usr/share/fonts/opentype/noto"
SC_IDX = 2

CREAM  = (248, 242, 230)
CARD   = (253, 250, 243)
INK    = (51, 38, 32)
MUTED  = (138, 118, 87)
FAINT  = (176, 160, 132)
MUST   = (246, 184, 64)
HILTXT = (62, 42, 18)
ORANGE = (232, 120, 46)
ORANGE_D = (196, 96, 34)
LINE   = (229, 217, 192)
MUSTBG = (250, 236, 195)
TIP = (176, 84, 58)      # 易错提醒砖红
LINH = 1.42

_fc = {}
def F(weight="Regular", size=28):
    key = (weight, size)
    if key not in _fc:
        _fc[key] = ImageFont.truetype(
            f"{FDIR}/NotoSansCJK-{weight}.ttc", size, index=SC_IDX)
    return _fc[key]

def tw(f, s):
    return f.getlength(s)

def tokenize(text):
    """切 token:CJK 单字 / 拉丁词。返回 [(tok, is_lat)]"""
    toks, cur = [], ""
    def flush():
        nonlocal cur
        if cur:
            toks.append((cur, True))
            cur = ""
    for ch in text:
        if ch.isascii() and (ch.isalnum() or ch in "'-."):
            cur += ch
        else:
            flush()
            toks.append((ch, False))
    flush()
    return toks

def _clean(tok):
    """去掉高亮标记前缀 \\x00,测宽/绘制时忽略它。"""
    if isinstance(tok, str) and tok.startswith("\x00"):
        return tok[1:]
    return tok

def mline(tokens, font):
    """一行 tokens 的宽度(连续两个拉丁词间补空格)。"""
    total, prev = 0.0, False
    for tok, is_lat in tokens:
        if prev and is_lat:
            total += tw(font, " ")
        total += tw(font, _clean(tok))
        prev = is_lat
    return total

def wrap(tokens, font, maxw):
    lines = [[]]
    for tok in tokens:
        cx = lines[-1] + [tok]
        if mline(cx, font) <= maxw or len(lines[-1]) == 0:
            lines[-1].append(tok)
        else:
            lines.append([tok])
    return lines

def draw_line(draw, x, y, tokens, font, color):
    xc, prev = x, False
    for tok, is_lat in tokens:
        if prev and is_lat:
            xc += tw(font, " ")
        draw.text((xc, y), _clean(tok), font=font, fill=color)
        xc += tw(font, _clean(tok))
        prev = is_lat
    return xc

_hlm = {}
def _hl_vert(font):
    """按字号缓存统一的高亮纵向范围 (top, bottom),参考含高低笔画的字形。"""
    size = font.size
    if size not in _hlm:
        b = font.getbbox("Agjy永走Hg")
        _hlm[size] = (b[1], b[3])
    return _hlm[size]

def draw_hl(draw, x, y, tokens, font, color=INK, hl_bg=MUST, hl_color=HILTXT):
    """带黄底高亮渲染一行(高亮 token 以 \\x00 前缀标记)。
    连续高亮合成为一整条等高色块,顶底对齐,不随字母起伏。"""
    items = []
    for tok, is_lat in tokens:
        if isinstance(tok, str) and tok.startswith("\x00"):
            items.append((tok[1:], True, is_lat))
        else:
            items.append((tok, False, is_lat))
    px, py = int(font.size * 0.14), int(font.size * 0.09)
    ht, hb = _hl_vert(font)
    n = len(items)
    xc = x
    i = 0
    while i < n:
        txt, hl, lat = items[i]
        if not hl:
            if i > 0 and items[i - 1][2] and lat:
                xc += tw(font, " ")
            draw.text((xc, y), txt, font=font, fill=color)
            xc += tw(font, txt)
            i += 1
            continue
        j = i
        sx = xc
        if i > 0 and items[i - 1][2] and items[i][2]:
            sx += tw(font, " ")
        ex = sx + tw(font, txt)
        prev_lat = lat
        j = i + 1
        while j < n and items[j][1]:
            r_txt, _, r_lat = items[j]
            if prev_lat and r_lat:
                ex += tw(font, " ")
            ex += tw(font, r_txt)
            prev_lat = r_lat
            j += 1
        yy0, yy1 = y + ht - py, y + hb + py
        draw.rounded_rectangle(
            [sx - px, yy0, ex + px, yy1],
            radius=int(min(10, (yy1 - yy0) / 2)), fill=hl_bg)
        cx = sx
        prev_lat = lat
        for k in range(i, j):
            r_txt, _, r_lat = items[k]
            if prev_lat and r_lat:
                cx += tw(font, " ")
            draw.text((cx, y), r_txt, font=font, fill=hl_color)
            cx += tw(font, r_txt)
            prev_lat = r_lat
        xc = ex
        i = j
    return x

def fit_size(lines, weight, base, maxw, min_size=24):
    """整句各不折行的最大字号(从 base 逐级下调)。"""
    size = base
    while size > min_size:
        f = F(weight, size)
        fits = True
        for ln in lines:
            if mline(tokenize(ln), f) > maxw:
                fits = False
                break
        if fits:
            return size
        size -= 1
    return base

def segs_tokens(segs):
    """接受 [(text, hl)] 或纯文本字符串 -> tokens。高亮 token 前缀 \\x00。"""
    if isinstance(segs, str):
        segs = [(segs, False)]
    out = []
    for text, hl in segs:
        for tok, is_lat in tokenize(text):
            out.append(("\x00" + tok if hl else tok, is_lat))
    return out

def page():
    img = Image.new("RGB", (W, H), CREAM)
    return img, ImageDraw.Draw(img)

def header(draw, badge, page_no, ep="S01E01"):
    y = 78
    fb = F("Bold", 26)
    bw = tw(fb, badge) + 52
    draw.rounded_rectangle([ML, y, ML + bw, y + 54], radius=27, fill=ORANGE)
    draw.text((ML + 26, y + 11), badge, font=fb, fill=(255, 250, 240))
    draw.line([ML, y + 78, W - MR, y + 78], fill=LINE, width=3)
    pf = F("Medium", 22)
    pt = f"{ep} · {page_no:02d}/18"
    draw.text((W - MR - tw(pf, pt), y + 15), pt, font=pf, fill=FAINT)
    return y + 78

def footer(draw):
    y = 1376
    f = F("Medium", 22)
    s = "老友记口语笔记 · 跟着剧集一起打卡"
    w = tw(f, s)
    x = (W - w) / 2
    draw.rounded_rectangle([x - 22, y - 4, x + w + 22, y + 40], radius=22,
                           fill=CARD, outline=LINE)
    draw.text((x, y + 3), s, font=f, fill=MUTED)

def block(draw, y0, item, scale=1.0):
    pad = 30
    fhead = F("Bold", int(item.get("size", 34) * scale))
    fgloss = F("Medium", int(24 * scale))
    fq = F("Medium", int(item.get("qsize", 28) * scale))
    ftiny = F("Regular", int(24 * scale))
    ftag = F("Bold", int(20 * scale))
    inner_w = CW - 2 * pad

    h_toks = segs_tokens(item["head"])
    h_lines = wrap(h_toks, fhead, inner_w)
    g_toks = segs_tokens(item.get("gloss") or [])
    g_lines = wrap(g_toks, fgloss, inner_w) if g_toks else []
    q_toks = segs_tokens(item["quote"])
    q_lines = wrap(q_toks, fq, inner_w - 8)

    details = []
    if "trans" in item:
        details.append(("译", item["trans"], MUTED, ORANGE))
    if "note" in item:
        details.append(("点", item["note"], MUTED, ORANGE))
    if "how" in item:
        details.append(("仿", item["how"], ORANGE_D, ORANGE))
    if "fix" in item:
        details.append(("别", item["fix"], TIP, TIP))

    # 预计算细节行的实际换行数,确保卡片高度精确
    detail_lines = []
    for tag, text, col, tcol in details:
        txn = tw(ftag, tag) + tw(ftag, " ")
        detail_lines.append((tag, text, col, tcol,
                             wrap(tokenize(text), ftiny, inner_w - txn)))

    lh = lambda f: int(f.size * LINH)
    hh = len(h_lines) * lh(fhead)
    gh = (len(g_lines) * lh(fgloss) + 4) if g_lines else 0
    qh = len(q_lines) * lh(fq) + 24
    dh = sum(len(w) * lh(ftiny) for _, _, _, _, w in detail_lines) + 4 * len(detail_lines)
    total = 2 * pad + hh + gh + (6 + qh + 12) + dh

    bbox = [ML, y0, W - MR, y0 + total]
    draw.rounded_rectangle(bbox, radius=26, fill=CARD)
    x = ML + pad
    y = y0 + pad

    for line in h_lines:
        draw_hl(draw, x, y, line, fhead)
        y += lh(fhead)
    if g_lines:
        y += 4
        for line in g_lines:
            draw_hl(draw, x, y, line, fgloss, color=ORANGE_D)
            y += lh(fgloss)

    y += 6
    qh0 = y
    qh1 = y + qh
    draw.rounded_rectangle([ML + pad - 12, qh0, W - MR - pad + 12, qh1],
                           radius=18, fill=MUSTBG)
    qy = qh0 + 12
    for line in q_lines:
        draw_hl(draw, ML + pad, qy, line, fq)
        qy += lh(fq)
    y = qh1 + 12

    for tag, text, col, tcol in details:
        txn = tw(ftag, tag) + tw(ftag, " ")
        draw.text((x, y), tag, font=ftag, fill=tcol)
        lns = wrap(tokenize(text), ftiny, inner_w - txn)
        for i, line in enumerate(lns):
            draw_line(draw, x + (txn if i == 0 else 0), y, line, ftiny, col)
            y += lh(ftiny)
        y += 4

    return y0 + total

BOTTOMS = []

def content_page(fname, page_no, badge, items, foot=None, subtitle=None, title=None, tsize=46, scale=1.0, ep="S01E01"):
    img, draw = page()
    top = header(draw, badge, page_no, ep)
    y = top + 30
    if subtitle:
        sf = F("Medium", 26)
        draw.text((ML, y), subtitle, font=sf, fill=ORANGE_D)
        y += int(26 * LINH) + 12
    if title:
        ft = F("Black", tsize)
        for line in wrap(segs_tokens(title), ft, CW):
            draw_hl(draw, ML, y, line, ft)
            y += int(tsize * LINH)
        y += 12
    for it in items:
        y = block(draw, y, it, scale) + 22
    if foot:
        ff = F("Medium", 25)
        fl = wrap(tokenize(foot), ff, CW - 80)
        fh = len(fl) * int(25 * LINH) + 40
        fy = H - 122 - fh
        draw.rounded_rectangle([ML, fy, W - MR, fy + fh], radius=24, fill=ORANGE)
        yy = fy + 20
        for line in fl:
            w = mline(line, ff)
            draw_hl(draw, (W - w) / 2, yy, line, ff,
                    color=(255, 252, 243), hl_bg=MUST, hl_color=INK)
            yy += int(25 * LINH)
    footer(draw)
    img.save(fname)
    BOTTOMS.append((page_no, y))
    return fname, y