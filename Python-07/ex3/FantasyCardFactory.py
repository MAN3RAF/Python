from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random

class FantasyCardFactory(CardFactory):

	def create_creature(self, name_or_power: str | int | None = None) -> Card:

		rarities = ["Common", "Rare"]

		creatures = ["Elf Archer", "Orc Warrior",
                     "Mountain Troll"]

		cards = {
			'Blue eyes White Dragon': {
				"cost": 8,
				"damage": 9,
				"rarity": "Epic",
				"health": 8
			},
			'Goblin Warrior': {
				"cost": 2,
				"damage": 3,
				"rarity": "Common",
				"health": 3
			},
			'Dark Magician': {
				"cost": 7,
				"damage": 8,
				"rarity": "Epic",
				"health": 7
			},
			'Exodia The Forbidden One': {
				"cost": 10,
				"damage": 10,
				"rarity": "Legendary",
				"health": 10
			},
			'Spirital Beast': {
				"cost": 5,
				"damage": 6,
				"rarity": "Rare",
				"health": 5
			}
		}

		if isinstance(name_or_power, str):
			name = name_or_power
			cost = random.randint(1, 6)
			rarity = random.choice(rarities)
			attack = random.randint(1, 6)
			health = random.randint(1, 6)
		elif isinstance(name_or_power, int):
			name = random.choice(creatures)
			cost = name_or_power
			rarity = random.choice(rarities)
			attack = random.randint(1, 6)
			health = random.randint(1, 6)
		else:
			creature = random.choice(list(cards.items()))

		card = CreatureCard(creature[0], creature[1]['cost'],
					  creature[1]['rarity'], creature[1]['damage'],
					  creature[1]['health'])

		return card

	def create_spell(self, name_or_power: str | int | None = None) -> Card:

		rarities = ["Common", "Rare", "Epic", "Legendary"]

		spells = [
			("FireBall", "damage"),
			("Healing Wave", "heal"),
			("Ice Blast", "damage"),
			("Lightning Bolt", "damage")
		]
		
		if isinstance(name_or_power, str):
			name = name_or_power
			cost = random.randint(1, 6)
			rarity = random.choice(rarities)
			if "Heal" in name_or_power:
				effect_type = 'heal'
			else:
				effect_type = 'damage'

		elif isinstance(name_or_power, int):
			name, effect_type = random.choice(spells)
			cost = name_or_power
			rarity = random.choice(rarities)

		else:
			name, effect_type = random.choice(spells)
			cost = random.randint(1, 6)
			rarity = random.choice(rarities)

		card = SpellCard(name, cost, rarity, effect_type)

		return card

	def create_artifact(self, name_or_power: str | int | None = None) -> Card:

		rarities = ["Common", "Rare", "Epic", "Legendary"]

		artifacts = [
			('Black Pendant' ,"Mana Boost"), 
			('Axe Of Despair', "Attack Boost"),
			("Nibelung's Ring", "Pasive Creature")
		]

		if isinstance(name_or_power, str):
			name = name_or_power
			cost = random.randint(1, 6)
			effect = "generic"

		elif isinstance(name_or_power, int):
			name, effect = random.choice(artifacts)
			cost = name_or_power

		else:
			name, effect = random.choice(artifacts)
			cost = random.randint(1, 4)

		durability = random.randint(1, 5)

		rarity = random.choice(rarities)

		card = ArtifactCard(name, cost, rarity, durability, effect)

		return card

	def create_themed_deck(self, size: int) -> dict:

		deck = []

		for _ in range(size):
			number = random.random()
			if number < 0.5:
				deck.append(self.create_creature)
			elif number < 0.8:
				deck.append(self.create_spell)
			else:
				deck.append(self.create_artifact)

		return deck

	def get_supported_types(self) -> dict:
		return {
            'creatures': ['dragon', 'goblin', 'dark_magician',
                          'exodia', 'spirital_beast', 'elf_archer',
						  'orc_warrior', 'mountain troll'],

            'spells': ['fireball', 'healing_wave',
                       'ice_blast', 'lightning_bolt'],

            'artifacts': ['black_pendant', 'axe_of_despair',
                          "nibelung's_ring"]
		}


# factory = FantasyCardFactory()

# card = factory.create_creature()

print(f"{random.random():.1f}")
