from ex0.CreatureCard import CreatureCard, Card
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
	def execute_turn(self, hand: list, battlefield: list) -> dict:
		mana = 10
		damage = 0
		spent = 0
		played_cards = []

		for card in hand:
			if card.cost > mana:
				raise "[ERROR] not enough mana"

			mana -= card.cost
			spent += card.cost
			damage += 5
			played_cards.append(card.name)

		return {
			"damage_dealt": damage,
			"mana_spent": spent,
			"cards_played": len(played_cards),
			"cards": played_cards
		}


	def get_strategy_name(self) -> str:
		return "AggressiveStrategy"

	def prioritize_targets(self, available_targets: list) -> list:
		targets = []

		for target in available_targets:
			if target == 'player':
				targets.insert(0, target)
			else:
				targets.append(target)
		return targets
