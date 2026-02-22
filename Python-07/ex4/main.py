from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")
    print()

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")

    dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        power=8,
        toughness=6,
        base_rating=1200
    )

    wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity="Rare",
        power=6,
        toughness=5,
        base_rating=1150
    )

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.calculate_rating()}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")
    print()

    print(f"{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.calculate_rating()}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")
    print()

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")
    print()

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, 1):
        record = entry['record']
        rating = entry['rating']
        print(f"{i}. {entry['name']} - Rating: {rating} ({record})")
    print()

    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(report)
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
