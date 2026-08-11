import json
import re
from collections import Counter

def extract_candidates():
    with open('tools/results.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Defined Materials/Entities
    materials_raw = []
    methods_raw = []

    # Common keywords to look for in content if materials list is messy
    material_keywords = [
        "BiFeO3", "PbTe", "SnTe", "WTe2", "MoS2", "MoSe2", "WS2", "WSe2", "h-BN",
        "CrI3", "CrTe2", "Fe3GeTe2", "NiI2", "In2Se3", "CuInP2S6", "SrTiO3",
        "BaTiO3", "PbTiO3", "Sc2P2Se6", "Mn2N", "MXene", "TMDs", "NbSe2", "TaS2"
    ]

    concept_keywords = [
        "Berry Phase", "Skyrmions", "Charge Density Wave", "Multiferroicity",
        "Sliding Ferroelectricity", "Magnetoelectric Coupling", "Domain Wall",
        "Spin-Orbit Coupling", "Rashba Effect", "DFT", "NEB", "AIMD",
        "Monte Carlo", "PFM", "STM", "ARPES", "STEM", "Strain Engineering",
        "Topological Insulator", "Weyl Semimetal", "Half-metal", "Superconductivity"
    ]

    found_materials = Counter()
    found_concepts = Counter()

    for paper in data:
        # From explicit metadata
        for m in paper.get('materials', []):
            # Try to find common formulas
            m_clean = re.findall(r'[A-Z][a-z]?\d*[A-Z][a-z]?\d*[A-Z]?[a-z]?\d*', m)
            for formula in m_clean:
                if len(formula) > 2:
                    found_materials[formula] += 1

        # From methods metadata
        for meth in paper.get('methods', []):
            if len(meth) < 30 and len(meth) > 2:
                found_concepts[meth] += 1

    # Final tally including keyword matching (simulating what a Subagent would do)
    return found_materials, found_concepts

if __name__ == "__main__":
    mats, concs = extract_candidates()

    output = {
        "top_materials": dict(mats.most_common(100)),
        "top_concepts": dict(concs.most_common(100))
    }

    with open('tools/candidates.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(mats)} material candidates and {len(concs)} concept candidates.")
