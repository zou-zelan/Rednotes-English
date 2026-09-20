#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""特殊版式:封面 / 剧情 / 名场面 / 彩蛋时间线 / 结尾。"""
from xhs_engine import (
    W, H, ML, MR, CW, CREAM, CARD, INK, MUTED, FAINT, MUST, HILTXT,
    ORANGE, ORANGE_D, LINE, MUSTBG, LINH,
    F, tw, tokenize, mline, wrap, draw_line, draw_hl, segs_tokens, fit_size,
    page, header, footer,
)

def cover(fname, *, episode="第 1 集", quote=None, sub=None, tags=None,
          lead="打开这一集,你能带走 4 类干货", credit="老友记 S01E01 · 台词精讲笔记"):
    if quote is None:
        quote = [("Welcome to the real world.", False),
                 ("It sucks. You're gonna love it.", True)]
    if sub is None:
        sub = "这集承包了美剧史上被引用最多的名台词之一"
    if tags is None:
        tags = ["高频缩略", "高频短语", "万能句型", "绝妙比喻"]
    img, draw = page()
    f = F("Bold", 26)
    y = 70
    x = ML
    pills = [("看老友记 · 学地道口语", ORANGE, (255, 250, 240)),
             (episode, MUST, (50, 34, 12))]
    for txt, bg, tc in pills:
        w = tw(f, txt) + 44
        draw.rounded_rectangle([x, y, x + w, y + 54], radius=27, fill=bg)
        draw.text((x + 22, y + 10), txt, font=f, fill=tc)
        x += w + 18

    fq = F("Black", 62)
    size = fit_size([q[0] for q in quote], "Black", 62, CW)
    fq = F("Black", size)
    y = 340
    for txt, hl in quote:
        toks = [("\x00" + t if hl else t, lat) for t, lat in tokenize(txt)]
        for ln in wrap(toks, fq, CW):
            w = mline(ln, fq)
            draw_hl(draw, (W - w) / 2, y, ln, fq)
            y += int(size * LINH * 1.05)

    fs = F("Medium", 28)
    s = sub
    w = tw(fs, s)
    draw.line([(W - w) / 2 - 60, y + 18, (W + w) / 2 + 60, y + 18],
              fill=ORANGE, width=3)
    draw.text(((W - w) / 2, y + 34), s, font=fs, fill=MUTED)

    # 本集看点导行
    gy = y + 128
    fg = F("Bold", 27)
    s = lead
    w = tw(fg, s)
    draw.text(((W - w) / 2, gy), s, font=fg, fill=INK)
    ft = F("Bold", 25)
    ph = 52
    tot = sum(tw(ft, t) + 44 for t in tags) + (len(tags) - 1) * 16
    x = (W - tot) / 2
    ty = gy + 46
    for t in tags:
        w = tw(ft, t) + 44
        draw.rounded_rectangle([x, ty, x + w, ty + ph], radius=ph // 2,
                               fill=MUSTBG, outline=ORANGE)
        draw.text((x + 22, ty + 12), t, font=ft, fill=ORANGE_D)
        x += w + 16

    fb = F("Bold", 30)
    s = "左滑 18 张 · 每张一句地道表达"
    w = tw(fb, s)
    by = H - 200
    draw.rounded_rectangle([(W - w) / 2 - 26, by, (W + w) / 2 + 26, by + 64],
                           radius=32, fill=INK)
    draw.text(((W - w) / 2, by + 14), s, font=fb, fill=CREAM)
    fc = F("Medium", 24)
    s = credit
    w = tw(fc, s)
    draw.text(((W - w) / 2, by + 96), s, font=fc, fill=FAINT)
    img.save(fname)
    return fname

def story(fname, page_no, *, ep="S01E01", badge="先讲发生在同一晚的故事", lines=None,
          pill="这一集,几乎每句话都值得模仿。"):
    if lines is None:
        lines = [
            "Rachel 在自己的婚礼当天逃婚,穿着婚纱冲进了 Central Perk",
            "Ross 刚被离婚打击,正处在人生低谷",
            "Monica 为首次约会精心准备,Paul 却藏着秘密",
            "六个人,在咖啡馆里挤成一团,互相救场",
        ]
    img, draw = page()
    top = header(draw, badge, page_no, ep)
    y = top + 40
    f = F("Medium", 29)
    fnum = F("Black", 30)
    for i, ln in enumerate(lines):
        lns = wrap(tokenize(ln), f, CW - 100)
        h = len(lns) * int(29 * LINH) + 46
        draw.rounded_rectangle([ML, y, W - MR, y + h], radius=24, fill=CARD)
        num = f"{i + 1:02d}"
        draw.text((ML + 32, y + 22), num, font=fnum, fill=ORANGE)
        yy = y + 16
        for line in lns:
            draw_line(draw, ML + 32 + tw(fnum, num) + 36, yy, line, f, INK)
            yy += int(29 * LINH)
        y += h + 18
    f2 = F("Bold", 28)
    s = pill
    w = tw(f2, s)
    draw.rounded_rectangle([(W - w) / 2 - 20, y + 6, (W + w) / 2 + 20, y + 64],
                           radius=29, fill=MUST)
    draw.text(((W - w) / 2, y + 14), s, font=f2, fill=HILTXT)
    footer(draw)
    img.save(fname)
    return fname

