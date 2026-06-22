#!/usr/bin/env python3
"""Add natural {{< ref >}} internal links to all article intro paragraphs."""
import os

base = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide"

articles = [
    # (rel_path, search_text, replacement_text_with_ref)
    ("content\\space-age\\aquilo\\aquilo-guide.md",
     "how to survive on Factorio coldest planet.",
     "how to survive on Factorio coldest planet. Check the {{< ref \"/space-age/guide/planet-order-guide\" >}} for when to visit, and {{< ref \"/space-age/platform/space-platform-guide\" >}} for ship design planning."),
    
    ("content\\space-age\\gleba\\bioflux-production.md",
     "keeps bioflux flowing.",
     "keeps bioflux flowing. For a complete Gleba walkthrough, see {{< ref \"/space-age/gleba/gleba-survival-guide\" >}}."),
    
    ("content\\space-age\\gleba\\gleba-survival-guide.md",
     "Here's the build order that prevents that.",
     "Here's the build order that prevents that. Check {{< ref \"/space-age/guide/planet-order-guide\" >}} for route comparison and {{< ref \"/space-age/vulcanus/lava-processing\" >}} for why Vulcanus unlocks foundry tech first."),
    
    ("content\\space-age\\gleba\\pentapod-defense.md",
     "too many pentapods with too much spore pollution.",
     "too many pentapods with too much spore pollution. Pair with {{< ref \"/space-age/gleba/bioflux-production\" >}} to understand the root cause of spore generation."),
    
    ("content\\space-age\\guide\\planet-order-guide.md",
     "Vulcanus vs Fulgora vs Gleba route comparison.",
     "Vulcanus vs Fulgora vs Gleba route comparison. Start with {{< ref \"/space-age/guide/vulcanus-guide\" >}} for the full landing preparation guide."),
    
    ("content\\space-age\\guide\\vulcanus-guide.md",
     "how to exploit the planet's unique resources.",
     "how to exploit the planet's unique resources. Once established, {{< ref \"/space-age/vulcanus/lava-processing\" >}} covers the infinite foundry production chain."),
    
    ("content\\space-age\\fulgora\\fulgora-recycling-guide.md",
     "Fulgora guide for Factorio Space Age. Scrap recycling sorter design, holmium processing, lightning power, and the recycler loop mechanics.",
     'Fulgora guide for Factorio Space Age. Scrap recycling sorter design, holmium processing, lightning power, and the recycler loop mechanics. See {{< ref "/space-age/fulgora/scrap-overflow" >}} for dedicated overflow handling.'),
    
    ("content\\space-age\\fulgora\\fulgora-recycling-guide.md",
     "Description says meta. Need to update description line only.",
     "Fulgora guide for Factorio Space Age. Scrap recycling sorter design, holmium processing, lightning power, and the recycler loop mechanics. See {{< ref \"/space-age/fulgora/scrap-overflow\" >}} for dedicated overflow handling."),
    
    ("content\\space-age\\fulgora\\scrap-overflow.md",
     "plan for everything that could come out.",
     "plan for everything that could come out. Start with {{< ref \"/space-age/fulgora/fulgora-recycling-guide\" >}} for the Fulgora landing setup."),
    
    ("content\\space-age\\quality\\quality-module-guide.md",
     "the definitive quality module strategies for Space Age endgame.",
     "the definitive quality module strategies for Space Age endgame. For the full upcycling loop design, see {{< ref \"/space-age/quality/upcycling-loop\" >}}."),
    
    ("content\\space-age\\quality\\upcycling-loop.md",
     "the optimal module path for Space Age endgame factory.",
     "the optimal module path for Space Age endgame factory. Start with {{< ref \"/space-age/quality/quality-module-guide\" >}} for the fundamentals of quality probability."),
    
    ("content\\space-age\\platform\\ship-design.md",
     "multi-planet ship that won't explode halfway.",
     "multi-planet ship that won't explode halfway. Start with {{< ref \"/space-age/platform/space-platform-guide\" >}} for platform fundamentals."),
    
    ("content\\space-age\\platform\\space-platform-guide.md",
     "Here's the build order that prevents that.",
     "Here's the build order that prevents that. For advanced ship designs, see {{< ref \"/space-age/platform/ship-design\" >}}."),
    
    ("content\\space-age\\platform\\cross-planet-logistics.md",
     "cargo rocket is your supply line.",
     "cargo rocket is your supply line. See {{< ref \"/space-age/guide/planet-order-guide\" >}} for which planet to visit when, and {{< ref \"/space-age/platform/space-platform-guide\" >}} for platform fundamentals."),
    
    ("content\\space-age\\vulcanus\\lava-processing.md",
     "without ever placing a miner.",
     "without ever placing a miner. If you haven't landed yet, {{< ref \"/space-age/guide/vulcanus-guide\" >}} covers the first steps on Vulcanus."),
]

for rel_path, search, replace in articles:
    full_path = os.path.join(base, rel_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search in content:
        new_content = content.replace(search, replace, 1)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"OK {os.path.basename(rel_path)}")
    else:
        # Try fuzzy match
        print(f"MISS {os.path.basename(rel_path)}: '{search[:60]}' not found")
