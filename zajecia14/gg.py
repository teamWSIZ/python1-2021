from random import randint, seed


def get_random_piece(alpha=3):
    st = chr(ord('A') + randint(0, alpha - 1))
    en = chr(ord('A') + randint(0, alpha - 1))
    return st + en


def get_sample(alpha=3, length=10, seed_=111):
    seed(seed_)
    return [get_random_piece(alpha) for _ in range(length)]


if __name__ == '__main__':
    print(get_sample())