def hero(fname, page_no, subtitle, quote, trans, note, *, ep="S01E01",
         msg=None, teaser=None, tag_txt="下一站"):
    if msg is None:
        msg = "这句话,说给逃婚的 Rachel,也说给焦虑的你"
    if teaser is None:
        teaser = "本集还有冰激凌口味 / 嘴里卡衣架两大妙喻 →"
    img, draw = page()
    top = header(draw, "本集名场面 · 收藏级", page_no, ep)
    y = top + 60
    fs = F("Medium", 26)
    draw.text((ML, y), subtitle, font=fs, fill=ORANGE_D)
    y += int(26 * LINH) + 40
    size = fit_size([q[0] for q in quote], "Black", 56, CW, min_size=34)
    fq = F("Black", size)
    for txt, hl in quote:
        toks = [("\x00" + t if hl else t, lat) for t, lat in tokenize(txt)]
        for ln in wrap(toks, fq, CW):
            w = mline(ln, fq)
            draw_hl(draw, (W - w) / 2, y, ln, fq)
            y += int(size * LINH * 1.05)
    y += 18
    draw.line([ML + 60, y, W - MR - 60, y], fill=LINE, width=3)
    y += 30
    ft = F("Medium", 27)
    for ln in wrap(tokenize(trans), ft, CW):
        draw_line(draw, ML, y, ln, ft, MUTED)
        y += int(27 * LINH)
    y += 26
    if note:
        fn = F("Medium", 24)
        for ln in wrap(tokenize(note), fn, CW):
            draw_line(draw, ML, y, ln, fn, ORANGE_D)
            y += int(24 * LINH)
    y += 10
    fm = F("Bold", 25)
    s = msg
    note_lines = wrap(tokenize(s), fm, CW - 70)
    card_h = max(len(note_lines) * int(25 * LINH) + 44, 96)
    draw.rounded_rectangle([ML, y, W - MR, y + card_h], radius=24, fill=MUSTBG)
    yy = y + 22
    for ln in note_lines:
        w = mline(ln, fm)
        draw_hl(draw, (W - w) / 2, yy, ln, fm, color=INK, hl_bg=MUST)
        yy += int(25 * LINH)
    y += card_h + 24
    # 同款类比预告
    ftag = F("Medium", 23)
    fte = F("Medium", 23)
    tcx = tw(ftag, tag_txt) + 14
    draw.text((ML, y), tag_txt, font=ftag, fill=ORANGE)
    draw.text((ML + tcx, y), teaser, font=fte, fill=MUTED)
    footer(draw)
    img.save(fname)
    return fname

def timeline(fname, page_no, *, ep="S01E01", badge="本集彩蛋 | 笑话弧光", title=None,
             items=None, pill="看懂台词背后的伏笔,才叫真正听懂这一集。"):
    if title is None:
        title = "一句 grab a spoon,串起全集的梗"
    if items is None:
        items = [
            ("开头", "被 Rachel 一巴掌打懵,Ross 自嘲开解:\u201cWelcome back to the world. Grab a spoon.\u201d(欢迎回到现实,拿起勺子开吃吧)"),
            ("中段", "Rachel 逃婚留下的烂摊子里,Monica 劝大家\u201c放下心来,好好吃这口生活\u201d,冰激凌比喻正式上线。"),
            ("结尾", "Rachel 主动吻上他,Ross 愣了半秒,回了一句:\u201cI just grabbed a spoon.\u201d(我刚刚握住了勺子)"),
        ]
    img, draw = page()
    top = header(draw, badge, page_no, ep)
    y = top + 34
    ft = F("Black", 40)
    s = title
    for ln in wrap(tokenize(s), ft, CW):
        draw_hl(draw, ML, y, ln, ft)
        y += int(40 * LINH)
    y += 26
    f = F("Medium", 28)
    fnum = F("Black", 30)
    for i, (tag, body) in enumerate(items):
        lns = wrap(tokenize(body), f, CW - 120)
        h = len(lns) * int(28 * LINH) + 46
        draw.rounded_rectangle([ML, y, W - MR, y + h], radius=24, fill=CARD)
        draw.text((ML + 32, y + 22), tag, font=fnum, fill=ORANGE)
        yy = y + 16
        for line in lns:
            draw_line(draw, ML + 150, yy, line, f, INK)
            yy += int(28 * LINH)
        y += h + 18
    f2 = F("Medium", 25)
    s = pill
    w = tw(f2, s)
    draw.rounded_rectangle([(W - w) / 2 - 20, y + 6, (W + w) / 2 + 20, y + 62],
                           radius=29, fill=MUST)
    draw.text(((W - w) / 2, y + 14), s, font=f2, fill=HILTXT)
    footer(draw)
    img.save(fname)
    return fname

