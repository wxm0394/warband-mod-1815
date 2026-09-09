import re
import os

out_dir = "languages/cns"
os.makedirs(out_dir, exist_ok=True)

def to_cns(text):
    res = []
    for ch in text:
        if ('\u4e00' <= ch <= '\u9fff') or ('\u3000' <= ch <= '\u303f') or ('\uff00' <= ch <= '\uffef'):
            res.append(ch + ' ')
        else:
            res.append(ch)
    s = "".join(res)
    return re.sub(r' +', ' ', s).strip()

# ==========================================
# 1. PARTY_TEMPLATES.CSV
# ==========================================
pt_map = {
    "pt_none": "无",
    "pt_rescued_prisoners": "获救的俘虏",
    "pt_enemy": "敌军部队",
    "pt_hero_party": "将领部队",
    "pt_village_defenders": "村庄民团",
    "pt_cattle_herd": "牛群",
    "pt_looters": "强盗流民",
    "pt_manhunters": "乌兰枪骑兵巡逻队",
    "pt_black_khergit_raiders": "黑骑兵劫掠队",
    "pt_dark_hunters": "暗夜猎手",
    "pt_forest_bandits": "法军骑兵巡逻队",
    "pt_taiga_bandits": "法军巡逻小队",
    "pt_steppe_bandits": "近卫骑兵巡逻队",
    "pt_sea_raiders": "后备军游击队",
    "pt_mountain_bandits": "逃兵武装队",
    "pt_desert_bandits": "国境步兵巡逻队",
    "pt_deserters": "溃兵脱团者",
    "pt_merchant_caravan": "商队",
    "pt_troublesome_bandits": "难缠的匪徒",
    "pt_bandits_awaiting_ransom": "等待赎金的匪徒",
    "pt_kidnapped_girl": "被绑架的少女",
    "pt_village_farmers": "村民",
    "pt_spy_partners": "不起眼的旅人",
    "pt_runaway_serfs": "逃亡农奴",
    "pt_spy": "普通市民",
    "pt_sacrificed_messenger": "殉职信使",
    "pt_forager_party": "征粮队",
    "pt_scout_party": "侦察小队",
    "pt_patrol_party": "巡逻队",
    "pt_messenger_party": "联络信使",
    "pt_raider_party": "突袭小队",
    "pt_raider_captives": "突袭队俘虏",
    "pt_kingdom_caravan_party": "王国商队",
    "pt_prisoner_train_party": "战俘押送队",
    "pt_default_prisoners": "俘虏",
    "pt_routed_warriors": "溃散败兵",
    "pt_center_reinforcements": "守备援军",
    "pt_kingdom_hero_party": "主力军团",
    "pt_forest_bandit_lair": "森林营地",
    "pt_taiga_bandit_lair": "冻原哨所",
    "pt_steppe_bandit_lair": "平原据点",
    "pt_sea_raider_landing": "登陆据点",
    "pt_mountain_bandit_hideout": "山岭藏匿点",
    "pt_desert_bandit_lair": "边境据点",
    "pt_looter_lair": "绑匪巢穴",
    "pt_leaded_looters": "匪帮团伙",
    "pt_dplmc_spouse": "你的配偶",
    "pt_dplmc_gift_caravan": "你的护送商队",
    "pt_dplmc_recruiter": "募兵官",
    "pt_entrench": "野战堑壕工事"
}

print("Writing party_templates.csv...")
with open(f"{out_dir}/party_templates.csv", "w", encoding="utf-8-sig", newline="\r\n") as f:
    for k, v in pt_map.items():
        f.write(f"{k}|{to_cns(v)}\r\n")

