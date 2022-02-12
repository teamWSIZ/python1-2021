from math import cos, sin

import matplotlib.pyplot as plt


def coord_x(r, phi):
    return r * cos(phi)


def coord_y(r, phi):
    return r * sin(phi)


x = [i for i in range(200)]
y = [e ** 2 for e in x]

plt.plot(x, y)
plt.savefig('gg.png')
plt.show()
