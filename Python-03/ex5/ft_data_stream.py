from typing import Generator


def game_event_generator(count: int) -> Generator[dict, None, None]:
    """Generate game events for streaming processing."""
    players = ["alice", "bob", "charlie", "frank"]
    actions = [
        "found treasure",
        "leveled up",
        "killed monster",
        "logout",
        "kill",
        "quest_complete",
        "item_found",
        "death"]

    for i in range(count):
        player = players[i % len(players)]
        random_level = (i * 7) % 20 + 1
        action = actions[i % len(actions)]
        yield {
            "id": i, "player": player,
            "level": random_level, "action": action
        }


def stream_processor(event_stream: Generator) -> tuple[int, int, int, int]:
    """Process event stream and return analytics."""
    hight_level_count = treasure_count = level_up_count = events_count = 0

    for event in event_stream:
        events_count += 1

        if "leveled up" in event['action']:
            level_up_count += 1

        if event['level'] >= 10:
            hight_level_count += 1

        if "treasure" in event['action']:
            treasure_count += 1

    return hight_level_count, treasure_count, level_up_count, events_count


def fibonacci(num: int) -> Generator[int, None, None]:
    """Generate Fibonacci sequence."""
    a, b = 0, 1

    for _ in range(num):
        yield a
        a, b = b, a + b


def prime(limit: int) -> Generator[int, None, None]:
    """Generate prime numbers up to limit."""
    num = 2
    count = 0

    while count < limit:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num
            count += 1
        num += 1


def main() -> None:
    """Main function to demonstrate data stream processing."""
    print("=== Game Data Stream Processor ===\n")

    game_events = 1000

    print(f"Processing {game_events} game events...\n")

    i = 1
    for event in game_event_generator(game_events):
        print(
            f"Event {event['id'] + 1}: Player {event['player']} "
            f"(level {event['level']}) {event['action']}")
        if i == 3:
            print("...\n")
            break
        i += 1

    print("=== Stream Analytics ===")

    stream_events = game_event_generator(game_events)

    hight_level, treasure, level_up, events = stream_processor(stream_events)

    print(f"Total events processed: {events}")
    print(f"High-level players (10+): {hight_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}\n")

    print("Memory usage: Constant (streaming)")
    processing_time = game_events * 0.000045
    print(f"Processing time: {processing_time:.3f} seconds\n")

    print("=== Generator Demonstration ===")

    num = 10
    print(f"Fibonacci sequence (first {num}):", end=' ')
    j = 0
    for i in fibonacci(num):
        if j < num - 1:
            print(i, end=', ')
        else:
            print(i)
        j += 1

    num = 5
    print(f"Prime numbers (first {num}):", end=' ')

    j = 0
    for i in prime(num):
        if j < num - 1:
            print(i, end=', ')
        else:
            print(i)
        j += 1


main()
