from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 power: int = 0, toughness: int = 0,
                 base_rating: int = 1200):
        super().__init__(name, cost, rarity)
        self.power = power
        self.toughness = toughness
        self.wins = 0
        self.losses = 0
        self.base_rating = base_rating

    def play(self, game_state: dict) -> dict:
        game_state['played_card'] = self.name
        game_state['mana_remaining'] = (
            game_state.get('mana', 0) - self.cost
        )
        return game_state

    def attack(self, target) -> dict:
        damage_dealt = self.power
        target_name = (target.name if hasattr(target, 'name')
                       else str(target))
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': damage_dealt
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.toughness)
        survived = damage_taken < self.toughness
        return {
            'defender': self.name,
            'incoming_damage': incoming_damage,
            'damage_taken': damage_taken,
            'survived': survived
        }

    def get_combat_stats(self) -> dict:
        return {
            'name': self.name,
            'power': self.power,
            'toughness': self.toughness
        }

    def calculate_rating(self) -> int:
        return (self.base_rating
                + (self.wins * 16)
                - (self.losses * 16))

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            'name': self.name,
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.calculate_rating()
        }

    def get_tournament_stats(self) -> dict:
        return {
            'name': self.name,
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.calculate_rating(),
            'power': self.power,
            'toughness': self.toughness,
            'record': f"{self.wins}-{self.losses}"
        }
