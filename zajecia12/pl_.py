from math import cos, sin, sqrt

import matplotlib.pyplot as plt

x = []
y = []
for f in range(20000):
    ph = f * 0.02
    r = sqrt(ph)
    x.append(r * cos(ph))
    y.append(r * sin(ph))

plt.plot(x,y)
plt.show()

