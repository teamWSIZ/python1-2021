from zajecia11.f import time_to_seconds
from zajecia11.runners_classes import MarathonRunner

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

print(f'runners: {len(runners)}')