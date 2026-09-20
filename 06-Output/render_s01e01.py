#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""渲染老友记 S01E01 小红书图文 18 张。"""
import os
from xhs_engine import content_page
from xhs_pages import cover, story, hero, timeline, ending

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img-S01E01")
os.makedirs(OUT, exist_ok=True)
F = lambda n: os.path.join(OUT, n)


def main():
    cover(F("S01E01-01.png"))
    story(F("S01E01-02.png"), 2)

    content_page(
        F("S01E01-03.png"), 3, "必背 | 听懂美剧第一步", [
            dict(head=[("gotta", True), (" = have got to", False)], gloss="一定 / 肯定",
                 quote=[("There's ", False), ("gotta", True), (" be something wrong with him.", False)],
                 trans="那男的肯定有问题。", note="gotta 表“一定/肯定”,比 must 更生活化。"),
            dict(head=[("wanna", True), (" = want to", False)], gloss="想要",
                 quote=[("I just ", False), ("wanna", True), (" be married again.", False)],
                 trans="我就想再结一次婚!(自嘲:还想要一百万呢)"),
            dict(head=[("gonna", True), (" = going to", False)], gloss="将要 / 打算",
                 quote=[("I'm ", False), ("gonna", True), (" go get one of those job things.", False)],
                 trans="我要去弄一个那种“工作”回来。",
                 fix="疑问句别缩写:Gonna you go? ✗ → Are you going to…? ✓"),
        ],
        subtitle="高频缩略三兄弟,先背熟再刷剧",
        foot="听到 gotta / wanna / gonna,先还原成 got to / want to / going to,语速瞬间 2 倍速。")

    content_page(
        F("S01E01-04.png"), 4, "高频口头禅 | 一句顶十句", [
            dict(head=[("Are you kidding?", True)], gloss="你开玩笑吧?",
                 quote=[("You got a job?", False), ("——", False), ("Are you kidding?", True), (" I'm trained for nothing.", False)],
                 trans="你找到工作了?——开什么玩笑?我啥技能都没有。"),
            dict(head=[("I have no idea.", True)], gloss="我完全不知道",
                 quote=[("What's this?", False), ("——", False), ("I have no idea.", True)],
                 trans="这是什么?——我也不晓得。", note="表达“不知道”,比 I don't know 更有力度。"),
            dict(head=[("I'll be fine.", True)], gloss="我没事 / 我能行",
                 quote=[("Go, ", False), ("I'll be fine.", True)],
                 trans="你去吧,我没事的。"),
        ],
        subtitle="社交瞬间开口就能用",
        foot="三句背熟,日常对话开口就有。")

    content_page(
        F("S01E01-05.png"), 5, "心情万能句 | 情绪表达", [
            dict(head=[("I can't stop smiling.", True)], gloss="我笑得根本停不下来",
                 quote=[("Did you talk to Barry? ", False), ("I can't stop smiling.", True)],
                 trans="你跟 Barry 谈了吗?我笑得根本停不下来。",
                 how="I can't stop laughing / eating / worrying.(根本停不下来…)",
                 fix="固定搭配是 can't stop + doing,别写成 stop to smile。"),
            dict(head=[("It's been a long day.", True)], gloss="今天真是漫长的一天",
                 quote=[("Oh, sure. ", False), ("It's been a long day.", True)],
                 trans="好,行。今天真是够长的一天。", note="疲惫一天最自然的总结句,比 I'm tired 高级。"),
            dict(head=[("Oh, wow, ", False), ("are you in trouble!", True)], gloss="哇,你完蛋了",
                 quote=[("Oh, wow, ", False), ("are you in trouble!", True)],
                 trans="哇哦,这下你可栽了!(你这是被爱情套牢了)",
                 note="感叹句主谓倒装=You're in big trouble,表“你被套牢了”。"),
        ],
        subtitle="心情、状态,这样表达才对味")

    content_page(
        F("S01E01-06.png"), 6, "高频句 | 闲聊与八卦", [
            dict(head=[("Wish me luck!", True), (" / ", False), ("What for?", True)], gloss="祝我好运吧! / 为什么?",
                 quote=[("Oh, ", False), ("wish me luck!", True), ("——", False), ("What for?", True)],
                 trans="祝我好运吧!——为什么呀?", note="What for? = Why? 朋友明知你没技能,故意反问,损到飞起。",
                 fix="What for? 的 for 别吞音;它= Why 的口语版。"),
            dict(head=[("I should've caught on.", True)], gloss="我本该早察觉",
                 quote=[("I ", False), ("should've caught on", True), (" when she went to the dentist four and five times a week.", False)],
                 trans="她一周去四五次牙医,我本该早就察觉了。", note="should've = should have,别读成 should of;catch on = 察觉。"),
            dict(head=[("You had sex, didn't you?", True)], gloss="你跟人睡了,对吧?",
                 quote=[("Welcome back. How was Florida? ", False), ("You had sex, didn't you?", True)],
                 trans="欢迎回来,佛罗里达怎样?——你跟人睡了,对吧?(直球开涮)",
                 note="美式朋友间直球八卦,别当疑问句温柔地念。"),
        ],
        subtitle="三句,撑起一次对话")

    content_page(
        F("S01E01-07.png"), 7, "吐槽专用 | 情绪释放", [
            dict(head=[("To hell with her!", True)], gloss="去她的!",
                 quote=[("To hell with her.", True), (" She left me!", False)],
                 trans="去她的!她甩了我!"),
            dict(head=[("You got screwed.", True)], gloss="你被坑惨了",
                 quote=[("…What did you get?——", False), ("You got screwed.", True)],
                 trans="…你拿到了什么?——你被坑惨了。"),
            dict(head=[("Give her a break.", True)], gloss="饶了她吧",
                 quote=[("Give her a break.", True), (" It's hard being on your own for the first time.", False)],
                 trans="饶了她吧。第一次独立生活不容易。", note="give sb. a break = 别刁难、让人喘口气。"),
        ],
        subtitle="吐槽的力气,用这三句",
        foot="get screwed = 被坑、被耍,分手分家产语境下特别形象。")

    content_page(
        F("S01E01-08.png"), 8, "恋爱 / 分手 | 高频短语", [
            dict(head=[("Walk out on sb.", True)], gloss="甩了对方、一走了之",
                 quote=[("Ever since she ", False), ("walked out on", True), (" me, I…", False)],
                 trans="自从她甩了我、离家而去,我…"),
            dict(head=[("Hit on sb.", True)], gloss="搭讪、撩",
                 quote=[("Joey, ", False), ("stop hitting on her.", True), (" It's her wedding day.", False)],
                 trans="乔伊,别撩她了。今天可是她逃婚的日子。"),
            dict(head=[("Keep fixating on sth.", True)], gloss="一直揪着不放",
                 quote=[("Why does everyone keep ", False), ("fixating on", True), (" that?", False)],
                 trans="为什么大家都揪着这事不放?", note="hit on 比 flirt with 更直接,美式俚语感十足。",
                 fix="fixating on 的 on 别丢:是 keep fixating on that。"),
        ],
        subtitle="一句句都有戏")

    content_page(
        F("S01E01-09.png"), 9, "闲聊万能三连 | 破冰", [
            dict(head=[("What are you up to?", True)], gloss="今晚有什么安排?",
                 quote=[("So, Rachel, ", False), ("what are you up to", True), (" tonight?", False)],
                 trans="那,瑞秋,你今晚有什么打算?", note="比 What are you doing? 更地道。",
                 fix="be up to + doing = 打算做;打招呼是 What's up?。"),
            dict(head=[("Hang out", True)], gloss="待着、闲逛",
                 quote=[("I'm just gonna ", False), ("hang out", True), (" here tonight.", False)],
                 trans="谢了,不过我今晚就想在这待着。"),
            dict(head=[("End up doing sth.", True)], gloss="兜兜转转最后…",
                 quote=[("I ", False), ("ended up living with", True), (" this albino guy…", False)],
                 trans="我最后只能跟一个擦车窗的小哥合住…", note="end up + doing = 落得…,带点无奈。"),
        ],
        subtitle="社交场合这三句够用")

    content_page(
        F("S01E01-10.png"), 10, "情感话题 | 表白与翻车", [
            dict(head=[("Have a (major) crush on sb.", True)], gloss="疯狂暗恋某人",
                 quote=[("Back in high school I had ", False), ("a major crush on", True), (" you.", False)],
                 trans="高中的时候,我疯狂暗恋过你。"),
            dict(head=[("It was a line.", True)], gloss="那不过是套路",
                 quote=[("Of course ", False), ("it was a line.", True)],
                 trans="那当然只是哄你上床的套路。", note="line = 搭讪花言巧语,还有 pick-up line(搭讪台词)。",
                 fix="line 这里是“套路/花言巧语”,不是“台词”,直译会闹笑话。"),
        ],
        subtitle="本集 Ross 表白,笑点在这一句",
        foot="结尾 Ross 一句 “I just grabbed a spoon.” 呼应开头,详情见目录页 17。")

    content_page(
        F("S01E01-11.png"), 11, "场景口语 | 即学即用", [
            dict(head=[("What's with you?", True)], gloss="你怎么回事?",
                 quote=[("Hey, ", False), ("what's with you?", True)],
                 trans="嘿,你这人怎么了?"),
            dict(head=[("Buzz him in.", True)], gloss="放他进来",
                 quote=[("Uh, it's Paul.", False), ("——", False), ("Buzz him in.", True)],
                 trans="是保罗(按门铃)。——放他进来吧。", note="美式公寓门禁,buzz = 哔一声按铃开门。",
                 fix="buzz 作动词就是“按铃放行”,地道直接。"),
            dict(head=[("I'm trained for nothing.", True)], gloss="我啥技能都没有",
                 quote=[("I'm ", False), ("trained for nothing.", True), (" I was laughed out of 12 interviews today.", False)],
                 trans="我什么技能都没学过。今天 12 场面试全把我轰出来了。"),
        ],
        subtitle="三个场景,三个词")

    content_page(
        F("S01E01-12.png"), 12, "万能句型 | 回避与救场", [
            dict(head=[("There's nothing to tell.", True)], gloss="没什么好说的",
                 quote=[("There's nothing to tell.", True), (" It's just some guy I work with.", False)],
                 trans="没什么可说的。就是一起工作的一个男的。", note="回避追问的万能挡箭牌。"),
            dict(head=[("Did I say that out loud?", True)], gloss="我把心里话说出来了吗?",
                 quote=[("Sometimes I wish I was a lesbian. / ", False), ("Did I say that out loud?", True)],
                 trans="真希望自己是蕾丝边。/ 我把这话说出口了吗?", note="不小心说出心里话的救场金句,一定要背下来。",
                 fix="out loud 是固定短语,别替换成 loudly。"),
            dict(head=[("Being spit on is probably not what you need right now.", True)], gloss="你现在最不缺的是被喷一脸口水",
                 quote=[("It's okay. ", False), ("Being spit on is probably not what you need right now.", True)],
                 trans="没关系。你现在最不缺的就是被喷一脸口水。(被咖啡喷到后的解围金句)",
                 note="用“对眼下最不需要的事”幽默解围,化解尴尬的典范。"),
        ],
        subtitle="说错话、被追问,都有救")

    content_page(
        F("S01E01-13.png"), 13, "万能句型 | 感叹与类比", [
            dict(head=[("Talk about your…", True)], gloss="那可真叫…",
                 quote=[("Aruba. This time of year? ", False), ("Talk about your…", True), (" big lizards.", False)],
                 trans="阿鲁巴?这个季节?说到那里的…大蜥蜴。",
                 how="Talk about a disaster! = 那可真叫灾难!"),
            dict(head=[("It's more of a … kind of …", True)], gloss="这更像是…那种…",
                 quote=[("No, it's more of a ", False), ("fifth-date kind of revelation.", True)],
                 trans="不,这更像是该在第五次约会时才揭晓的事。", note="more of a + 名词 = 更像某种东西。",
                 fix="more of a 接名词短语;真要加形容词用 it's more + 形容词。"),
            dict(head=[("How clean can teeth get?", True)], gloss="牙还能洗多干净?",
                 quote=[("I mean, ", False), ("how clean can teeth get?", True)],
                 trans="我是说,牙还能洗多干净?(一周去五次牙医也太离谱)",
                 note="反问表“此事实在离谱”,自嘲被绿而未察觉。"),
        ],
        subtitle="感叹、掩饰,一句话切换")

    content_page(
        F("S01E01-14.png"), 14, "万能句型 | 得体邀约", [
            dict(head=[("Do you think it would be okay if…?", True)], gloss="你觉得可以的话…",
                 quote=[("Do you think it would be okay if", True), (" I ask you out sometime, maybe?", False)],
                 trans="你觉得可以的话,我改天约你出来,行不行?", note="最委婉、最有风度的邀约句式。"),
            dict(head=[("I was supposed to be headed for…", True)], gloss="我本该正前往…",
                 quote=[("I was ", False), ("supposed to be headed for", True), (" Aruba on my honeymoon.", False)],
                 trans="我这会儿本该正在去阿鲁巴度蜜月的路上。", note="be supposed to = 本该;be headed for = 朝着…前进。",
                 fix="supposed 里的 d 要念出来,别读成 suppose to。"),
            dict(head=[("Try not to let my vulnerability become a factor.", True)], gloss="别让我的脆弱影响你的决定",
                 quote=[("And ", False), ("try not to let my vulnerability become any kind of a factor", True), (" here.", False)],
                 trans="而且,尽量别让我的脆弱影响到你做决定。(刚表白就让人别心软)",
                 note="Ross 式自嘲收尾;factor = 考虑因素。"),
        ],
        subtitle="约人、自嘲,都拿得出手")

    hero(F("S01E01-15.png"), 15, "本集最经典的一句",
         [("Welcome to the real world.", False),
          ("It sucks. You're gonna love it.", True)],
         "欢迎来到现实世界。它糟透了,但你会爱上它的。",
         "Monica 端着咖啡对逃婚的 Rachel 说出这句。哲理 + 自嘲,被引用至今。")

    content_page(
        F("S01E01-16.png"), 16, "绝妙比喻 | 可模仿的英文", [
            dict(head=[("You're a shoe!", True), (" / ", False), ("Wanna be a purse?", True)], gloss="鞋的人生 / 包的人生",
                 quote=[("Everyone's always told me, ", False), ("\"You're a shoe!\"", True), (" What if I wanna be a purse? It's a metaphor, Daddy!", False)],
                 trans="所有人都说“你是一双鞋!”那我想当个包呢?——这是比喻啊,爸!",
                 note="鞋 = 按部就班的“新娘人生”;包 = 自由自主。"),
            dict(head=[("One flavor of ice cream", True)], gloss="冰激凌口味比喻",
                 quote=[("That's like saying ", False), ("there's only one flavor of ice cream", True), (" for you. There's lots of flavors out there.", False)],
                 trans="这就像说世界上只配有一种口味的冰激凌给你。外面口味多着呢。",
                 note="劝死脑筋别认定“唯一人选”,最强类比句式。"),
            dict(head=[("Slept with a hanger in your mouth", True)], gloss="笑得合不拢嘴",
                 quote=[("You look like you ", False), ("slept with a hanger in your mouth.", True)],
                 trans="你看上去像嘴里卡了个衣架睡了一觉(笑不拢嘴)。",
                 note="画面感极强的美式夸张比喻。"),
        ],
        subtitle="三个比喻,记下来,写作文也能用")

    timeline(F("S01E01-17.png"), 17)

    ending(F("S01E01-18.png"), 18)


if __name__ == "__main__":
    from xhs_engine import BOTTOMS
    main()
    print("done:", sorted(os.listdir(OUT)))
    for no, y in sorted(BOTTOMS):
        flag = " <-- COLLIDES FOOTER (>1370)" if y > 1370 else ""
        print(f"  page {no:02d}: content bottom y={y}{flag}")