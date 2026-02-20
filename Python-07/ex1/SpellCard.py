from ex0.Card import Card
from enum import Enum


class EffectType(Enum):
	DAMAGE = "damage"
	HEAL = "heal"
	BUFF = "buff"
	DEBUFF = "debuff"


class SpellCard(Card):
	def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
		super().__init__(name, cost, rarity)
		if effect_type not in [effect.value for effect in EffectType]:
			raise ValueError("[ERROR] Invalid rarity!")
		self.effect_type = effect_type

	def play(self, game_state: dict) -> dict:
		print(f"Drew: {self.name} (Spell)")
		if self.effect_type == "damage":
			self.effect = "deal 3 damage to target"
		elif self.effect_type == "heal":
			self.effect = "+3 health points"
		elif self.effect_type == "buff":
			self.effect = "damage buff for 3 turns"
		else:
			self.effect = "damage debuff for 3 turns"
		return {
			'card_played': self.name,
			'mana_used': self.cost,
			'effect': self.effect
			}

	def resolve_effect(self, targets: list) -> dict:
		pass

s = SpellCard("GG", 1, "Common", "damage")

g = s.play({})

print(g)
