import random
import itertools

def build_master_keyword():
    words = open("keywords.txt").read().splitlines()
    combo = random.sample(words, 2)
    number = random.randint(1000, 999999)
    return f"{combo[0]}_{combo[1]}_{number}"

def choose_mode():
    return random.choice([
        "EMERGENCY PSA",
        "TRAINING TAPE",
        "CONTAINMENT FAILURE",
        "RELIGIOUS WARNING",
        "EDUCATIONAL FILM 1994"
    ])
