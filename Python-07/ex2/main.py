from ex2.EliteCard import EliteCard


# Simple dummy target class
class DummyTarget:
    def __init__(self, name, health):
        self.name = name
        self.health = health


def main():
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):\n")

    # Create EliteCard
    elite = EliteCard(
        name="Arcane Warrior",
        cost=4,
        rarity="Legendary",
        health=10,
        damage=5,
        defen=3,
        combat_type="melee",
        mana=8
    )

    print("Combat phase:")

    # Create enemy
    enemy = DummyTarget("Enemy", 10)

    attack_result = elite.attack(enemy)
    print(f"Attack result: {attack_result}")

    defense_result = elite.defend(5)  # 5 incoming damage
    print(f"Defense result: {defense_result}")

    print("\nMagic phase:")

    enemy1 = DummyTarget("Enemy1", 10)
    enemy2 = DummyTarget("Enemy2", 10)

    spell_result = elite.cast_spell("Fireball", [enemy1, enemy2])
    print(f"Spell cast: {spell_result}")

    mana_result = elite.channel_mana(3)
    print(f"Mana channel: {mana_result}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()