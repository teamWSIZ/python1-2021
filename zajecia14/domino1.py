import time
from random import choice, seed

from zajecia14.gg import get_sample


def solve_domino(domino_start: list[str]) -> list[str]:
    domino = domino_start.copy()
    starter = '-A'
    game = [starter]

    while True:
        changed = False
        i = 0
        a = len(domino)
        while i < a:
            if domino[i][0] == game[-1][1]:
                game.append(domino[i])
                a -= 1
                domino.pop(i)
                changed = True
            i += 1
        if not changed:
            break
    return game


def solve_domino_randomly(domino: list[str]) -> list[str]:
    best = []
    domino_start = domino.copy()
    for _ in range(10000):
        starter = '-A'
        domino = domino_start.copy()
        game = [starter]
        seed(time.time() % 10007)
        while True:
            matching = []
            for piece in domino:
                if piece[0] == game[-1][1]:
                    matching.append(piece)
            if len(matching) == 0:
                break
            chosen_piece = choice(matching)
            game.append(chosen_piece)
            domino.remove(chosen_piece)
        if len(game) > len(best):
            best = game
    return best


domino = get_sample(alpha=4, length=40, seed_=12)
print(solve_domino(domino))
print(solve_domino_randomly(domino))

# O(N 2**N)