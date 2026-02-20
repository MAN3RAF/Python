from ex0.Card import Card


class ArtifactCard(Card):
	def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
		super().__init__(name, cost, rarity)

		if not isinstance(durability, int) or durability < 0:
			raise ValueError("[ERROR] durability must be a positive number")

		self.durability = durability
		self.effect = effect

	def play(self, game_state: dict) -> dict:
		
		print(f"Drew: {self.name} (Artifact)")

		if 'available_mana' in game_state:
			game_state['available_mana'] -= self.cost

		return {
			'card_played': self.name,
			'mana_used': self.cost,
			'effect': self.effect
		}

	def activate_ability(self) -> dict:
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

