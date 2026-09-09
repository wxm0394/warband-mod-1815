import re
import os

# Helper to format string for Warband CNS font (each Chinese char separated by space)
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

# ==========================================
# 1. FACTIONS.CSV
# ==========================================
print("Generating factions.csv...")
factions_data = [
    ("fac_no_faction", "无阵营"),
    ("fac_commoners", "平民百姓"),
    ("fac_outlaws", "不法之徒"),
    ("fac_neutral", "中立地区"),
    ("fac_innocents", "平民无辜者"),
    ("fac_merchants", "商会行会"),
    ("fac_dark_knights", "黑骑士团"),
    ("fac_black_khergits", "黑库吉特"),
    ("fac_culture_1", "法兰西文化"),
    ("fac_culture_2", "普鲁士文化"),
    ("fac_culture_3", "大不列颠文化"),
    ("fac_culture_4", "荷兰文化"),
    ("fac_culture_5", "德意志文化"),
    ("fac_culture_6", "奥地利文化"),
    ("fac_culture_7", "通用欧陆文化"),
    ("fac_player_faction", "玩家军团"),
    ("fac_player_supporters_faction", "同盟复国军"),
    ("fac_kingdom_1", "法兰西第一帝国"),
    ("fac_kingdom_2", "普鲁士王国"),
    ("fac_kingdom_3", "大不列颠联合王国"),
    ("fac_kingdom_4", "尼德兰联合王国"),
    ("fac_kingdom_5", "德意志同盟"),
    ("fac_kingdom_6", "哈布斯堡帝国"),
    ("fac_kingdoms_end", "各大王国疆界"),
    ("fac_robber_knights", "强盗匪帮"),
    ("fac_khergits", "异邦骑兵"),
    ("fac_manhunters", "赏金猎人"),
    ("fac_deserters", "战场逃兵"),
    ("fac_mountain_bandits", "山区土匪"),
    ("fac_forest_bandits", "绿林劫匪"),
    ("fac_undeads", "亡灵怪客"),
    ("fac_slavers", "人贩武装"),
    ("fac_peasant_rebels", "农民起义军"),
    ("fac_noble_refugees", "流亡贵族")
]

with open(f"{out_dir}/factions.csv", "w", encoding="utf-8-sig", newline="\r\n") as f:
    for fid, name in factions_data:
        f.write(f"{fid}|{to_cns(name)}\r\n")

# ==========================================
# 2. PARTIES.CSV
# ==========================================
print("Generating parties.csv...")
town_names = {
    "p_town_1": "里尔",
    "p_town_2": "布鲁塞尔",
    "p_town_3": "卡塞尔",
    "p_town_4": "弗勒尔拜",
    "p_town_5": "阿贝勒",
    "p_town_6": "伯津",
    "p_town_7": "圣让",
    "p_town_8": "基勒姆",
    "p_town_9": "瓦雷姆",
    "p_town_10": "佩泽尔霍克",
    "p_town_11": "考滕",
    "p_town_12": "洛维",
    "p_town_13": "加尔格",
    "p_town_14": "孔特",
    "p_town_15": "卡斯特",
    "p_town_16": "库特霍夫",
    "p_town_17": "多津厄姆",
    "p_town_18": "佩泽尔霍克北",
    "p_town_19": "卢森堡",
    "p_town_20": "特里尔",
    "p_town_21": "科布伦茨",
    "p_town_22": "美因茨"
}

