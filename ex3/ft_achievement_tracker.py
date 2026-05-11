import random


def gen_player_achievements():

    Achievements = ['Collector Supreme', 'Unstoppable', 'Untouchable',
                    'Speed Runner', 'World Savior', 'Crafting Genius',
                    'Survivor', 'First Steps', 'Sharp Mind', 'Boss Slayer',
                    'Master Explorer', 'Strategist', 'Treasure Hunter']

    Alice = set(random.sample(Achievements, 7))
    Bob = set(random.sample(Achievements, 9))
    Charlie = set(random.sample(Achievements, 4))
    Dylan = set(random.sample(Achievements, 6))

    Achievements = Alice.union(Bob, Charlie, Dylan)
    In_common = Alice.intersection(Bob, Charlie, Dylan)

    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}:")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")
    print(f"\nAll distinct achievements: {Achievements}")
    print(f"\nCommon achievements: {In_common}")
    print(f"\nOnly Alice has: {Alice.difference(Charlie, Bob, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}:")
    print(f"Only Charlie has: {Charlie.difference(Alice, Bob, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Charlie, Alice, Bob, Dylan)}")

    print(f"\nAlice is missing: {Achievements.difference(Alice)}")
    print(f"Bob is missing: {Achievements.difference(Bob)}")
    print(f"Charlie is missing: {Achievements.difference(Charlie)}")
    print(f"Dylan is missing: {Achievements.difference(Dylan)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    gen_player_achievements()
