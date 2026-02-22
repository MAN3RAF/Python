from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from typing import Optional


class GameEngine:
    """Game engine managing factory and strategy."""

    def __init__(self) -> None:
        """Initialize the game engine."""
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Configure engine with factory and strategy."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """Simulate a single turn."""
        deck = self.factory.create_themed_deck(5)
        hand = deck['cards'][:3]
        battlefield = deck['cards'][3:5]

        result = self.strategy.execute_turn(hand, battlefield)
        result['hand'] = hand

        self.turns_simulated += 1
        self.total_damage += result['damage_dealt']
        self.cards_created += 5

        return result

    def get_engine_status(self) -> dict:
        """Get engine status."""
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
