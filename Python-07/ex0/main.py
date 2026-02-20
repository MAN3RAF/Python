from abc import ABC, abstractmethod
from enum import Enum
from typing import Any
from CreatureCard import CreatureCard


def main():
	print("\n=== DataDeck Card Foundation ===\n")
	
	print("Testing Abstract Base Class Design:\n")

	card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
	available_mana = 6
	enemy_card = CreatureCard("Goblin Warrior", 1, "common", 2, 3)

	info = card.get_card_info()
	
	print(f"CreatureCard Info:\n{info}\n")

	info["available_mana"] =  available_mana


	playable = card.is_playable(available_mana)
	if playable:
		play_res = card.play(info)
		print(f"Playable: {playable}")
		print(f"Play result: {play_res}\n")
	else:
		print("Playable: False")

	attack_res = card.attack_target(enemy_card)

	print(f"Attack result: {attack_res}")

	print("\nTesting insufficient mana (3 available):")
	available_mana = 3
	playable = card.is_playable(available_mana)

	if playable:
		play_res = card.play(info)
		print(f"Playable: {playable}")
		print(f"Play result: {play_res}\n")
	else:
		print("Playable: False")
	print("\nAbstract pattern successfully demonstrated!")

if __name__ == "__main__":
	main()