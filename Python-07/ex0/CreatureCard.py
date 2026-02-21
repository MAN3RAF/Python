from typing import Any
from .Card import Card


class CreatureCard(Card):
    """Card class representing creatures with attack and health."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        """Initialize a creature card with attack and health stats."""
        super().__init__(name, cost, rarity)

        # Validate attack
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("[ERROR] Attack must be a positive integer!")

        # Validate health
        if not isinstance(health, int) or health <= 0:
            raise ValueError("[ERROR] Health must be a positive integer!")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """Play the creature card, deducting mana if available."""
        if 'available_mana' in game_state:
            if game_state['available_mana'] >= self.cost:
                game_state['available_mana'] -= self.cost
            else:
                raise ValueError("[ERROR] Not enough mana")
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def get_card_info(self) -> dict:
        """Return creature card information including stats."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health,
        }

    def attack_target(self, target: Any) -> dict:
        """Attack another creature, dealing damage equal to attack value."""
        print(f"{self.name} attacks {target.name}:")
        # Deal damage to target
        target.health -= self.attack
        if target.health < 0:
            target.health = 0
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
