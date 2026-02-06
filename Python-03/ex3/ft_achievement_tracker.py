
def main() -> None:
    """Track and analyze player achievements."""
    alice_achievements = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }
    bob_achievements = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }
    charlie_achievements = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }

    all_achievements = alice_achievements.union(
        bob_achievements, charlie_achievements)
    shared_achievements = (
        alice_achievements.intersection(bob_achievements).union(
            alice_achievements.intersection(charlie_achievements).union(
                bob_achievements.intersection(charlie_achievements))))
    rare_achievements = all_achievements.difference(shared_achievements)

    print("=== Achievement Tracker System ===\n")

    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}\n")

    print("=== Achievement Analytics ===\n")

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    print(
        f"Common to all players: {
            alice_achievements.intersection(
                bob_achievements,
                charlie_achievements)}")

    print(f"Rare achievements (1 player): {rare_achievements}\n")

    print(
        f"Alice vs Bob common: {
            alice_achievements.intersection(bob_achievements)}")
    print(f"Alice unique: {alice_achievements.difference(bob_achievements)}")
    print(f"Bob unique: {bob_achievements.difference(alice_achievements)}")


main()
