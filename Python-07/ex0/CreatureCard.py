from typing import Any
from .Card import Card


class CreatureCard(Card):
	def __init__(self, name: str, cost: int, rarity: str, 
			  attack: int, health: int):

		super().__init__(name, cost, rarity)

		if not isinstance(attack, int) or attack < 0:
			raise ValueError("[ERROR] Attack must be a positive integer!")

		if not isinstance(health, int) or health <= 0:
			raise ValueError("[ERROR] Health must be a positive integer!")

		self.attack = attack
		self.health = health

	def play(self, game_state: dict) -> dict:
		if 'available_mana' in game_state:
			game_state['available_mana'] -= self.cost

		return {
			"card_played": self.name,
			"mana_used": self.cost,
			"effect": "Creature summoned to battlefield",
		}

	def get_card_info(self) -> dict:
		return {
			"name":self.name,
			"cost":self.cost,
			"rarity":self.rarity,
			"type": "Creature",
			"attack": self.attack,
			"health": self.health,
		}

	def attack_target(self, target: Any) -> dict:
		print(f"{self.name} attacks {target.name}:")
		target.health -= self.attack
		if target.health < 0:
			target.health = 0
		return {
			"attacker": self.name,
			"target": target.name,
			"damage_dealt": self.attack,
			"combat_resolved": True,
		}
