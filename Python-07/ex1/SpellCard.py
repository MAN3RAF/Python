from ex0.Card import Card
from enum import Enum
from typing import Any


class EffectType(Enum):
    """Enumeration for spell effect types."""
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    """Card representing spells with various effects."""

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        """Initialize a spell card with an effect type."""
        super().__init__(name, cost, rarity)

        if effect_type not in [effect.value for effect in EffectType]:
            raise ValueError("[ERROR] Invalid effect!")

        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Play the spell card, applying its effect."""
        if 'available_mana' in game_state:
            if game_state['available_mana'] >= self.cost:
                if self.effect_type == "damage":
                    self.effect = "deal 3 damage to target"
                elif self.effect_type == "heal":
                    self.effect = "+3 health points"
                elif self.effect_type == "buff":
                    self.effect = "damage buff for 3 turns"
                else:
                    self.effect = "damage debuff for 3 turns"
            else:
                raise ValueError("[ERROR] Not enough mana!")

            game_state['available_mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect,
        }

    def resolve_effect(self, targets: list[Any]) -> dict:
        """Resolve spell effect on target list."""
        for target in targets:
            if self.effect_type == "damage":
                target.health -= self.cost
                if target.health < 0:
                    target.health = 0
            elif self.effect_type == "heal":
                target.health += self.cost
            elif self.effect_type == "buff":
                target.attack *= 2  # Permanent buff!
            else:
                target.attack /= 2  # Permanent debuff!

        return {
            "Spell": self.name,
            "effect_type": self.effect_type,
            "target": targets,
            "status": "resolved",
        }
