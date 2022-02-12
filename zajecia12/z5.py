from math import sin, cos, sqrt
import matplotlib.pyplot as plt

def coord_x(r, phi):
    return r * cos(phi)


def coord_y(r, phi):
    return r * sin(phi)


f = 0
df = 0.01
phi = []
while f < 100:
    f += df
    phi.append(f)
# print(phi)

x = [coord_x(sqrt(f), f) for f in phi]
y = [coord_y(sqrt(f), f) for f in phi]

plt.plot(x,y)
plt.show()