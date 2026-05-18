"""Download official Factorio icons from wiki.factorio.com using Python urllib."""
import os, urllib.request, time, csv

# All icons needed by the site
ICONS = {
    # Science packs
    'automation_science': 'Automation_science_pack',
    'logistic_science': 'Logistic_science_pack',
    'military_science': 'Military_science_pack',
    'chemical_science': 'Chemical_science_pack',
    'production_science': 'Production_science_pack',
    'utility_science': 'Utility_science_pack',
    'space_science': 'Space_science_pack',
    # Ores & Basic materials
    'iron_ore': 'Iron_ore',
    'copper_ore': 'Copper_ore',
    'coal': 'Coal',
    'stone': 'Stone',
    'uranium_ore': 'Uranium_ore',
    'crude_oil': 'Crude_oil',
    'water': 'Water',
    # Plates & basic products
    'iron_plate': 'Iron_plate',
    'copper_plate': 'Copper_plate',
    'steel_plate': 'Steel_plate',
    'stone_brick': 'Stone_brick',
    'copper_cable': 'Copper_cable',
    'iron_gear': 'Iron_gear_wheel',
    'plastic_bar': 'Plastic_bar',
    'sulfur': 'Sulfur',
    'solid_fuel': 'Solid_fuel',
    'empty_barrel': 'Empty_barrel',
    # Circuits
    'circuit_red': 'Electronic_circuit',
    'circuit_green': 'Advanced_circuit',
    'circuit_blue': 'Processing_unit',
    # Modules
    'speed_module_1': 'Speed_module_1',
    'speed_module_2': 'Speed_module_2',
    'speed_module_3': 'Speed_module_3',
    'productivity_module_1': 'Productivity_module_1',
    'productivity_module_2': 'Productivity_module_2',
    'productivity_module_3': 'Productivity_module_3',
    'beacon': 'Beacon',
    # Machines
    'stone_furnace': 'Stone_furnace',
    'steel_furnace': 'Steel_furnace',
    'electric_furnace': 'Electric_furnace',
    'boiler': 'Boiler',
    'steam_engine': 'Steam_engine',
    'steam_turbine': 'Steam_turbine',
    'assembling_machine_1': 'Assembling_machine_1',
    'assembling_machine_2': 'Assembling_machine_2',
    'assembling_machine_3': 'Assembling_machine_3',
    'chemical_plant': 'Chemical_plant',
    'oil_refinery': 'Oil_refinery',
    'pumpjack': 'Pumpjack',
    'offshore_pump': 'Offshore_pump',
    'centrifuge': 'Centrifuge',
    'nuclear_reactor': 'Nuclear_reactor',
    'heat_exchanger': 'Heat_exchanger',
    'solar_panel': 'Solar_panel',
    # Logistics
    'transport_belt': 'Transport_belt',
    'fast_transport_belt': 'Fast_transport_belt',
    'inserter': 'Inserter',
    'long_inserter': 'Long_inserter',
    'pipe': 'Pipe',
    'rail': 'Rail',
    'rail_signal': 'Rail_signal',
    'train_stop': 'Train_stop',
    'roboport': 'Roboport',
    'construction_robot': 'Construction_robot',
    'logistic_robot': 'Logistic_robot',
    'battery': 'Battery',
    # Defense
    'gun_turret': 'Gun_turret',
    'laser_turret': 'Laser_turret',
    'flamethrower_turret': 'Flamethrower_turret',
    'stone_wall': 'Stone_wall',
    'land_mine': 'Land_mine',
    # Ammo
    'piercing_rounds': 'Piercing_rounds_magazine',
    'explosives': 'Explosives',
    # Fluids
    'heavy_oil': 'Heavy_oil',
    'light_oil': 'Light_oil',
    'petroleum_gas': 'Petroleum_gas',
    'lubricant': 'Lubricant',
    # Nuclear
    'uranium': 'Uranium_ore',
    'uranium_235': 'Uranium-235',
    'uranium_238': 'Uranium-238',
    'uranium_fuel_cell': 'Uranium_fuel_cell',
    # Misc
    'engine_unit': 'Engine_unit',
    'electric_engine': 'Electric_engine_unit',
    'accumulator': 'Accumulator',
    # Fluids for pipe network
}

OUT_DIR = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\icon'

def try_download(name, wiki_name, size=64):
    """Try to download from wiki.factorio.com with fallback sources."""
    urls = [
        f'https://wiki.factorio.com/images/thumb/{wiki_name}.png/{size}px-{wiki_name}.png',
        f'https://wiki.factorio.com/images/{wiki_name}.png',
        f'https://raw.githubusercontent.com/wube/factorio-data/master/base/graphics/icons/{wiki_name.replace("_","-").lower()}.png',
    ]
    
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                if len(data) > 200:  # Real icon should be > 200 bytes
                    path = os.path.join(OUT_DIR, f'{name}.png')
                    with open(path, 'wb') as f:
                        f.write(data)
                    return len(data)
        except Exception:
            continue
    return 0

print('Downloading official Factorio icons...')
print('=' * 60)

success = 0
fail = 0
for name, wiki_name in ICONS.items():
    size = try_download(name, wiki_name)
    if size > 0:
        status = '✅'
        success += 1
    else:
        status = '❌'
        fail += 1
    if size > 0:
        print(f'  OK {name:30s} -> {size:>5}B')
    else:
        print(f'  -- {name:30s} FAILED')

print(f'\nResult: {success} success, {fail} failed')
