from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Aggressive game strategy focusing on damage."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute an aggressive turn."""
        mana = 30  # Available mana for the turn
        damage = 0
        spent = 0
        played_cards = []
        targets = ['Enemy Player']

        # Sort hand by cost (low to high) for aggressive play
        sorted_hand = sorted(hand, key=lambda card: card.cost)

        for card in sorted_hand:
            if card.cost <= mana:
                mana -= card.cost
                spent += card.cost

                # Calculate damage based on card type
                if hasattr(card, 'attack'):
                    damage += card.attack
                else:
                    damage += 5  # Default spell/artifact damage

                played_cards.append(card.name)

        return {
            'cards_played': played_cards,
            'mana_used': spent,
            'targets_attacked': targets,
            'damage_dealt': damage
        }

    def get_strategy_name(self) -> str:
        """Get the strategy name."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize targets with player first."""
        targets = []

        for target in available_targets:
            if target == 'player':
                targets.insert(0, target)
            else:
                targets.append(target)
        return targets
