import random

class Players:
    def __init__(
        self,
        draft_names: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 
                                'Gregory', 'john', 'kevin', 'Liam']
    ):
        self.draft_names = draft_names
        self.capitalized_names = self.capitalize_all()
        self.score_dict = self.add_to_dict()
        self.average = self.score_avr()
        self.prev_cap = self.cap_names()

    def player_names(self) -> list[str]:
        print(f"Initial list of players: {self.draft_names}")
        return (self.draft_names)

    def capitalize_all(self) -> list[str]:
        capitalized = [name.capitalize() for name in self.draft_names]
        return (capitalized)
    
    def cap_names(self) -> list[str]:
        cap_names = [name for name in self.draft_names if name[0].isupper()]
        return (cap_names)

    def add_to_dict(self, count: int = 9) -> dict[str, int]:

        self.score_dict = {
            random.choice(self.capitalized_names): random.randint(0, 1000)
            for _ in range(count)
        }
        return (self.score_dict)

    def score_avr(self) -> float:

        total = sum(score for score in self.score_dict.values())
        count = len(self.score_dict)

        return (total / count)

    def high_score(self) -> dict[str, int]:
        
        result = {key: score for key, score in self.score_dict.items() if score >= self.average}

        return(result)


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    info = Players()
    info.player_names()

    capitalized = info.capitalize_all()
    cap_names = info.prev_cap
    dictionary = info.add_to_dict()
    average_score = info.score_avr()
    highscore = info.high_score()

    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {cap_names}")
    print(f"Score dict: {dictionary}")
    print(f"Score Average is {round(average_score, 2)}")
    print(f"High scores: {highscore}")




    


