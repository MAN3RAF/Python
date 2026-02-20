from abc import ABC, abstractmethod
from enum import Enum

class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
	def __init__(self, name: str, cost: int, rarity: str):
		if rarity not in [r.value for r in Rarity]:
			raise ValueError("[ERROR] Invalid rarity!")

		if not isinstance(cost, int) or cost < 0:
			raise ValueError("[ERROR] cost must be a positive integer!")
 
		self.name = name
		self.cost = cost
		self.rarity = rarity

	@abstractmethod
	def play(self, game_state: dict) -> dict:
		return game_state

	def get_card_info(self) -> dict:
		info = {
			"name":self.name,
			"cost":self.cost,
			"rarity":self.rarity,
		}
		return info

	def is_playable(self, available_mana: int) -> bool:
		if available_mana < self.cost:
			return False
		return True
