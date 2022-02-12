from random import randint

from zajecia14.div6_bis import split


def split_random(x: int) -> tuple[int, int]:
    best = 0
    sol = (0, 0)
    for _ in range(10000):
        k3 = randint(0, x // 3)
        rest = x - k3 * 3
        if k3 > best and 3 < rest <= 6:
            sol = (k3 * 3, rest)
    return sol

for _ in range(30):
    x = randint(8,80000)
    print(split(x))
    print(split_random(x))
