from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


def main():
	print("\n=== DataDeck Deck Builder ===\n")

	player_mana = 10

	print("Building deck with different card types...")

	deck = Deck()

	card1 = CreatureCard('Fire Dragon', 5, "Legendary", 5, 7)
	card2 = SpellCard('Lightning Bolt', 3, "Rare", "damage")
	card3 = ArtifactCard('Mana Crystal', 2, "Epic", 5, "Permanent: +1 mana per turn")

	deck.add_card(card1)
	deck.add_card(card2)
	deck.add_card(card3)

	deck_info = deck.get_deck_stats()

	print(deck_info)

	print("\nDrawing and playing cards:\n")

	while deck.deck:
		card = deck.draw_card()

		if isinstance(card, SpellCard):
			print("Drew: Lightning Bolt (Spell)")
		elif isinstance(card, ArtifactCard):
			print("Drew: Mana Crystal (Artifact)")
		elif isinstance(card, CreatureCard):
			print("Drew: Fire Dragon (Creature)")

		game_status = card.get_card_info()
		game_status['available_mana'] = player_mana

		play_result = card.play(game_status)
		print(f"Play result: {play_result}\n")
		
		player_mana = game_status['available_mana']

	print("Polymorphism in action: Same interface, different card behaviors!")

if __name__ == "__main__":
	main()