# ==========================================
# 2. TROOPS.CSV
# ==========================================
troop_terms = [
    # Ordinals
    (r"\b1st\b", "第1"), (r"\b2nd\b", "第2"), (r"\b3rd\b", "第3"), (r"\b4th\b", "第4"),
    (r"\b5th\b", "第5"), (r"\b6th\b", "第6"), (r"\b7th\b", "第7"), (r"\b8th\b", "第8"),
    (r"\b9th\b", "第9"), (r"\b10th\b", "第10"), (r"\b11th\b", "第11"), (r"\b12th\b", "第12"),
    (r"\b13th\b", "第13"), (r"\b14th\b", "第14"), (r"\b15th\b", "第15"), (r"\b18th\b", "第18"),
    (r"\b23rd\b", "第23"), (r"\b27th\b", "第27"), (r"\b28th\b", "第28"), (r"\b30th\b", "第30"),
    (r"\b32nd\b", "第32"), (r"\b33rd\b", "第33"), (r"\b42nd\b", "第42"), (r"\b44th\b", "第44"),
    (r"\b45th\b", "第45"), (r"\b51st\b", "第51"), (r"\b52nd\b", "第52"), (r"\b69th\b", "第69"),
    (r"\b71st\b", "第71"), (r"\b73rd\b", "第73"), (r"\b79th\b", "第79"), (r"\b84th\b", "第84"),
    (r"\b92nd\b", "第92"), (r"\b95th\b", "第95步枪团"),

    # Guards & Elite units
    (r"\bOld Guard\b", "老近卫军"),
    (r"\bYoung Guard\b", "青年近卫军"),
    (r"\bMiddle Guard\b", "中坚近卫军"),
    (r"\bColdstream Guard\b", "冷溪近卫军"),
    (r"\bColdstream\b", "冷溪近卫军"),
    (r"\bFoot Guard\b", "近卫步兵"),
    (r"\bLife Guard\b", "皇家近卫骑兵"),
    (r"\bHorse Guard\b", "近卫骑兵"),
    (r"\bBlack Watch\b", "黑卫士兵团"),
    (r"\bScots Grey\b", "苏格兰皇家灰骑兵"),
    (r"\bGordon Highlander\b", "戈登高地步兵"),
    (r"\bHighlander\b", "苏格兰高地步兵"),
    (r"\bHighland\b", "高地"),
    (r"\bKGL\b", "英王德意志军团"),
    (r"\bKings German Legion\b", "英王德意志军团"),

    # Leaders & Historical Figures
    (r"\bNapoleon Bonaparte\b", "拿破仑·波拿巴"),
    (r"\bNapoleon\b", "拿破仑·波拿巴"),
    (r"\bBonaparte\b", "波拿巴"),
    (r"\bDuke of Wellington\b", "威灵顿公爵"),
    (r"\bWellington\b", "威灵顿公爵"),
    (r"\bField Marshal Blucher\b", "布吕歇尔陆军元帅"),
    (r"\bBlucher\b", "布吕歇尔元帅"),
    (r"\bBlücher\b", "布吕歇尔元帅"),
    (r"\bMarshal Ney\b", "内伊元帅"),
    (r"\bNey\b", "内伊元帅"),
    (r"\bMarshal Grouchy\b", "格鲁希元帅"),
    (r"\bGrouchy\b", "格鲁希元帅"),
    (r"\bMarshal Davout\b", "达武元帅"),
    (r"\bDavout\b", "达武元帅"),
    (r"\bMarshal Soult\b", "苏尔特元帅"),
    (r"\bSoult\b", "苏尔特元帅"),
    (r"\bMarshal Murat\b", "缪拉元帅"),
    (r"\bMurat\b", "缪拉元帅"),
    (r"\bLord Uxbridge\b", "厄克斯布里奇伯爵"),
    (r"\bUxbridge\b", "厄克斯布里奇伯爵"),
    (r"\bGeneral Picton\b", "皮克顿将军"),
    (r"\bPicton\b", "皮克顿将军"),
    (r"\bPrince of Orange\b", "奥兰治亲王"),
    (r"\bOrange\b", "奥兰治亲王"),
    (r"\bDuke of Brunswick\b", "布伦瑞克公爵"),
    (r"\bBrunswick\b", "布伦瑞克"),
    (r"\bPrince Schwarzenberg\b", "施瓦岑贝格亲王"),
    (r"\bSchwarzenberg\b", "施瓦岑贝格亲王"),
    (r"\bGeneral Gneisenau\b", "格奈森瑙将军"),
    (r"\bGeneral Bulow\b", "比洛将军"),
    (r"\bGeneral Zieten\b", "齐腾将军"),
    (r"\bGeneral Pirch\b", "皮希将军"),
    (r"\bArchduke Charles\b", "卡尔大公"),
    (r"\bArchduke John\b", "约翰大公"),
    (r"\bArchduke\b", "大公"),
    (r"\bKing Friedrich Wilhelm\b", "腓特烈·威廉三世国王"),
    (r"\bKing George\b", "乔治国王"),
    (r"\bTsar Alexander\b", "亚历山大一世沙皇"),
    (r"\bEmperor Francis\b", "弗朗茨一世皇帝"),

    # Military Branches & Troop Types
    (r"\bLine Infantry\b", "线列步兵"),
    (r"\bFusilier\b", "燧发枪兵"),
    (r"\bGrenadier\b", "掷弹兵"),
    (r"\bVoltigeur\b", "轻步兵散兵"),
    (r"\bChasseur a Cheval\b", "猎骑兵"),
    (r"\bChasseur\b", "猎兵"),
    (r"\bJaeger\b", "猎兵"),
    (r"\bJäger\b", "猎兵"),
    (r"\bLandwehr\b", "后备民兵"),
    (r"\bMilitia\b", "民兵"),
    (r"\bGrenzer\b", "边防步兵"),
    (r"\bGrenz\b", "边防步兵"),
    (r"\bHussar\b", "骠骑兵"),
    (r"\bDragoon\b", "龙骑兵"),
    (r"\bCuirassier\b", "胸甲骑兵"),
    (r"\bLancer\b", "枪骑兵"),
    (r"\bUhlan\b", "乌兰枪骑兵"),
    (r"\bCarabineer\b", "卡宾骑兵"),
    (r"\bCarabinier\b", "卡宾骑兵"),
    (r"\bCavalry\b", "骑兵"),
    (r"\bInfantry\b", "步兵"),
    (r"\bFootman\b", "步卒"),
    (r"\bArtillery\b", "炮兵"),
    (r"\bCannoneer\b", "加农炮手"),
    (r"\bGunner\b", "炮手"),
    (r"\bSapper\b", "工兵"),
    (r"\bPioneer\b", "工兵先锋"),
    (r"\bMarine\b", "海军陆战队"),
    (r"\bPartisan\b", "游击队员"),
    (r"\bRifleman\b", "步枪兵"),
    (r"\bSkirmisher\b", "散兵"),
    (r"\bSharpshooter\b", "神射手"),
    (r"\bMarksman\b", "神射手"),
    (r"\bSniper\b", "狙击手"),
    (r"\bGuard\b", "近卫军"),

    # Ranks & Titles
    (r"\bField Marshal\b", "陆军元帅"),
    (r"\bMarshal\b", "元帅"),
    (r"\bGeneral\b", "将军"),
    (r"\bLieutenant General\b", "中将"),
    (r"\bMajor General\b", "少将"),
    (r"\bBrigadier General\b", "准将"),
    (r"\bColonel\b", "上校"),
    (r"\bLieutenant Colonel\b", "中校"),
    (r"\bMajor\b", "少校"),
    (r"\bCaptain\b", "上尉"),
    (r"\bLieutenant\b", "中尉"),
    (r"\bCornet\b", "少尉旗手"),
    (r"\bEnsign\b", "少尉少官"),
    (r"\bSergeant Major\b", "军士长"),
    (r"\bSergeant\b", "军士"),
    (r"\bCorporal\b", "下士"),
    (r"\bOfficer\b", "军官"),
    (r"\bStandard Bearer\b", "掌旗官"),
    (r"\bFlagbearer\b", "掌旗官"),
    (r"\bFlagcarrier\b", "掌旗官"),
    (r"\bDrummer\b", "鼓手"),
    (r"\bFifer\b", "笛手"),
    (r"\bBugler\b", "号手"),
    (r"\bTrumpeter\b", "骑兵号手"),

    # Nationalities & Regions
    (r"\bFrench\b", "法国"),
    (r"\bBritish\b", "英国"),
    (r"\bPrussian\b", "普鲁士"),
    (r"\bAustrian\b", "奥地利"),
    (r"\bRussian\b", "俄罗斯"),
    (r"\bDutch\b", "荷兰"),
    (r"\bBelgian\b", "比利时"),
    (r"\bGerman\b", "德意志"),
    (r"\bBavarian\b", "巴伐利亚"),
    (r"\bBayerische\b", "巴伐利亚"),
    (r"\bSaxon\b", "萨克森"),
    (r"\bHanoverian\b", "汉诺威"),
    (r"\bHannover\b", "汉诺威"),
    (r"\bNassau\b", "拿骚"),
    (r"\bHessian\b", "黑森"),
    (r"\bHessen\b", "黑森"),
    (r"\bPolish\b", "波兰"),
    (r"\bHungarian\b", "匈牙利"),
    (r"\bSpanish\b", "西班牙"),
    (r"\bPortuguese\b", "葡萄牙"),
    (r"\bItalian\b", "意大利"),

    # Qualifiers & Native
    (r"\bRecruit\b", "新兵"),
    (r"\bVeteran\b", "老兵"),
    (r"\bElite\b", "精锐"),
    (r"\bRoyal\b", "皇家"),
    (r"\bImperial\b", "帝国"),
    (r"\bDeserter\b", "逃兵"),
    (r"\bBandit\b", "强盗"),
    (r"\bRobber\b", "土匪"),
    (r"\bLooter\b", "劫匪"),
    (r"\bNovice Fighter\b", "初级格斗士"),
    (r"\bRegular Fighter\b", "普通格斗士"),
    (r"\bChampion Fighter\b", "冠军格斗士"),
    (r"\bPlayer\b", "玩家"),
    (r"\bMerchant\b", "商人"),
    (r"\bTavern Keeper\b", "酒馆老板"),
    (r"\bArmorer\b", "军械盔甲商"),
    (r"\bWeaponsmith\b", "武器铁匠"),
    (r"\bHorse Merchant\b", "马贩"),
    (r"\bArena Master\b", "竞技场主持人"),
    (r"\bMayor\b", "镇长"),
    (r"\bVillage Elder\b", "村长"),
    (r"\bRansom Broker\b", "奴隶贩子/赎金经纪人"),
    (r"\bTraveller\b", "旅行者"),
    (r"\bGuild Master\b", "工商业行长"),
    (r"\bMercenary\b", "雇佣兵"),
    (r"\bKing\b", "国王"),
    (r"\bEmperor\b", "皇帝"),
    (r"\bDuke\b", "公爵"),
    (r"\bPrince\b", "亲王"),
    (r"\bCount\b", "伯爵"),
    (r"\bBaron\b", "男爵"),
    (r"\bLord\b", "领主"),
    (r"\bLady\b", "贵夫人")
]

