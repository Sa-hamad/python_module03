import random
from typing import Generator


def gen_event(
    list_name: list[str] = ["bob", "alice", "dylan", "charlie"],
    list_action: list[str] = ["run", "eat", "sleep", "grab",
                              "move", "climb", "swim", "release"]
) -> Generator[tuple[str, str], None, None]:

    while True:
        yield (random.choice(list_name), random.choice(list_action))


def gather_list(
        generated_event: Generator[tuple[str, str], None, None],
        len: int) -> list[tuple[str, str]]:
    events = []
    for _ in range(len):
        events.append(next(generated_event))
    return events


def consume_event(
        events: list[tuple[str, str]]
) -> Generator[tuple[tuple[str, str], list[tuple[str, str]]], None, None]:
    for _ in range(len(events)):
        pair = random.choice(events)
        events.remove(pair)
        yield pair, events


if __name__ == "__main__":
    stream = gen_event()
    gathered_list = gather_list(stream, 10)
    changed_list = consume_event(gathered_list)
    print("=== Game Data Stream Processor ===")

    for num in range(1000):
        name, action = next(stream)
        print(f"Event {num}: Player {name} did action {action}")

    print(f"Build list of events: {gathered_list}")

    for pair, remaining_list in changed_list:
        print(f"Got Event from list: {pair}")
        print(f"Remains in list: {remaining_list}")
