from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Any


class EliteCard(Card, Combatable, Magical):
    """Elite card with both combat and magical abilities."""

    def __init__(self, name: str, cost: int, rarity: str,
                 health: int, damage: int, defen: int,
                 combat_type: str, mana: int) -> None:
        """Initialize an elite card with combat and magic stats."""
        super().__init__(name, cost, rarity)

        self.health = health
        self.damage = damage
        self.defen = defen
        self.combat_type = combat_type
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        """Play the elite card."""
        return {
            'card': self.name,
            'cost': self.cost,
            'damage': self.damage,
            'combat_type': self.combat_type
        }

    def attack(self, target: Any) -> dict:
        """Attack a target, dealing damage."""
        target.health -= self.damage
        if target.health < 0:
            target.health = 0

        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.damage,
            'combat_type': self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""
        alive = True

        if incoming_damage > self.defen:
            damage_taken = incoming_damage - self.defen
            self.health -= damage_taken
            if self.health <= 0:
                self.health = 0
                alive = False
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': self.defen,
            'still_alive': alive
        }

    def get_combat_stats(self) -> dict:
        """Get combat statistics."""
        return {
            "card": self.name,
            "attack": self.damage,
            "defense": self.defen,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on target list."""
        if self.mana < self.cost:
            raise ValueError("[ERROR] Not enough mana!")
        else:
            self.mana -= self.cost

        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': [target.name for target in targets],
            'mana_used': self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        """Channel mana to increase mana pool."""
        self.mana += amount

        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        """Get magic statistics."""
        return {
            "card": self.name,
            "mana": self.mana
        }