castle_names = {
    "p_castle_1": "安特卫普要塞", "p_castle_2": "哈瑟尔特城堡", "p_castle_3": "列日要塞",
    "p_castle_4": "那慕尔城堡", "p_castle_5": "沙勒罗瓦要塞", "p_castle_6": "蒙斯城堡",
    "p_castle_7": "布鲁日城堡", "p_castle_8": "蒂尔特要塞", "p_castle_9": "科特赖克城堡",
    "p_castle_10": "奥斯滕德海防要塞", "p_castle_11": "泽布吕赫港口要塞", "p_castle_12": "根特城堡",
    "p_castle_13": "安特卫普防线", "p_castle_14": "哈瑟尔特前哨", "p_castle_15": "敦刻尔克要塞",
    "p_castle_16": "亚泽布鲁克要塞", "p_castle_17": "阿尔芒蒂耶尔要塞", "p_castle_18": "奥布尔丹城堡",
    "p_castle_19": "埃姆要塞", "p_castle_20": "鲁贝城堡", "p_castle_21": "瓦朗谢讷要塞",
    "p_castle_22": "康布雷城堡", "p_castle_23": "科德里要塞", "p_castle_24": "富尔米城堡",
    "p_castle_25": "德南要塞", "p_castle_26": "格拉夫林要塞", "p_castle_27": "莫伯日要塞",
    "p_castle_28": "科德里防线", "p_castle_29": "杜埃城堡", "p_castle_30": "梅赫伦城堡",
    "p_castle_31": "尼韦勒要塞", "p_castle_32": "鲁汶要塞", "p_castle_33": "蒂伦豪特城堡",
    "p_castle_34": "奥德纳尔德要塞", "p_castle_35": "登德尔蒙德城堡", "p_castle_36": "利尔城堡",
    "p_castle_37": "瓦勒海姆要塞", "p_castle_38": "苏瓦尼城堡", "p_castle_39": "尼韦勒前哨",
    "p_castle_40": "阿特要塞", "p_castle_41": "穆斯克龙城堡", "p_castle_42": "卡尔万城堡",
    "p_castle_43": "阿拉斯要塞", "p_castle_44": "弗尔讷城堡", "p_castle_45": "布兰肯贝赫城堡",
    "p_castle_46": "洛克伦要塞", "p_castle_47": "泰姆瑟城堡", "p_castle_48": "鲁瑟拉勒要塞"
}

parties_dict = {}
with open("parties.txt", encoding="latin-1") as f:
    for line in f:
        p = line.split()
        if len(p) > 4 and p[3].startswith("p_"):
            pid = p[3]
            pname = p[4]
            parties_dict[pid] = pname

with open(f"{out_dir}/parties.csv", "w", encoding="utf-8-sig", newline="\r\n") as f:
    f.write("p_main_party|玩 家 军 团\r\n")
    f.write("p_temp_party|军 队\r\n")
    f.write("p_camp_bandits|强 盗 营 地\r\n")
    
    for pid, raw_name in sorted(parties_dict.items()):
        clean_name = raw_name.replace("_", " ")
        if pid in town_names:
            cn_name = town_names[pid]
        elif pid in castle_names:
            cn_name = castle_names[pid]
        else:
            if "Hougoumont" in clean_name:
                cn_name = "乌古蒙庄园"
            elif "Haye" in clean_name:
                cn_name = "拉艾圣农庄"
            elif "Waterloo" in clean_name:
                cn_name = "滑铁卢"
            elif pid.startswith("p_village_"):
                cn_name = clean_name + "村"
            else:
                cn_name = clean_name
        
        f.write(f"{pid}|{to_cns(cn_name)}\r\n")

# ==========================================
# 3. GAME_MENUS.CSV
# ==========================================
print("Updating game_menus.csv...")
existing_menus = {}
if os.path.exists(f"{out_dir}/game_menus.csv"):
    with open(f"{out_dir}/game_menus.csv", encoding="utf-8-sig", errors="ignore") as f:
        for line in f:
            if "|" in line:
                k, v = line.strip().split("|", 1)
                existing_menus[k] = v

existing_menus["mno_dev_jump"] = to_cns("DEV JUMP: 快速进入沙盒（跳过身世直接进大地图）")
existing_menus["mno_dev_jump_map"] = to_cns("DEV JUMP: 传送到大地图")

with open(f"{out_dir}/game_menus.csv", "w", encoding="utf-8-sig", newline="\r\n") as f:
    for k, v in existing_menus.items():
        f.write(f"{k}|{v}\r\n")

print("Generated core factions, parties, and menus in CNS format.")
