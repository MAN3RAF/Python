from ex0.Card import Card
from enum import Enum
# from ex0.CreatureCard import CreatureCard


class EffectType(Enum):
	DAMAGE = "damage"
	HEAL = "heal"
	BUFF = "buff"
	DEBUFF = "debuff"


class SpellCard(Card):
	def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
		super().__init__(name, cost, rarity)

		if effect_type not in [effect.value for effect in EffectType]:
			raise ValueError("[ERROR] Invalid effect!")

		self.effect_type = effect_type

	def play(self, game_state: dict) -> dict:
		print(f"Drew: {self.name} (Spell)")
		
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
				game_state['available_mana'] -= self.cost
		return {
			'card_played': self.name,
			'mana_used': self.cost,
			'effect': self.effect,
		}

	def resolve_effect(self, targets: list) -> dict:

		for target in targets:
			if self.effect_type == "damage":
				target.health -= self.cost
				if target.health < 0:
					target.health = 0
			elif self.effect_type == "heal":
				target.health += self.cost
			elif self.effect_type == "buff":
				target.attack *= 2			#Permanent buff!
			else:
				target.attack /= 2			#Permanent debuff!

		return {
			"Spell": self.name,
			"effect_type": self.effect_type,
			"target": targets,
			"status": "resolved",
		}

# heal_card = SpellCard("GG!", 3, "Rare", "heal")

# card1 = CreatureCard("GOGO!", 2, "Common", 1, 3)
# card2 = CreatureCard("GOGO!", 2, "Common", 1, 3)
# card3 = CreatureCard("GOGO!", 2, "Common", 1, 3)

# print(heal_card.resolve_effect([card1, card2, card3]))