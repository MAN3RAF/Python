from abc import ABC, abstractmethod
from enum import Enum
from typing import Any

class Rarity(Enum):
    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"

class Card(ABC):
	def __init__(self, name: str, cost: int, rarity: str):
		if rarity not in [r.value for r in Rarity]:
			raise ValueError("Invalid rarity")
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
		if available_mana <= 3:
			return False
		return True
