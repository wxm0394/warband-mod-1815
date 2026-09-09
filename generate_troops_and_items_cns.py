import re
import os

def to_cns(text):
    res = []
    for ch in text:
        if ('\u4e00' <= ch <= '\u9fff') or ('\u3000' <= ch <= '\u303f') or ('\uff00' <= ch <= '\uffef'):
            res.append(ch + ' ')
        else:
            res.append(ch)
    s = "".join(res)
    return re.sub(r' +', ' ', s).strip()

out_dir = "languages/cns"
os.makedirs(out_dir, exist_ok=True)

# Word replacements dictionary for Napoleonic military terms
term_map = [
    ("Old_Guard", "老近卫军"),
    ("Young_Guard", "青年近卫军"),
    ("Middle_Guard", "中坚近卫军"),
    ("Foot_Guard", "近卫步兵"),
    ("Coldstream", "冷溪近卫军"),
    ("Life_Guard", "近卫骑兵"),
    ("Horse_Guard", "近卫骑兵"),
    ("Line_Infantry", "线列步兵"),
    ("Fusilier", "燧发枪兵"),
    ("Grenadier", "掷弹兵"),
    ("Voltigeur", "轻步兵散兵"),
    ("Chasseur", "猎兵"),
    ("Jaeger", "猎兵"),
    ("Jäger", "猎兵"),
    ("Landwehr", "后备民兵"),
    ("Militia", "民兵"),
    ("Grenz", "国境步兵"),
    ("Hussar", "骠骑兵"),
    ("Dragoon", "龙骑兵"),
    ("Cuirassier", "胸甲骑兵"),
    ("Lancer", "枪骑兵"),
    ("Uhlan", "枪骑兵"),
    ("Carabineer", "卡宾枪骑兵"),
    ("Carabinier", "卡宾枪骑兵"),
    ("Cavalry", "骑兵"),
    ("Infantry", "步兵"),
    ("Artillery", "炮兵"),
    ("Officer", "军官"),
    ("Sergeant", "军士"),
    ("Corporal", "下士"),
    ("Captain", "上尉"),
    ("Colonel", "上校"),
    ("General", "将军"),
    ("Marshal", "元帅"),
    ("Duke", "公爵"),
    ("Baron", "男爵"),
    ("Prince", "亲王"),
    ("Drummer", "鼓手"),
    ("Fifer", "笛手"),
    ("Standard_Bearer", "掌旗官"),
    ("Flagbearer", "掌旗官"),
    ("Flagcarrier", "掌旗官"),
    ("Flag_Bearer", "掌旗官"),
    ("King", "国王"),
    ("Emperor", "皇帝"),
    ("Lord", "勋爵"),
    ("Napoleon", "拿破仑"),
    ("Bonaparte", "波拿巴"),
    ("Wellington", "威灵顿公爵"),
    ("Blucher", "布吕歇尔"),
    ("Blücher", "布吕歇尔"),
    ("Ney", "内伊元帅"),
    ("Grouchy", "格鲁希元帅"),
    ("Davout", "达武元帅"),
    ("Soult", "苏尔特元帅"),
    ("Uxbridge", "厄克斯布里奇伯爵"),
    ("Picton", "皮克顿将军"),
    ("Brunswick", "布伦瑞克"),
    ("Schwarzenberg", "施瓦岑贝格亲王"),
    ("Orange", "奥兰治亲王"),
    ("Bavarian", "巴伐利亚"),
    ("Bayerische", "巴伐利亚"),
    ("Hessen", "黑森"),
    ("Austrian", "奥地利"),
    ("Prussian", "普鲁士"),
    ("British", "英国"),
    ("French", "法国"),
    ("Dutch", "荷兰"),
    ("German", "德意志"),
    ("Belgian", "比利时"),
    ("Hanoverian", "汉诺威"),
    ("Hannover", "汉诺威"),
    ("KGL", "英王德意志军团"),
    ("95th", "第95步枪团"),
    ("Black_Watch", "黑卫士兵团"),
    ("Scots_Grey", "苏格兰灰骑兵"),
    ("Highland", "苏格兰高地"),
    ("Veteran", "老练"),
    ("Elite", "精锐"),
    ("Recruit", "新兵"),
    ("Deserter", "逃兵"),
    ("Bandit", "强盗"),
    ("Robber", "土匪")
]

def translate_phrase(text):
    clean = text.replace("_", " ")
    for en, cn in term_map:
        clean_en = en.replace("_", " ")
        if clean_en in clean:
            clean = clean.replace(clean_en, cn)
    return clean

# ==========================================
# 1. TROOPS.CSV
# ==========================================
print("Translating troops.txt to troops.csv...")
troops_out = []

