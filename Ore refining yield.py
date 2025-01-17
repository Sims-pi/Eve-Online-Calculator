import math
ores = {
    'Veldspar': {'Tritanium': 400},
    'Stable Veldspar': {'Tritanium': 460},
    'Dense Veldspar': {'Tritanium': 440},
    'Concentrated Veldspar': {'Tritanium': 420},
    'Scordite': {'Tritanium': 150, 'Pyerite': 90},
    'Massive Scordite': {'Tritanium': 165, 'Pyerite': 99},
    'Condensed Scordite': {'Tritanium': 158, 'Pyerite': 95},
    'Glossy Scordite': {'Tritanium': 173, 'Pyerite': 104},
    'Pyroxeres': {'Pyerite': 90, 'Mexallon': 30},
    'Solid Pyroxeres': {'Pyerite': 95, 'Mexallon': 32},
    'Viscous Pyroxeres': {'Pyerite': 99, 'Mexallon': 33},
    'Opulent Pyroxeres': {'Pyerite': 104, 'Mexallon': 35},
    'Plagioclase': {'Tritanium': 175, 'Mexallon': 70},
    'Rich Plagioclase': {'Tritanium': 193, 'Mexallon': 77},
    'Azure Plagioclase': {'Tritanium': 184, 'Mexallon': 74},
    'Sparkling Plagioclase': {'Tritanium': 201, 'Mexallon': 81},
    'Arkonor': {'Pyerite': 3200, 'Mexallon': 1200, 'Megacyte': 120},
    'Prime Arkonor': {'Pyerite': 3520, 'Mexallon': 1320, 'Megacyte': 132},
    'Flawless Arkonor': {'Pyerite': 3680, 'Mexallon': 1380, 'Megacyte': 138},
    'Crimson Arkonor': {'Pyerite': 3360, 'Mexallon': 1260, 'Megacyte': 126},
    'Bezdnacine': {'Tritanium': 40000, 'Isogen': 4800, 'Morphite': 128},
    'Hadal Bezdnacine': {'Tritanium': 44000, 'Isogen': 5280, 'Morphite': 141},
    'Abyssal Bezdnacine': {'Tritanium': 42000, 'Isogen': 5040, 'Morphite': 134},
    'Bistot': {'Pyerite': 3200, 'Mexallon': 1200, 'Zydrine': 160},
    'Triclinic Bistot': {'Pyerite': 3360, 'Mexallon': 1260, 'Zydrine': 168},
    'Monoclinic Bistot': {'Pyerite': 3520, 'Mexallon': 1320, 'Zydrine': 176},
    'Cubic Bistot': {'Pyerite': 3680, 'Mexallon': 1380, 'Zydrine': 184},
    'Crokite': {'Tritanium': 800, 'Pyerite': 2000, 'Nocxium': 800},
    'Crystalline Crokite': {'Tritanium': 880, 'Pyerite': 2200, 'Nocxium': 880},
    'Pellucid Crokite': {'Tritanium': 920, 'Pyerite': 2300, 'Nocxium': 920},
    'Sharp Crokite': {'Tritanium': 840, 'Pyerite': 2100, 'Nocxium': 840},
    'Dark Ochre': {'Mexallon': 1360, 'Isogen': 1200, 'Nocxium': 320},
    'Jet Ochre': {'Mexallon': 1564, 'Isogen': 1380, 'Nocxium': 368},
    'Obsidian Ochre': {'Mexallon': 1496, 'Isogen': 1320, 'Nocxium': 352},
    'Onyx Ochre': {'Mexallon': 1428, 'Isogen': 1260, 'Nocxium': 336},
    'Duninium': {'Morphite': 170},
    'Imperial Duninium': {'Morphite': 196},
    'Noble Duninium': {'Morphite': 179},
    'Royal Duninium': {'Morphite': 187},
    'Eifyrium': {'Zydrine': 266},
    'Augmented Eifyrium': {'Zydrine': 306},
    'Doped Eifyrium': {'Zydrine': 279},
    'Boosted Eifyrium': {'Zydrine': 293},
    'Gneiss': {'Pyerite': 2000, 'Mexallon': 1500, 'Isogen': 800},
    'Iridescent Gneiss': {'Pyerite': 2100, 'Mexallon': 1575, 'Isogen': 840},
    'Prismatic Gneiss': {'Pyerite': 2200, 'Mexallon': 1650, 'Isogen': 880},
    'Brilliant Gneiss': {'Pyerite': 2300, 'Mexallon': 1725, 'Isogen': 920},
    'Griemeer': {'Tritanium': 250, 'Isogen': 80},
    'Inky Griemeer': {'Tritanium': 275, 'Isogen': 88},
    'Opaque Griemeer': {'Tritanium': 288, 'Isogen': 92},
    'Clear Griemeer': {'Tritanium': 263, 'Isogen': 84},
    'Hedbergite': {'Pyerite': 450, 'Isogen': 120, 'Zydrine': 150},
    'Glazed Hedbergite': {'Pyerite': 495, 'Isogen': 132, 'Zydrine': 165},
    'Lustrous Hedbergite': {'Pyerite': 518, 'Isogen': 138, 'Zydrine': 173},
    'Vitric Hedbergite': {'Pyerite': 473, 'Isogen': 126, 'Zydrine': 158},
    'Hemorphite': {'Isogen': 240, 'Nocxium': 90},
    'Radiant Hemorphite': {'Isogen': 264, 'Nocxium': 99},
    'Scintillating Hemorphite': {'Isogen': 276, 'Nocxium': 104},
    'Vivid Hemorphite': {'Isogen': 252, 'Nocxium': 95},
    'Hezorime': {'Pyerite': 2000, 'Zydrine': 120, 'Morphite': 60},
    'Dull Hezorime': {'Pyerite': 2100, 'Zydrine': 126, 'Morphite': 63},
    'Serrated Hezorime': {'Pyerite': 2200, 'Zydrine': 132, 'Morphite': 66},
    'Sharp Hezorime': {'Pyerite': 2300, 'Zydrine': 138, 'Morphite': 69},
    'Jaspet': {'Mexallon': 150, 'Nocxium': 50},
    'Immaculate Jaspet': {'Mexallon': 173, 'Nocxium': 58},
    'Pristine Jaspet': {'Mexallon': 165, 'Nocxium': 55},
    'Pure Jaspet': {'Mexallon': 158, 'Nocxium': 53},
    'Kernit': {'Isogen': 60, 'Nocxium': 120},
    'Fiery Kernit': {'Isogen': 66, 'Nocxium': 132},
    'Luminous Kernit': {'Isogen': 63, 'Nocxium': 126},
    'Resplendant Kernit': {'Isogen': 69, 'Nocxium': 138},
    'Kylixium': {'Tritanium': 300, 'Pyerite': 200, 'Mexallon': 550},
    'Kaolin Kylixium': {'Tritanium': 315, 'Pyerite': 210, 'Mexallon': 578},
    'Argil Kylixium': {'Tritanium': 330, 'Pyerite': 220, 'Mexallon': 605},
    'Adobe Kylixium': {'Tritanium': 345, 'Pyerite': 230, 'Mexallon': 633},
    'Mercoxit': {'Morphite': 140},
    'Magma Mercoxit': {'Morphite': 147},
    'Vitreous Mercoxit': {'Morphite': 154},
    'Mordunium': {'Pyerite': 80},
    'Plum Mordunium': {'Pyerite': 84},
    'Plunder Mordunium': {'Pyerite': 92},
    'Prize Mordunium': {'Pyerite': 88},
    'Nocxite': {'Tritanium': 900, 'Pyerite': 150, 'Nocxium': 105},
    'Intoxicating Nocxite': {'Tritanium': 990, 'Pyerite': 165, 'Nocxium': 116},
    'Fragrant Nocxite': {'Tritanium': 945, 'Pyerite': 158, 'Nocxium': 111},
    'Ambrosial Nocxite': {'Tritanium': 1035, 'Pyerite': 173, 'Nocxium': 121},
    'Omber': {'Pyerite': 90, 'Mexallon': 75},
    'Golden Omber': {'Pyerite': 99, 'Mexallon': 83},
    'Platinoid Omber': {'Pyerite': 104, 'Mexallon': 86},
    'Silvery Omber': {'Pyerite': 95, 'Mexallon': 79},
    'Rakovene': {'Tritanium': 40000, 'Pyerite': 3200, 'Isogen': 200},
    'Nesosilicate Rakovene': {'Pyerite': 1500, 'Isogen': 120, 'Morphite': 7, 'Neo-Jadarite': 65},
    'Hadal Rakovene': {'Tritanium': 44000, 'Pyerite': 3520, 'Isogen': 220},
    'Abyssal Rakovene': {'Tritanium': 42000, 'Pyerite': 3360, 'Isogen': 210},
    'Spodumain': {'Tritanium': 48000, 'Isogen': 1000, 'Zydrine': 160, 'Megacyte': 80, 'Morphite': 40},
    'Gleaming Spodumain': {'Tritanium': 52800, 'Isogen': 1100, 'Zydrine': 176, 'Megacyte': 88, 'Morphite': 44},
    'Dazzling Spodumain': {'Tritanium': 55200, 'Isogen': 1150, 'Zydrine': 184, 'Megacyte': 92, 'Morphite': 46},
    'Bright Spodumain': {'Tritanium': 50400, 'Isogen': 1050, 'Zydrine': 168, 'Megacyte': 84, 'Morphite': 42},
    'Talassonite': {'Tritanium': 40000, 'Megacyte': 960, 'Morphite': 32},
    'Hadal Talassonite': {'Tritanium': 44000, 'Megacyte': 1056, 'Morphite': 35},
    'Abyssal Talassonite': {'Tritanium': 42000, 'Megacyte': 1008, 'Morphite': 34},
    'Ueganite': {'Pyerite': 800, 'Morphite': 40},
    'Stormy Ueganite': {'Pyerite': 920, 'Morphite': 46},
    'Overcast Ueganite': {'Pyerite': 880, 'Morphite': 44},
    'Foggy Ueganite': {'Pyerite': 840, 'Morphite': 42},
    'Ytrium': {'Isogen': 240},
    'Moonshine Ytrium': {'Isogen': 276},
    'Firewater Ytrium': {'Isogen': 264},
    'Bootleg Ytrium': {'Isogen': 252}
}

while True:
    ore_name = input('Ore type (or "exit" to quit): ').strip().title()
    if ore_name.lower() == 'exit':
        break
    ore_amount = float(input('Amount: '))
    percent_yield = float(input('Percent yield: ')) / 100

    if ore_name in ores:
        ore_minerals = ores[ore_name]
        for mineral, quantity in ore_minerals.items():
            yield_amount = math.floor(ore_amount * quantity * percent_yield / 100)
            print(f'{mineral}: {yield_amount}')
    else:
        print('Ore type not found.')