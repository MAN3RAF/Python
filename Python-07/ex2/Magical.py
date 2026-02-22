from abc import ABC, abstractmethod


class Magical(ABC):
    """Abstract interface for cards with magical abilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel mana to increase available mana pool."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Get magic statistics."""
        pass
