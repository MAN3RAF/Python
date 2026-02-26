
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_list = sorted(artifacts, key=lambda artifact: artifact['power'], reverse=True)
    return sorted_list

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_list = list(filter(lambda mage: mage['power'] >= min_power, mages))
    return filtered_list

def spell_transformer(spells: list[str]) -> list[str]:
    transformed_list = list(map(lambda spell: "* " + spell + " *", spells))
    return transformed_list

def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage['power'])['power']
    min_power = min(mages, key=lambda mage: mage['power'])['power']
    total_power = sum(map(lambda mage: mage['power'], mages))
    avr_power = round(total_power / len(mages), 2)
    return {'max_power': max_power, 'min_power': min_power, 'avg_power': avr_power}

def main():
    print("\nTesting artifact sorter...")

    sorted_artifact = artifact_sorter(
        [
            {'name': "Fire Staff", 'power': 92, 'type': "Staff"},
            {'name': "Crystal Orb", 'power': 85, 'type': "Orb"},     
        ]
    )
    print(
        f"{sorted_artifact[0]['name']} ({sorted_artifact[0]['power']}) comes "
        f"before {sorted_artifact[1]['name']} ({sorted_artifact[1]['power']}"
        ")"
    )

    print("\nTesting spell transformer...")

    transformed_spells = spell_transformer(["fireball", "heal", "shield"])

    for spell in transformed_spells:
        print(spell, end=' ')


if __name__ == "__main__":
    main()
