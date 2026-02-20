from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ArtifactCard import ArtifactCard
from SpellCard import SpellCard


class Deck():
	def add_card(self, card: Card) -> None:
		pass

	def remove_card(self, card_name: str) -> bool:
		pass

	def shuffle(self) -> None:
		pass

	def draw_card(self) -> Card:
		pass

	def get_deck_stats(self) -> dict:
		pass