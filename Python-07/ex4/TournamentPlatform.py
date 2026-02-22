from ex4.TournamentCard import TournamentCard
from typing import Dict
import random


class TournamentPlatform:
    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0
        self.card_counter: Dict[str, int] = {}

    def register_card(self, card: TournamentCard) -> str:
        base_name = card.name.lower().replace(' ', '_')

        if base_name not in self.card_counter:
            self.card_counter[base_name] = 0

        self.card_counter[base_name] += 1
        card_id = f"{base_name}_{self.card_counter[base_name]:03d}"

        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError("One or both card IDs not found")

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        attack_result = card1.attack(card2)
        card2.defend(attack_result['damage'])

        if card1.power > card2.power:
            winner_id = card1_id
            loser_id = card2_id
        elif card2.power > card1.power:
            winner_id = card2_id
            loser_id = card1_id
        else:
            winner_id, loser_id = random.choice([
                (card1_id, card2_id),
                (card2_id, card1_id)
            ])

        winner = self.cards[winner_id]
        loser = self.cards[loser_id]

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self.cards.items(),
            key=lambda x: x[1].calculate_rating(),
            reverse=True
        )

        leaderboard = []
        for card_id, card in sorted_cards:
            leaderboard.append({
                'id': card_id,
                'name': card.name,
                'rating': card.calculate_rating(),
                'wins': card.wins,
                'losses': card.losses,
                'record': f"{card.wins}-{card.losses}"
            })

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)

        if total_cards > 0:
            total = sum(
                card.calculate_rating()
                for card in self.cards.values()
            )
            avg_rating = total // total_cards
        else:
            avg_rating = 0

        return {
            'total_cards': total_cards,
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': ('active' if total_cards > 0
                                else 'inactive')
        }
