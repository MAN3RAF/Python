from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random
from enum import Enum


class Deck():

	def __init__(self):
		self.deck: list = []

	def add_card(self, card: Card) -> None:
		self.deck.append(card)

	def remove_card(self, card_name: str) -> bool:
		for card in self.deck:
			if card.name == card_name:
				self.deck.remove(card)
				return True
		return False

	def shuffle(self) -> None:
		random.shuffle(self.deck)

	def draw_card(self) -> Card:
		if self.deck:
			card = self.deck[0]
			self.deck.remove(card)
			return card
		return None

	def get_deck_stats(self) -> dict:
		
		creatures = 0
		spells = 0
		artifacts = 0
		total_cost = 0

		for card in self.deck:
			if isinstance(card, CreatureCard):
				creatures += 1
				total_cost += card.cost
			elif isinstance(card, SpellCard):
				spells += 1
				total_cost += card.cost
			elif isinstance(card, ArtifactCard):
				artifacts += 1
				total_cost += card.cost
		
		count = len(self.deck)
		avg = total_cost / count if count > 0 else 0

		return {
			"total_cards": count,
			"creatures": creatures,
			"spells": spells,
			"artifacts": artifacts,
			"avg_cost": avg,
		}
			

# d = Deck()

# d.add_card(CreatureCard("GG1", 3, "Common", 2, 1))
# d.add_card(SpellCard("GG2", 7, "Common", "damage"))
# d.add_card(ArtifactCard("GG3", 3, "Common", 1, "GIGI"))
# d.add_card(CreatureCard("GG4", 2, "Common", 4, 3))
# d.add_card(CreatureCard("GG5", 1, "Common", 5, 2))

# b = d.get_deck_stats()

# print(b)