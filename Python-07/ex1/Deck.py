from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random


class Deck():
    """Represents a deck of cards."""

    def __init__(self) -> None:
        """Initialize an empty deck."""
        self.deck: list[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card by name from the deck."""
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck randomly."""
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        """Draw a card from the top of the deck."""
        if self.deck:
            card = self.deck[0]
            self.deck.remove(card)
        return card

    def get_deck_stats(self) -> dict:
        """Get statistics about the deck composition."""
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.deck:
            if isinstance(card, CreatureCard):
                creatures += 1
                total_cost += card.cost
            elif isinstance(card, SpellCard):
                spells += 1
                total_cost += card.cost
            elif isinstance(card, ArtifactCard):
                artifacts += 1
                total_cost += card.cost

        count = len(self.deck)
        avg = total_cost / count if count > 0 else 0

        return {
            "total_cards": count,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": f"{avg:.1f}",
        }
