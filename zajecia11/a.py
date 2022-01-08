from dataclasses import dataclass


class Sportsman:
    max_hr: int


class Runner(Sportsman):
    best_time_1k: float


class Biker(Sportsman):
    pass


class Swimmer(Sportsman):
    best_butterfly_400m: float


class Thriatlonist(Runner, Biker, Swimmer):
    pass


@dataclass
class MarathonRunner:  # klasa
    race_no: int  # pola klasy
    country: str
    category: str


if __name__ == '__main__':
    u1 = MarathonRunner(1, 'Kenya', 'MMM2')  # instancja klasy MarathonRunner
    u2 = MarathonRunner(2, 'Thailand', 'MMM2')  # instancja klasy MarathonRunner
    u3 = MarathonRunner(3, 'Brasil', 'MMM1')  # instancja klasy MarathonRunner

    # u1.race_no = 1
    # u1.country = 'Kenya'
    #
    # u2.race_no = 2
    # u2.country = 'Thailand'
    #
    # u3.race_no = 3
    # u3.country = 'Uruguay'

    runners = [u1, u2, u3]

    for u in runners:
        print(f'number: {u.race_no}, country:{u.country}')
        if u.category == 'MMM1':
            print(u)

    countries = [u.country for u in runners]
    countries.sort()
    print(countries)