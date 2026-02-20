from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ArtifactCard import ArtifactCard
from SpellCard import SpellCard


class Deck():

	def __init__(self):
		self.deck: list = []

	def add_card(self, card: Card) -> None:
		self.deck.append(card)

	def remove_card(self, card_name: str) -> bool:
		for card in self.deck:
			if card.name == card_name:
				self.deck.remove(card_name)
				return True
		return False

	def shuffle(self) -> None:
		pass

	def draw_card(self) -> Card:
		pass

	def get_deck_stats(self) -> dict:
		pass