from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract base class for game strategies."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a turn with given hand and battlefield."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Get the name of the strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize targets for attacks."""
        pass
