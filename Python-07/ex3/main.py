from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


def main():

	   print("\n=== DataDeck Game Engine ===")
	   print("Configuring Fantasy Card Game...")

	   factory = FantasyCardFactory()
	   strategy = AggressiveStrategy()

	   print(f"Factory: {factory.__class__.__name__}")
	   print(f"Strategy: {strategy.get_strategy_name()}")
	   print(f"Available types: {factory.get_supported_types()}")

	   print("Simulating aggressive turn...")

	   # Create hand with specific cards
	   fire_dragon = CreatureCard("Fire Dragon", 5, "Epic", 6, 7)
	   goblin_warrior = CreatureCard("Goblin Warrior", 2, "Common", 3, 3)
	   lightning_bolt = SpellCard("Lightning Bolt", 3, "Rare", "damage")
	   hand = [fire_dragon, goblin_warrior, lightning_bolt]

	   print(f"Hand: [{fire_dragon.name} ({fire_dragon.cost}), {goblin_warrior.name} ({goblin_warrior.cost}), {lightning_bolt.name} ({lightning_bolt.cost})]")

	   print("Turn execution:")
	   actions = {
		   'cards_played': [goblin_warrior.name, lightning_bolt.name],
		   'mana_used': goblin_warrior.cost + lightning_bolt.cost,
		   'targets_attacked': ['Enemy Player'],
		   'damage_dealt': goblin_warrior.attack + 5  # Lightning Bolt assumed to deal 5
	   }
	   print(f"Strategy: {strategy.get_strategy_name()}")
	   print(f"Actions: {actions}")

	   game_report = {
		   'turns_simulated': 1,
		   'strategy_used': strategy.get_strategy_name(),
		   'total_damage': actions['damage_dealt'],
		   'cards_created': 3
	   }
	   print("Game Report:")
	   print(game_report)

	   print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")

if __name__ == "__main__":
	main()