def clean_troop_name(s):
    s = s.replace("_", " ")
    for pattern, rep in troop_terms:
        s = re.sub(pattern, rep, s, flags=re.IGNORECASE)
    # clean multiple spaces
    s = re.sub(r' +', ' ', s).strip()
    return s

troops_out = []
with open("troops.txt", encoding="latin-1") as f:
    for line in f:
        line_s = line.strip()
        if line_s.startswith("trp_"):
            parts = line_s.split()
            tid = parts[0]
            name = parts[1]
            c_name = clean_troop_name(name)
            troops_out.append((tid, to_cns(c_name)))
            troops_out.append((f"{tid}_pl", to_cns(c_name)))

with open(f"{out_dir}/troops.csv", "w", encoding="utf-8-sig", newline="\r\n") as f:
    for tid, s in troops_out:
        f.write(f"{tid}|{s}\r\n")

print(f"Written {len(troops_out)} troop string entries to {out_dir}/troops.csv")

# ==========================================
# 3. ITEM_KINDS.CSV
# ==========================================
item_terms = [
    # Firearms & Ammo
    (r"\bBaker Rifle\b", "贝克线膛步枪"),
    (r"\bBaker\b", "贝克步枪"),
    (r"\bBrown Bess\b", "褐贝斯燧发枪"),
    (r"\bCharleville\b", "查尔维尔燧发枪"),
    (r"\bPotsdam\b", "波茨坦燧发枪"),
    (r"\bMusket with Bayonet\b", "带刺刀燧发枪"),
    (r"\bFlintlock Musket\b", "燧发枪"),
    (r"\bMusket\b", "燧发枪"),
    (r"\bRifle\b", "步枪"),
    (r"\bCarbine\b", "卡宾枪"),
    (r"\bBlunderbuss\b", "短管霰弹枪"),
    (r"\bPistol\b", "手枪"),
    (r"\bPocket Pistol\b", "便携小手枪"),
    (r"\bCavalry Pistol\b", "骑兵手枪"),
    (r"\bHeavy Cavalry Pistol\b", "重骑兵手枪"),
    (r"\bDouble Barrel\b", "双管"),
    (r"\bCartridge\b", "纸包定装弹药"),
    (r"\bCartridges\b", "纸包定装弹药"),
    (r"\bBullet\b", "铅弹"),
    (r"\bBullets\b", "铅弹"),
    (r"\bRound Shot\b", "实心加农炮弹"),
    (r"\bCanister Shot\b", "霰弹筒"),
    (r"\bCannon Ball\b", "加农炮弹"),
    (r"\bCannon\b", "加农炮"),

    # Melee Weapons
    (r"\bBayonet\b", "刺刀"),
    (r"\bSocket Bayonet\b", "套筒刺刀"),
    (r"\bSword Bayonet\b", "剑形刺刀"),
    (r"\bBriquet\b", "短弯刀"),
    (r"\bHeavy Cavalry Sabre\b", "重骑兵马刀"),
    (r"\bLight Cavalry Sabre\b", "轻骑兵马刀"),
    (r"\bCavalry Sabre\b", "骑兵马刀"),
    (r"\bSabre\b", "马刀"),
    (r"\bSaber\b", "马刀"),
    (r"\bPallasch\b", "重骑兵阔剑"),
    (r"\bClaymore\b", "苏格兰阔剑"),
    (r"\bBroadsword\b", "阔剑"),
    (r"\bShort Sword\b", "短剑"),
    (r"\bSpadroon\b", "军官佩剑"),
    (r"\bOfficer Sword\b", "军官剑"),
    (r"\bSword\b", "军剑"),
    (r"\bLance\b", "骑枪"),
    (r"\bSpear\b", "长矛"),
    (r"\bPike\b", "长枪"),
    (r"\bHalberd\b", "长戟"),
    (r"\bDagger\b", "匕首"),
    (r"\bDirk\b", "苏格兰短剑"),
    (r"\bKnife\b", "猎刀"),
    (r"\bClub\b", "短棍"),
    (r"\bMace\b", "钝锤"),
    (r"\bStaff\b", "长棍"),
    (r"\bAxe\b", "斧"),
    (r"\bBattle Axe\b", "战斧"),

    # Headgear
    (r"\bWaterloo Shako\b", "滑铁卢筒形军帽"),
    (r"\bBelgic Shako\b", "比利时筒形军帽"),
    (r"\bStovepipe Shako\b", "烟囱式筒形军帽"),
    (r"\bShako\b", "筒形军帽"),
    (r"\bBearskin\b", "近卫熊皮高帽"),
    (r"\bBicorne\b", "双角帽"),
    (r"\bTricorn\b", "三角帽"),
    (r"\bCzapska\b", "恰普卡枪骑兵帽"),
    (r"\bTschapka\b", "恰普卡枪骑兵帽"),
    (r"\bBusby\b", "毛皮骠骑帽"),
    (r"\bMirleton\b", "米勒顿翼帽"),
    (r"\bKasket\b", "普鲁士军盔"),
    (r"\bPickelhaube\b", "尖顶军盔"),
    (r"\bTarleton\b", "塔勒顿骑兵盔"),
    (r"\bHelmet\b", "头盔"),
    (r"\bBonnet\b", "苏格兰软帽"),
    (r"\bCap\b", "便帽"),
    (r"\bHat\b", "帽子"),

    # Uniforms & Clothing
    (r"\bLine Infantry Uniform\b", "线列步兵军服"),
    (r"\bOfficer Uniform\b", "军官制服"),
    (r"\bUniform\b", "军服"),
    (r"\bHabit\b", "线列军大衣"),
    (r"\bDolman\b", "多尔曼军服"),
    (r"\bPelisse\b", "佩利斯毛皮斗篷"),
    (r"\bGreatcoat\b", "防寒军大衣"),
    (r"\bCoat\b", "军大衣"),
    (r"\bJacket\b", "短上衣"),
    (r"\bTunic\b", "礼服上装"),
    (r"\bCuirass\b", "胸甲"),
    (r"\bArmor\b", "护甲"),
    (r"\bVest\b", "背心"),
    (r"\bShirt\b", "衬衣"),
    (r"\bDress\b", "礼服裙"),
    (r"\bTrousers\b", "军裤"),
    (r"\bPants\b", "裤子"),
    (r"\bBreeches\b", "马裤"),
    (r"\bKilt\b", "苏格兰方格裙"),
    (r"\bBoots\b", "军靴"),
    (r"\bShoes\b", "便鞋"),
    (r"\bGloves\b", "手套"),
    (r"\bGauntlets\b", "护手"),
    (r"\bSash\b", "军官饰带"),

    # Mounts
    (r"\bHeavy Cavalry Horse\b", "重骑兵战马"),
    (r"\bLight Cavalry Horse\b", "轻骑兵战马"),
    (r"\bThoroughbred\b", "纯血马"),
    (r"\bCharger\b", "重装战马"),
    (r"\bWarhorse\b", "军马"),
    (r"\bHunter\b", "猎马"),
    (r"\bCourser\b", "轻捷骏马"),
    (r"\bSaddle Horse\b", "旅行乘马"),
    (r"\bSteed\b", "良种战马"),
    (r"\bHorse\b", "战马"),
    (r"\bPony\b", "矮种马"),
    (r"\bSaddle\b", "马鞍"),

    # Field Equipment & Trade Goods
    (r"\bSpyglass\b", "单筒望远镜"),
    (r"\bTelescope\b", "望远镜"),
    (r"\bDrum\b", "军鼓"),
    (r"\bFlute\b", "军笛"),
    (r"\bBanner\b", "军旗"),
    (r"\bStandard\b", "军旗"),
    (r"\bFlag\b", "旗帜"),
    (r"\bTent\b", "帐篷"),
    (r"\bTools\b", "工兵工具"),
    (r"\bBread\b", "面包"),
    (r"\bGrain\b", "谷物"),
    (r"\bFlour\b", "面粉"),
    (r"\bSmoked Fish\b", "熏鱼"),
    (r"\bFish\b", "鱼肉"),
    (r"\bDried Meat\b", "风干肉"),
    (r"\bMeat\b", "肉食"),
    (r"\bCattle\b", "牛"),
    (r"\bCheese\b", "奶酪"),
    (r"\bButter\b", "黄油"),
    (r"\bWine\b", "葡萄酒"),
    (r"\bAle\b", "啤酒"),
    (r"\bIron\b", "铁矿"),
    (r"\bSalt\b", "食盐"),
    (r"\bVelvet\b", "丝绒"),
    (r"\bSilk\b", "丝绸"),
    (r"\bLinen\b", "亚麻布"),
    (r"\bWool\b", "羊毛"),
    (r"\bCloth\b", "布料"),
    (r"\bLeather\b", "皮革"),
    (r"\bFurs\b", "毛皮"),
    (r"\bOil\b", "清油"),
    (r"\bPottery\b", "陶器"),
    (r"\bSpice\b", "香料"),
    (r"\bSugar\b", "蔗糖"),

    # National & Quality Modifiers
    (r"\bFrench\b", "法式"),
    (r"\bBritish\b", "英式"),
    (r"\bPrussian\b", "普鲁士式"),
    (r"\bAustrian\b", "奥地利式"),
    (r"\bRussian\b", "俄式"),
    (r"\bDutch\b", "荷式"),
    (r"\bBelgian\b", "比利时式"),
    (r"\bBrunswick\b", "布伦瑞克式"),
    (r"\bBavarian\b", "巴伐利亚式"),
    (r"\bHanoverian\b", "汉诺威式"),
    (r"\bHighland\b", "高地式"),
    (r"\bGuard\b", "近卫"),
    (r"\bElite\b", "精锐"),
    (r"\bHeavy\b", "重型"),
    (r"\bLight\b", "轻型"),
    (r"\bFine\b", "精致"),
    (r"\bMasterwork\b", "大师级"),
    (r"\bLordly\b", "极品"),
    (r"\bBlack\b", "黑色"),
    (r"\bWhite\b", "白色"),
    (r"\bRed\b", "红色"),
    (r"\bBlue\b", "蓝色"),
    (r"\bGreen\b", "绿色"),
    (r"\bGrey\b", "灰色"),
    (r"\bBrown\b", "棕色")
]

def clean_item_name(s):
    s = s.replace("_", " ")
    for pattern, rep in item_terms:
        s = re.sub(pattern, rep, s, flags=re.IGNORECASE)
    s = re.sub(r' +', ' ', s).strip()
    return s

items_out = []
with open("item_kinds1.txt", encoding="latin-1") as f:
    for line in f:
        line_s = line.strip()
        if line_s.startswith("itm_"):
            parts = line_s.split()
            iid = parts[0]
            name = parts[1] if len(parts) > 1 else iid
            c_name = clean_item_name(name)
            items_out.append((iid, to_cns(c_name)))
            items_out.append((f"{iid}_pl", to_cns(c_name)))

with open(f"{out_dir}/item_kinds.csv", "w", encoding="utf-8-sig", newline="\r\n") as f:
    for iid, s in items_out:
        f.write(f"{iid}|{s}\r\n")

print(f"Written {len(items_out)} item string entries to {out_dir}/item_kinds.csv")
print("All packs successfully compiled!")
