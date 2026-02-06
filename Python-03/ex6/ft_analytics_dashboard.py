players = [
    {
        "name": "alice",
        "score": 2300,
        "active": True,
        "achievements": ["first_kill", "boss_slayer"],
        "region": "north"
    },
    {
        "name": "bob",
        "score": 1800,
        "active": True,
        "achievements": ["first_kill"],
        "region": "east"
    },
    {
        "name": "charlie",
        "score": 2150,
        "active": True,
        "achievements": ["boss_slayer", "collector"],
        "region": "north"
    },
    {
        "name": "diana",
        "score": 2050,
        "active": False,
        "achievements": ["level_10"],
        "region": "central"
    }
]


def list_comprehensions() -> tuple[list, list, list]:
    """Demonstrate list comprehension examples."""
    high_scores = [p['name'] for p in players if p['score'] > 2000]
    double_scores = [p['score'] * 2 for p in players]
    active_players = [p['name'] for p in players if p['active']]

    return high_scores, double_scores, active_players


def dict_comprehensions() -> tuple[dict, dict, dict]:
    """Demonstrate dict comprehension examples."""
    player_scores = {p['name']: p['score'] for p in players}
    score_categories = {
        "high": len([p for p in players if p['score'] > 2100]),
        "medium": len([p for p in players if 1500 < p['score'] < 2100]),
        "low": len([p for p in players if p['score'] < 1500])
    }
    achievement_count = {p['name']: len(p['achievements']) for p in players}

    return player_scores, score_categories, achievement_count


def set_comprehensions() -> tuple[set, set, set]:
    """Demonstrate set comprehension examples."""
    unique_players = {p['name'] for p in players}
    unique_achievements = {
        p for player in players for p in player['achievements']
    }
    active_regions = {p['region'] for p in players}

    return unique_players, unique_achievements, active_regions


def combined_analysis(
        unique_achievements: set) -> tuple[int, int, float, dict]:
    """Perform combined analysis on player data."""
    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    score = [p['score'] for p in players]
    average_score = sum(score) / total_players
    top_score = max(score)
    top_player = [p for p in players if p['score'] == top_score][0]

    return total_players, total_unique_achievements, average_score, top_player


def main() -> None:
    """Main function to run analytics dashboard."""
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    high, double, active = list_comprehensions()
    print(f"High scorers (>2000): {high}")
    print(f"Scores doubled: {double}")
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")
    scores, categories, achievements = dict_comprehensions()
    print(f"Player scores: {scores}")
    print(f"Score categories: {categories}")
    print(f"Achievement counts: {achievements}")

    print("\n=== Set Comprehension Examples ===")
    players, achievements, regions = set_comprehensions()
    print(f"Unique players: {players}")
    print(f"Unique achievements: {achievements}")
    print(f"Active regions: {regions}")

    print("\n=== Combined Analysis ===")
    players, u_achievements, average, top = combined_analysis(achievements)
    print(f"Total players: {players}")
    print(f"Total unique achievements: {u_achievements}")
    print(f"Average score: {average}")
    print(
        f"Top performer: {top['name']} ({top['score']} points, "
        f"{len(top['achievements'])} achievements)"
    )


main()
