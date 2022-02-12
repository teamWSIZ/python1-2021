alts = [0, 10, 30, 20, 15, 40, 80, 150, 12, 0]

up = 0
dn = 0

prev = alts[0]

for a in alts:
    if prev < a:
        up += a - prev
    else:
        dn += prev - a
    prev = a

print(f'up={up} dn={dn}')