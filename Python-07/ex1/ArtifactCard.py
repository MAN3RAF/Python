from ex0.Card import Card


class ArtifactCard(Card):
    """Card representing an artifact with durability and effects."""

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        """Initialize an artifact card with durability and effect."""
        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability < 0:
            raise ValueError(
                "[ERROR] durability must be a positive number"
            )

        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Play the artifact card, deducting mana if available."""
        if 'available_mana' in game_state:
            if game_state['available_mana'] >= self.cost:
                game_state['available_mana'] -= self.cost
            else:
                raise ValueError("[ERROR] Not enough mana")
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def activate_ability(self) -> dict:
        """Activate artifact ability, reducing durability."""
        if self.durability > 0:
            self.durability -= 1
            return {
                "artifact": self.name,
                "durability": self.durability,
                "effect": self.effect
            }
        else:
            return {
                "artifact": self.name,
                "durability": self.durability,
                "effect": "[ERROR] Can't use the artifact (0 durability)"
            }
