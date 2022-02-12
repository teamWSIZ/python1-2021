"""
Problem: mamy daną "mapę" "alt" w postaci (x,y) -> h   (czyli dla "każdej" pary (x,y) mamy daną
wysokość npm.


Podano nam ścieżkę w postaci par (x,y), czyli [(x0,y0),(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
... wyliczyć ile metrów w górę i ile w dół trzeba było przejść na tej ścieżce.
"""

alt = dict()
# alt['abra'] = 'kadabra'
# alt['pi'] = 3.14

alt[(0, 0)] = 500
alt[(0, 1)] = 510
alt[(0, 2)] = 510
alt[(0, 3)] = 530

alt[(1, 0)] = 500
alt[(1, 1)] = 520
alt[(1, 2)] = 540
alt[(1, 3)] = 550

alt[(2, 0)] = 500
alt[(2, 1)] = 500
alt[(2, 2)] = 510
alt[(2, 3)] = 520

alt[(3, 0)] = 500
alt[(3, 1)] = 500
alt[(3, 2)] = 510
alt[(3, 3)] = 510

# [(x0,y0),(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
path = [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3)]

# zadanie: wyznaczyć listę "altitudes" będącą kolejnymi wysokościami na ścieżce
# zadanie: napisać funkcję "get_up_down" biorącą kolejne wysokości na ścieżce, i
#    zwracającą sumę podejść i zejść na niej