with open("troops.txt", encoding="latin-1") as f:
    for line in f:
        line_s = line.strip()
        if line_s.startswith("trp_"):
            parts = line_s.split()
            tid = parts[0]
            name = parts[1]
            plural = parts[2] if len(parts) > 2 else name
            
            t_name = translate_phrase(name)
            t_plural = translate_phrase(plural)
            
            troops_out.append((tid, to_cns(t_name)))
            troops_out.append((f"{tid}_pl", to_cns(t_plural)))

with open(f"{out_dir}/troops.csv", "w", encoding="utf-8-sig", newline="\r\n") as f:
    for tid, s in troops_out:
        f.write(f"{tid}|{s}\r\n")

print(f"Written {len(troops_out)} troop string entries.")

# ==========================================
# 2. ITEM_KINDS.CSV
# ==========================================
print("Translating item_kinds1.txt to item_kinds.csv...")

item_term_map = [
    ("Musket", "燧发枪"),
    ("Rifle", "步枪"),
    ("Pistol", "手枪"),
    ("Carbine", "卡宾枪"),
    ("Sword", "军剑"),
    ("Sabre", "马刀"),
    ("Saber", "马刀"),
    ("Pallasch", "重骑兵直剑"),
    ("Lance", "骑枪"),
    ("Bayonet", "刺刀"),
    ("Dagger", "匕首"),
    ("Knife", "猎刀"),
    ("Cartridge", "纸包弹药"),
    ("Bullet", "铅弹"),
    ("Cannon", "加农炮"),
    ("Uniform", "军服"),
    ("Coat", "军大衣"),
    ("Tunic", "礼服上装"),
    ("Jacket", "短上衣"),
    ("Dolman", "多尔曼军服"),
    ("Pelisse", "佩利斯斗篷"),
    ("Habit", "线列军大衣"),
    ("Pants", "军裤"),
    ("Trousers", "长裤"),
    ("Breeches", "马裤"),
    ("Boots", "长靴"),
    ("Shoes", "便鞋"),
    ("Shako", "筒形军帽"),
    ("Hat", "军帽"),
    ("Cap", "便帽"),
    ("Bicorne", "双角帽"),
    ("Tricorn", "三角帽"),
    ("Bearskin", "熊皮高帽"),
    ("Helmet", "头盔"),
    ("Cuirass", "胸甲"),
    ("Armor", "护甲"),
    ("Gloves", "手套"),
    ("Gauntlets", "护手"),
    ("Horse", "战马"),
    ("Charger", "重装战马"),
    ("Courser", "轻捷战马"),
    ("Hunter", "轻型军马"),
    ("Pony", "轻马"),
    ("Steed", "良种战马"),
    ("Saddle", "马鞍"),
    ("Banner", "军旗"),
    ("Flag", "旗帜"),
    ("Drum", "军鼓"),
    ("Flute", "军笛"),
    ("Spyglass", "单筒望远镜"),
    ("Telescope", "望远镜"),
    ("Bread", "面包"),
    ("Meat", "熏肉"),
    ("Fish", "鱼肉"),
    ("Wine", "红酒"),
    ("Ale", "麦芽酒"),
    ("Iron", "铁矿石"),
    ("Velvet", "天鹅绒"),
    ("Cloth", "亚麻布匹"),
    ("Tools", "工兵工具"),
    ("French", "法军"),
    ("British", "英军"),
    ("Prussian", "普军"),
    ("Dutch", "荷军"),
    ("Brunswick", "布伦瑞克"),
    ("Austrian", "奥军"),
    ("Russian", "俄军"),
    ("Guard", "近卫"),
    ("Officer", "军官"),
    ("General", "将军"),
    ("Heavy", "重型"),
    ("Light", "轻型"),
    ("Elite", "精锐")
]

def translate_item(raw_name):
    clean = raw_name.replace("_", " ")
    for en, cn in item_term_map:
        clean_en = en.replace("_", " ")
        if clean_en in clean:
            clean = clean.replace(clean_en, cn)
    return clean

items_out = []
with open("item_kinds1.txt", encoding="latin-1") as f:
    for line in f:
        line_s = line.strip()
        if line_s.startswith("itm_"):
            parts = line_s.split()
            iid = parts[0]
            name = parts[1] if len(parts) > 1 else iid
            t_name = translate_item(name)
            items_out.append((iid, to_cns(t_name)))
            items_out.append((f"{iid}_pl", to_cns(t_name)))

with open(f"{out_dir}/item_kinds.csv", "w", encoding="utf-8-sig", newline="\r\n") as f:
    for iid, s in items_out:
        f.write(f"{iid}|{s}\r\n")

print(f"Written {len(items_out)} item string entries.")
print("All localization packs generated successfully!")
