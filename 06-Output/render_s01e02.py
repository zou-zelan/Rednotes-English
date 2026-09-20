#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""渲染老友记 S01E02 小红书图文 18 张。"""
import os
from xhs_engine import content_page as _content_page
from xhs_pages import cover as _cover, story as _story, hero as _hero, timeline as _timeline, ending as _ending

EP = "S01E02"


def content_page(*a, **kw):
    kw.setdefault("ep", EP)
    return _content_page(*a, **kw)


def story(*a, **kw):
    kw.setdefault("ep", EP)
    return _story(*a, **kw)


def hero(*a, **kw):
    kw.setdefault("ep", EP)
    return _hero(*a, **kw)


def timeline(*a, **kw):
    kw.setdefault("ep", EP)
    return _timeline(*a, **kw)


def ending(*a, **kw):
    kw.setdefault("ep", EP)
    return _ending(*a, **kw)


OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img-S01E02")
os.makedirs(OUT, exist_ok=True)
F = lambda n: os.path.join(OUT, n)


def main():
    _cover(F("S01E02-01.png"), episode="第 2 集",
          quote=[("I never thought", False), ("I'd be here.", True)],
          sub="退婚戒与当爸爸,一集撞成一场手忙脚乱",
          tags=["高频口头禅", "高频短语", "万能句型", "绝妙比喻"],
          credit="老友记 S01E02 · 台词精讲笔记")

    story(F("S01E02-02.png"), 2,
          badge="本集:一条消息与一枚戒指",
          lines=[
              "Carol 约 Ross 出来,当面宣布:她和 Susan 想让他一起抚养孩子",
              "Ross 全程懵圈:从惊喜到惊恐,手忙脚乱只差当场表演杂技",
              "Rachel 硬着头皮去退订婚钻戒,却听说 Barry 已经和伴娘 Mindy 在一起",
              "戒指没退成,新爸爸也当定了——两条线一起炸锅",
          ],
          pill="这一集,几乎每句都值得模仿。")

    content_page(
        F("S01E02-03.png"), 3, "高频口头禅 | 一句顶十句", [
            dict(head=[("You never know.", True)], gloss="谁知道呢 / 说不定",
                 quote=[("Well... ", False), ("You never know.", True)],
                 trans="谁知道呢,说不定呢。",
                 note="万能回答:表“说不准,可能有转机”;别直译“你永远不知道”。"),
            dict(head=[("Got me.", True)], gloss="问住我了 / 我也不知道",
                 quote=[("When did it get so complicated? ", False), ("Got me.", True)],
                 trans="什么时候变得这么复杂?——问住我了。",
                 note="(You) got me. = 问住我了;别字面译成“抓到我了”。"),
            dict(head=[("It's an expression.", True)], gloss="只是个说法",
                 quote=[("What's that supposed to mean? ", False), ("It's an expression.", True)],
                 trans="——你这话什么意思?——没什么,只是个说法。",
                 note="为自己话辩解:这是习语/惯用说法。"),
        ],
        subtitle="三句开场就能用",
        foot="三句背熟,日常对话开场就有。")

    content_page(
        F("S01E02-04.png"), 4, "高频句 | 情绪直说", [
            dict(head=[("Calm down.", True)], gloss="冷静点",
                 quote=[("Yeah, ", False), ("calm down", True), (". You don't see Ross getting all chaotic and twirly...", False)],
                 trans="好了,冷静点。你还没见 Ross 那种手忙脚乱、团团转的样子。",
                 note="劝人淡定的黄金三连;chaotic and twirly = 手忙脚乱。"),
            dict(head=[("You're scaring me.", True)], gloss="你吓到我了",
                 quote=[("Monica, um, ", False), ("you're scaring me.", True)],
                 trans="莫妮卡,呃,你吓到我了。",
                 note="scare 表“使害怕”,比 frighten 日常得多。"),
            dict(head=[("I can't do it.", True)], gloss="我真的做不到",
                 quote=[("I just can't do it.", True)],
                 trans="我真的做不到。",
                 note="极简口语,it 指代上下文;重读 can't 表无奈。"),
        ],
        subtitle="情绪别憋着,直说出来")

    content_page(
        F("S01E02-05.png"), 5, "高频短语 | 说人不说伤", [
            dict(head=[("She has issues.", True)], gloss="她有心结",
                 quote=[("Well, ", False), ("she has issues.", True)],
                 trans="她心结不少。",
                 note="have issues (with) = 有心结/问题,比 has problems 更委婉轻松。"),
            dict(head=[("Very supportive.", True)], gloss="非常支持 / 很能理解",
                 quote=[("Yes, and she's ", False), ("very supportive", True), (".", False)],
                 trans="是的,而且她非常支持(我们这种情况)。",
                 note="人际场合高频形容词:supportive = 支持的、能理解的。"),
            dict(head=[("Give them ammunition", True)], gloss="递给他们把柄",
                 quote=[("I don't want to ", False), ("give them any more ammunition", True), (" than they have.", False)],
                 trans="我不想再递给他们更多可以用来攻击我的把柄。",
                 note="ammunition 本义“弹药”,引申为“话柄”;极实用的引申义。",
                 fix="ammunition 别只当“弹药”,口语里常指“把柄”。"),
        ],
        subtitle="三个词,就够形容一个人")

    content_page(
        F("S01E02-06.png"), 6, "恋爱专题 | 旧账新账", [
            dict(head=[("Had a thing for you", True)], gloss="对你有意思",
                 quote=[("The big one ", False), ("had a thing for you", True), (", didn't she?", False)],
                 trans="那个胖胖的女孩对你有点意思吧?",
                 note="have a thing for sb = 有好感,和 a major crush on 一个意思。"),
            dict(head=[("We're kind of a thing now.", True)], gloss="我们算是一对了",
                 quote=[("Mindy? My maid of honor, Mindy? ", False), ("we're kind of a thing now.", True)],
                 trans="Mindy?我的伴娘 Mindy?——嗯,我们现在算是一对了。",
                 note="be a thing = 在一起了;kind of 表“算是”,低调又轻松。"),
            dict(head=[("Leave a man at the altar", True)], gloss="婚礼当天放鸽子",
                 quote=[("At least she had the chance to ", False), ("leave a man at the altar", True), (".", False)],
                 trans="好吧,至少她有在婚礼上把男人甩掉的机会。",
                 note="leave sb at the altar = 逃婚/放鸽子;altar = 圣坛。"),
        ],
        subtitle="本集最不缺的,就是恋爱梗",
        foot="旧账:逃婚还戒指;新账:一堆新恋情。")

    content_page(
        F("S01E02-07.png"), 7, "吐槽专用 | 损得漂亮", [
            dict(head=[("That borders on child abuse.", True)], gloss="那快算虐待儿童了",
                 quote=[("I think that ", False), ("borders on", True), (" child abuse.", False)],
                 trans="我觉得那都快算虐待儿童了。",
                 note="border on = 近乎、接近(带贬义)。"),
            dict(head=[("That was a cheap shot.", True)], gloss="这挖苦够损",
                 quote=[("I know it was a ", False), ("cheap shot", True), (", but I feel so much better now.", False)],
                 trans="好吧,我知道这挺损的,但我感觉好多了。",
                 note="cheap shot = 恶毒的挖苦(本义:偷袭暗算)。"),
            dict(head=[("You got plugs.", True)], gloss="你植发了吧",
                 quote=[("You got plugs.", True), (" Careful, they haven't quite taken yet.", False)],
                 trans="你植发了。——小心点,还没长稳呢。",
                 note="plugs = 植发块;take = 成活、长好(多义词)。"),
        ],
        subtitle="损人也要损得地道",
        foot="吐槽用词要准,这些可都出自本集台词。")

    content_page(
        F("S01E02-08.png"), 8, "场景口语 | 医院产检", [
            dict(head=[("Are you through with that?", True)], gloss="你用完了吗",
                 quote=[("Are you through with that?", True), (" Thanks.", False)],
                 trans="你用完了吗?谢谢。",
                 note="be through with sth = 用完/做完,比 done with 稍正式。"),
            dict(head=[("Lie back.", True), (" / ", False), ("Tilt your head.", True)], gloss="往后躺 / 头歪一点",
                 quote=[("Uh, ", False), ("lie back", True), (". If you ", False), ("tilt your head", True), (" to the left and relax your eyes...", False)],
                 trans="呃,往后躺。如果头向左侧歪一点,眼睛放松……",
                 note="lie back 仰卧 / lie flat 平躺 / lie down 躺下;tilt = 倾斜。"),
            dict(head=[("Are you welling up?", True)], gloss="你要哭了吧",
                 quote=[("Are you ", False), ("welling up", True), ("?", False)],
                 trans="你要哭了吧?——才没有。——你就是。",
                 note="well up = 眼眶含泪、强忍泪水,比 cry 轻。"),
        ],
        subtitle="产检室的这几句,先学会",
        foot="场景词:B超 sonogram、产前 ob-gyn、恶心 nausea。")

    content_page(
        F("S01E02-09.png"), 9, "高频短语 | 状态与进展", [
            dict(head=[("I got stuck at work.", True)], gloss="被工作缠住了",
                 quote=[("Sorry I'm late. ", False), ("I got stuck at work", True), (".", False)],
                 trans="对不起我迟到了,被工作缠住了。",
                 note="get stuck at/in = 脱不开身;stuck 是 stick 的过去分词。"),
            dict(head=[("If everything works out...", True)], gloss="如果一切顺利",
                 quote=[("If everything works out", True), (" and you end up getting married and having kids...", False)],
                 trans="如果一切顺利,而且你们最后结婚生子……",
                 note="work out = 进展顺利;顺带,end up doing = 最终落得。"),
            dict(head=[("Wind up calling her Geller", True)], gloss="最后简称 Geller",
                 quote=[("He knows they'll ", False), ("wind up calling her Geller", True), (".", False)],
                 trans="他就知道,大家最后会把她简称 Geller。",
                 note="wind up doing = 最终变成,和 end up 通用。"),
        ],
        subtitle="聊聊今天的“进度”")

    content_page(
        F("S01E02-10.png"), 10, "万能句型 | 表态与决定", [
            dict(head=[("It's totally up to me.", True)], gloss="完全由我决定",
                 quote=[("Basically, ", False), ("it's totally up to me", True), (".", False)],
                 trans="基本上,全由我说了算。",
                 note="sth is up to sb = 由某人决定;basically 总结高频词。",
                 how="It's up to you. = 你说了算。"),
            dict(head=[("As far as my parents are concerned", True)], gloss="在我爸妈眼里",
                 quote=[("As far as my parents are concerned", True), (", Ross can do no wrong.", False)],
                 trans="在我爸妈眼里,Ross 怎么做都是对的。",
                 note="as far as sb is concerned = 就某人而言;can do no wrong = 永远没错。"),
            dict(head=[("What does she mean by...?", True)], gloss="她的意思是?",
                 quote=[("What does she mean ", False), ("by", True), (" \"involved\"?", False)],
                 trans="她说“参与”是什么意思?",
                 note="What do you mean by X? = 你说的 X 是什么意思?追问澄清。"),
        ],
        subtitle="给出你的态度",
        foot="三句表态,今天就能用。")

    content_page(
        F("S01E02-11.png"), 11, "万能句型 | 感叹与祝福", [
            dict(head=[("You're gonna be an aunt.", True)], gloss="你要当姑姑啦",
                 quote=[("You're gonna be an aunt.", True), (" ", False), ("- Oh, shut up.", False)],
                 trans="你要当姑姑啦。——哦,你闭嘴。",
                 note="shut up 这里是“真的假的”的亲昵语气,不是骂人。",
                 how="You're gonna be a dad / an uncle.→ 同一句式"),
            dict(head=[("Isn't that amazing?", True)], gloss="是不是很神奇",
                 quote=[("Well, ", False), ("isn't that amazing?", True)],
                 trans="哇,是不是很神奇?",
                 note="反问表感叹,比 That's amazing! 更有情绪。"),
            dict(head=[("We're just waiting for?", True)], gloss="我们在等谁来着?",
                 quote=[("So, uh, ", False), ("we're just waiting for?", True)],
                 trans="那……我们是在等谁来着?",
                 note="半句话用升调让对方补全,逼对方回答,极口语。"),
        ],
        subtitle="惊讶的三种打开方式")

    content_page(
        F("S01E02-12.png"), 12, "万能句型 | 回应与澄清", [
            dict(head=[("This belongs to you.", True)], gloss="这物归原主",
                 quote=[("I guess ", False), ("this belongs to you", True), (". And thank you.", False)],
                 trans="我想这属于你。谢谢你把它给了我。",
                 note="belong to = 属于;归还物品的标准用语。"),
            dict(head=[("Why is she in the title?", True)], gloss="为什么她的名字也在?",
                 quote=[("Wait a minute. ", False), ("Why is she in the title", True), ("?", False)],
                 trans="等等,为什么她的姓氏也出现在名字里?",
                 note="title 此处指“名字/称号”,要结合上下文理解。"),
            dict(head=[("I feel so much better now.", True)], gloss="我感觉好多了",
                 quote=[("It was a cheap shot, but ", False), ("I feel so much better now", True), (".", False)],
                 trans="我知道这是挖苦,但我感觉好太多了。",
                 note="feel/be much better 比较级强化,安慰与自嘲都适用。"),
        ],
        subtitle="接话、还东西,都自然")

    content_page(
        F("S01E02-13.png"), 13, "万能句型 | 比较与夸张", [
            dict(head=[("More than anyone I've ever...", True)], gloss="超过任何人",
                 quote=[("I wanted to hurt you ", False), ("more than I've ever wanted to hurt anyone in my life", True), (".", False)],
                 trans="我想伤害你的愿望,超过我此生想伤害任何人的程度。",
                 note="more than ever / anyone 最高级比较,表达强烈情绪。"),
            dict(head=[("This is not my way.", True)], gloss="绝不是我设想的那种",
                 quote=[("Of all the ways I ever imagined this moment being... ", False), ("this is not my way", True), (".", False)],
                 trans="在我对这一刻的所有想象里,绝没有这一种。",
                 note="of all the X... this is not... = 在一切可能性里偏偏是这样。"),
            dict(head=[("How could I forget?", True)], gloss="我怎么会忘",
                 quote=[("Ross, you remember Susan. ", False), ("How could I forget?", True)],
                 trans="Ross,你还记得 Susan 吧。——我怎么忘得了?",
                 note="反问表“刻骨铭心”,常带讽刺;重读 could 强调。"),
        ],
        subtitle="把话说得更有分量")

    content_page(
        F("S01E02-14.png"), 14, "高频短语 | 一句话接得漂亮", [
            dict(head=[("Speaking of issues...", True)], gloss="说到这茬",
                 quote=[("Speaking of issues", True), (", isn't that your ex-wife?", False)],
                 trans="说到难处,那不是你前妻吗?",
                 note="speaking of... = 既然提到,比 about that 更自然。"),
            dict(head=[("Steer clear of the word \"dumped.\"", True)], gloss="别提“被甩”",
                 quote=[("You may want to ", False), ("steer clear of", True), (" the word \"dumped.\"", False)],
                 trans="你最好别提“被甩”这个字眼。",
                 note="steer clear of = 避开、绕着走,比 avoid 生动。",
                 how="Steer clear of that topic. = 那话题别碰。"),
            dict(head=[("Catch up with you in the Ice Age", True)], gloss="冰河时代再见",
                 quote=[("How about I'll ", False), ("catch up with you", True), (" in the Ice Age?", False)],
                 trans="那咱们冰河时代再见吧(玩笑:不急着找你)。",
                 note="catch up (with sb.) = 追上/叙旧;这里调侃拖很久。"),
        ],
        subtitle="顺口接住,聊天不断档")

    hero(F("S01E02-15.png"), 15, "Ross 得知要当爸爸后,最真实的一句",
         [("I never thought I'd be here.", True)],
         "我从没想过,自己会走到这一步。",
         "Carol 官宣怀孕,Ross 全程震惊。计划再周全,也追不上生活。",
         msg="这句话,说给还没准备好的爸妈,也说给被生活改了剧本的你",
         teaser="本集还有“空壳的男人”“家里的王子”两大妙喻 →")

    content_page(
        F("S01E02-16.png"), 16, "绝妙比喻 | 可模仿的英文", [
            dict(head=[("He's the prince.", True)], gloss="他是家里的“王子”",
                 quote=[("You see, ", False), ("he's the prince", True), (".", False)],
                 trans="你看,他就是那个最受宠的“王子”。",
                 note="比喻家里得宠的孩子;反义 the black sheep(不受宠)。",
                 how="He's the black sheep. = 他是家里不受宠的那个。"),
            dict(head=[("A broken shell of a man", True)], gloss="身心俱碎的空壳",
                 quote=[("He's going to be this ", False), ("broken shell of a man", True), (".", False)],
                 trans="他会变成一个身心俱碎、空壳般的男人。",
                 note="shell of a man/person = 行尸走肉;文学化但美剧仍常用。"),
            dict(head=[("That opens my cervix.", True)], gloss="那会让我“开宫颈”",
                 quote=[("Ross? ", False), ("That opens my cervix.", True)],
                 trans="Ross,那(声音)会让我子宫颈打开。",
                 note="麻醉医生逗孕妇的荤笑;cervix = 子宫颈。"),
        ],
        subtitle="三个比喻,记下来,写作文也能用")

    timeline(F("S01E02-17.png"), 17,
             badge="本集彩蛋 | 一集双线",
             title="从退钻戒到当爸爸,一集双线",
             items=[
                 ("开场", "Rachel 揣着钻戒去退,一路磨蹭:“Basically, it's totally up to me.”(基本上全由我说了算)"),
                 ("中段", "Carol 约 Ross 摊牌:想让他一起养孩子。Ross 全程懵圈:“No matter what I do, I'm still gonna be a father.”"),
                 ("结尾", "Rachel 撞见 Barry 和 Mindy 已经在一起,戒指没退成;Ross 在走廊呆立,反复拍自己额头。"),
             ],
             pill="旧婚礼撞上新生命:计划再周全,也追不上生活。")

    ending(F("S01E02-18.png"), 18,
           badge="第 2 集 · 完",
           quote=[("I never thought I'd be here.", True)],
           rows=[
               ("高频口头禅", "You never know · Got me · It's an expression"),
               ("高频短语", "calm down · steer clear of · I got stuck at work"),
               ("恋爱与状态", "had a thing for · we're a thing now · she has issues"),
               ("万能句型", "It's totally up to me · This belongs to you · How could I forget"),
               ("绝妙比喻", "he's the prince · a shell of a man · opens my cervix"),
           ],
           preview="下集预告 S01E03:Monica 的巨款、Chandler 的烟,和罐里的拇指……")


if __name__ == "__main__":
    from xhs_engine import BOTTOMS
    main()
    print("done:", sorted(os.listdir(OUT)))
    for no, y in sorted(BOTTOMS):
        flag = " <-- COLLIDES FOOTER (>1370)" if y > 1370 else ""
        print(f"  page {no:02d}: content bottom y={y}{flag}")