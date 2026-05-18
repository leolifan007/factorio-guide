#!/usr/bin/env python3
"""下载 Factorio Wiki 真实游戏图标到 static/images/icon/"""

import os
import sys
import urllib.request
import time

ICON_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "static", "images", "icon"
)

# 文件名→Factorio Wiki 页面名映射
ICON_MAP = {
    # 基础材料
    "iron_ore":         "Iron_ore",
    "iron_plate":       "Iron_plate",
    "copper_ore":       "Copper_ore",
    "copper_plate":     "Copper_plate",
    "copper_cable":     "Copper_cable",
    "iron_gear":        "Iron_gear_wheel",
    "steel_plate":      "Steel_plate",
    "stone":            "Stone",
    "stone_brick":      "Stone_brick",
    "coal":             "Coal",
    "sulfur":           "Sulfur",
    "plastic_bar":      "Plastic_bar",
    "water":            "Water",
    "petroleum_gas":    "Petroleum_gas",
    "light_oil":        "Light_oil",
    "heavy_oil":        "Heavy_oil",
    "lubricant":        "Lubricant",
    "crude_oil":        "Crude_oil",
    "uranium_ore":      "Uranium_ore",
    "uranium_235":      "Uranium-235",
    "uranium_238":      "Uranium-238",
    "empty_barrel":     "Barrel",

    # 中间产物
    "circuit_green":    "Electronic_circuit",
    "circuit_red":      "Advanced_circuit",
    "circuit_blue":     "Processing_unit",
    "engine_unit":      "Engine_unit",
    "electric_engine":  "Electric_engine_unit",
    "battery":          "Battery",
    "solid_fuel":       "Solid_fuel",
    "explosives":       "Explosives",
    "pipe":             "Pipe",
    "piercing_rounds":  "Piercing_rounds_magazine",

    # 传送/物流
    "transport_belt":   "Transport_belt",
    "fast_transport_belt": "Fast_transport_belt",
    "inserter":         "Inserter",
    "long_inserter":    "Long-handed_inserter",

    # 科技包
    "automation_science":  "Automation_science_pack",
    "logistic_science":    "Logistic_science_pack",
    "chemical_science":    "Chemical_science_pack",
    "military_science":    "Military_science_pack",
    "utility_science":     "Utility_science_pack",
    "space_science":       "Space_science_pack",

    # 电力
    "steam_turbine":    "Steam_turbine",
    "heat_exchanger":   "Heat_exchanger",
    "nuclear_reactor":  "Nuclear_reactor",
    "solar_panel":      "Solar_panel",
    "accumulator":      "Accumulator",
    "boiler":           "Boiler",
    "steam_engine":     "Steam_engine",

    # 生产设备
    "oil_refinery":     "Oil_refinery",
    "chemical_plant":   "Chemical_plant",
    "assembling_machine_1": "Assembling_machine_1",
    "assembling_machine_2": "Assembling_machine_2",
    "assembling_machine_3": "Assembling_machine_3",
    "electric_furnace": "Electric_furnace",
    "stone_furnace":    "Stone_furnace",
    "steel_furnace":    "Steel_furnace",
    "pumpjack":         "Pumpjack",
    "offshore_pump":    "Offshore_pump",
    "centrifuge":       "Centrifuge",

    # 防御
    "flamethrower_turret":  "Flamethrower_turret",
    "gun_turret":           "Gun_turret",
    "laser_turret":         "Laser_turret",
    "stone_wall":           "Wall",
    "land_mine":            "Land_mine",

    # 火车/机器人
    "rail":             "Straight_rail",
    "train_stop":       "Train_stop",
    "rail_signal":      "Rail_signal",
    "roboport":         "Roboport",
    "logistic_robot":   "Logistic_robot",
    "construction_robot": "Construction_robot",

    # 其他
    "beacon":           "Beacon",
    "speed_module_1":   "Speed_module",
    "speed_module_2":   "Speed_module_2",
    "speed_module_3":   "Speed_module_3",
    "productivity_module_1": "Productivity_module",
    "productivity_module_2": "Productivity_module_2",
    "productivity_module_3": "Productivity_module_3",
    "module":           "Effect_distribution_platform",
    "wall":             "Wall",
}

WIKI_BASE = "https://wiki.factorio.com/images/"

def download_icon(local_name, wiki_name):
    """下载单个图标，返回成功/失败"""
    url = f"{WIKI_BASE}{wiki_name}.png"
    # Wiki 通常把图标放在 images/thumb 目录
    url_thumb = f"{WIKI_BASE}thumb/{wiki_name}.png/64px-{wiki_name}.png"
    
    dest = os.path.join(ICON_DIR, f"{local_name}.png")
    
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        print(f"  ✓ {local_name}.png (已存在, 跳过)")
        return True
    
    for u in [url, url_thumb]:
        try:
            req = urllib.request.Request(u, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            })
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                if len(data) < 500:
                    continue
                with open(dest, "wb") as f:
                    f.write(data)
                print(f"  ✓ {local_name}.png ({len(data)//1024}KB)")
                return True
        except Exception as e:
            continue
    
    print(f"  x {local_name}.png ({wiki_name}) 失败")
    return False

def main():
    os.makedirs(ICON_DIR, exist_ok=True)
    
    print(f"下载 {len(ICON_MAP)} 个图标到 {ICON_DIR}")
    print()
    
    ok = 0
    fail = 0
    
    for local_name, wiki_name in ICON_MAP.items():
        if download_icon(local_name, wiki_name):
            ok += 1
        else:
            fail += 1
        time.sleep(0.3)  # 礼貌间隔
    
    print(f"\n完成: {ok} 成功, {fail} 失败")
    
    # 清理旧的 game-icons 目录
    old_dir = os.path.join(os.path.dirname(ICON_DIR), "game-icons")
    if os.path.isdir(old_dir):
        print(f"\n提示: 旧的 game-icons 目录仍存在 ({old_dir})")
        print("确认图标全部下载成功后，可删除它")

if __name__ == "__main__":
    main()