def ending(fname, page_no, *, ep="S01E01", badge="第 1 集 · 完",
           s1="这集的 20 条地道表达,\n你都记下来了吗?",
           mem="记住一条,用出来,才算学会。",
           quote=None,
           recap_title="本集 20 条,分 5 类,打包带走:",
           rows=None,
           preview=None):
    if quote is None:
        quote = [("Welcome to the real world.", False),
                 ("It sucks. You're gonna love it.", True)]
    if rows is None:
        rows = [
            ("高频缩略", "gotta · wanna · gonna"),
            ("高频口头禅", "Are you kidding? · I have no idea"),
            ("高频短语", "walk out on · hit on · hang out"),
            ("万能句型", "There's nothing to tell · Did I say that out loud"),
            ("绝妙比喻", "You're a shoe · 冰激凌口味 · 嘴里卡衣架"),
        ]
    if preview is None:
        preview = "下集预告 S02E01:Rachel 与 Ross 的那一夜"
    img, draw = page()
    top = header(draw, badge, page_no, ep)
    f1 = F("Black", 44)
    y = top + 70
    for chunk in s1.split("\n"):
        for ln in wrap(tokenize(chunk), f1, CW):
            w = mline(ln, f1)
            draw_hl(draw, (W - w) / 2, y, ln, f1)
            y += int(44 * LINH)
    f2 = F("Medium", 27)
    s = mem
    w = tw(f2, s)
    draw.text(((W - w) / 2, y + 18), s, font=f2, fill=MUTED)
    y += int(27 * LINH) + 40
    draw.line([ML + 80, y, W - MR - 80, y], fill=LINE, width=3)
    y += 30
    lines = [q[0] for q in quote]
    size = fit_size(lines, "Black", 40, CW, min_size=24)
    fq = F("Black", size)
    for txt, hl in quote:
        toks = [("\x00" + t if hl else t, lat) for t, lat in tokenize(txt)]
        for ln in wrap(toks, fq, CW):
            w = mline(ln, fq)
            draw_hl(draw, (W - w) / 2, y, ln, fq)
            y += int(size * LINH * 1.05)
    y += 30

    # 本集提要:5 类表达打包回顾
    rt = F("Bold", 27)
    rc = F("Bold", 23)
    cand = F("Medium", 24)
    pad_in = 26
    title_h = int(27 * LINH) + 8
    row_h = 38
    card_h = pad_in + title_h + len(rows) * row_h + pad_in
    draw.rounded_rectangle([ML, y, W - MR, y + card_h], radius=26, fill=CARD)
    w = tw(rt, recap_title)
    draw.text(((W - w) / 2, y + pad_in), recap_title, font=rt, fill=INK)
    yy = y + pad_in + title_h
    for i, (cat, ex) in enumerate(rows):
        if i:
            draw.line([ML + 30, yy, W - MR - 30, yy], fill=(232, 225, 211), width=1)
        cw = tw(rc, cat) + 20
        draw.rounded_rectangle([ML + 32, yy + 4, ML + 32 + cw, yy + 30],
                               radius=13, fill=MUSTBG)
        draw.text((ML + 42, yy + 5), cat, font=rc, fill=ORANGE_D)
        draw.text((ML + 32 + cw + 14, yy + 5), ex, font=cand, fill=INK)
        yy += row_h
    y += card_h + 26

    fs = F("Medium", 25)
    s = preview
    w = tw(fs, s)
    draw.text(((W - w) / 2, y), s, font=fs, fill=ORANGE_D)
    y += int(25 * LINH) + 40
    fb = F("Bold", 25)
    for i, s in enumerate(["关注我,一起刷完整部剧",
                           "评论区聊聊你记得最牢的一句"]):
        w = tw(fb, s)
        draw.rounded_rectangle([(W - w) / 2 - 22, y, (W + w) / 2 + 22, y + 56],
                               radius=28, fill=INK)
        draw.text(((W - w) / 2, y + 12), s, font=fb, fill=CREAM)
        y += 72
    footer(draw)
    img.save(fname)
    return fname