from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    """Enumeration for card rarity levels."""
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    """Abstract base class for all card types."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize a card with name, cost, and rarity."""
        # Validate rarity
        if rarity not in [r.value for r in Rarity]:
            raise ValueError("[ERROR] Invalid rarity!")

        # Validate cost
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("[ERROR] cost must be a positive integer!")

        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play the card with the given game state."""
        pass

    def get_card_info(self) -> dict:
        """Return dictionary containing card information."""
        info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }
        return info

    def is_playable(self, available_mana: int) -> bool:
        """Check if card can be played with available mana."""
        if available_mana < self.cost:
            return False
        return True
