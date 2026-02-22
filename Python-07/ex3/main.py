from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


def main() -> None:
    """Main function to test game engine."""
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    # Configure the engine with factory and strategy
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")

    # Simulate turn using engine (which uses factory to create cards)
    actions = engine.simulate_turn()

    # Display the hand
    hand = actions.pop('hand')  # Remove hand from actions dict
    hand_display = ', '.join(
        [f"{card.name} ({card.cost})" for card in hand]
    )
    print(f"Hand: [{hand_display}]")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {actions}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
