import sys
i: int = 0


class EmptyError(Exception):
    """No scores"""
    def __init__(self):
        super().__init__("No scores provided. Usage: python3"
                         "ft_score_analytics.py <score1> <score2> ...")


def score_analytics(raw_scores: list[str] = sys.argv[1:]) -> None:
    try:
        if not raw_scores:
            raise EmptyError()
        scores = []
        for s in raw_scores:
            try:
                scores.append(int(s))
            except ValueError:
                print(f"Invalid parameter: '{s}'")

        if not scores:
            raise EmptyError()

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {(max(scores) - min(scores))}")

    except (EmptyError) as nope:
        print(f"{nope}")


if __name__ == "__main__":

    print("=== Player Score Analytics ===")
    score_analytics()
