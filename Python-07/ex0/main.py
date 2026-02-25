from .CreatureCard import CreatureCard


def main() -> None:
    """Main function to test card system."""
    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    # Create test cards
    card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    enemy_card = CreatureCard("Goblin Warrior", 1, "Common", 2, 3)

    available_mana = 6

    info = card.get_card_info()

    print(f"CreatureCard Info:\n{info}\n")

    info["available_mana"] = available_mana

    # Test playing the card
    playable = card.is_playable(available_mana)
    if playable:
        print(
            f"Playing {card.name} with "
            f"{available_mana} mana available:"
        )
        play_res = card.play(info)
        print(f"Playable: {playable}")
        print(f"Play result: {play_res}\n")
    else:
        print("Playable: False")

    # Test attacking
    attack_res = card.attack_target(enemy_card)

    print(f"Attack result: {attack_res}")

    # Test insufficient mana scenario
    print("\nTesting insufficient mana (3 available):")
    available_mana = 3
    playable = card.is_playable(available_mana)

    if playable:
        play_res = card.play(info)
        print(f"Playable: {playable}")
        print(f"Play result: {play_res}")
    else:
        print("Playable: False")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
