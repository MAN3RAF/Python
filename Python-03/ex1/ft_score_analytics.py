import sys


def main() -> None:
    """Analyze and display player score statistics."""
    program_len = len(sys.argv)
    print("=== Player Score Analytics ===")
    if program_len < 2:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )

    else:
        score_list = []
        try:
            for i in range(1, program_len):
                score_list.append(int(sys.argv[i]))
            print(f"Scores processed: {score_list}")
            print(f"Total players: {program_len - 1}")
            print(f"Total score: {sum(score_list)}")
            print(f"Average score: {sum(score_list) / (program_len - 1)}")
            print(f"High score: {max(score_list)}")
            print(f"Low score: {min(score_list)}")
            print(f"Score range: {max(score_list) - min(score_list)}")
        except ValueError:
            print("Error: All the scores must be numbers!")


main()
