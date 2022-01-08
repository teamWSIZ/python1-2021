from zajecia11.a import MarathonRunner

runners = []
with open('challenge.csv') as f:
    lines = f.readlines()
    lines = lines[1:]
    for l in lines:
        row = l.split(',')
        mr = MarathonRunner(int(row[4]), row[5], row[3])
        runners.append(mr)
        # print(mr)

print(f'runners: {len(runners)}')