from typing import List

from zajecia11.f import time_to_seconds
from zajecia11.runners_classes import MarathonRunner


def get_runners():
    runners = []
    with open('challenge.csv') as f:
        lines = f.readlines()
        lines = lines[1:]
        for l in lines:
            row = l.split(',')
            try:
                mr = MarathonRunner(int(row[4]), row[5], row[3], time_to_seconds(row[6]),
                                    time_to_seconds(row[8]), time_to_seconds(row[9]))
                runners.append(mr)
            except ValueError:
                pass
            # print(mr)
    return runners


def get_runners_of_country(all_runners: List[MarathonRunner], country: str) -> List[MarathonRunner]:
    return [u for u in all_runners if u.country == country]


runners = get_runners()
print(f'all_runners: {len(runners)}')
jp = get_runners_of_country(runners, 'Japan')

of_interest = ['China', 'Japan', 'South Korea', 'Taiwan', 'Thailand']
for country in of_interest:
    runners_of_c = get_runners_of_country(runners, country)
    print(f'country: {country}, runners: {len(runners_of_c)}')