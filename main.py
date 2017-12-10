

from scipy.optimize import fsolve
import math


d1 = 5
d2 = 70
P1 = 0.99
P2 = 0.001
p1 = (180-d1)/180
p2 = (180-d2)/180


def equations(p):
    r, b = p
    return (1 - P1 - (1 - p1**r)**b, 1 - P2 - (1 - p2**r)**b)

r, b =  fsolve(equations, (1, 1))
r, b = int(r), int(b)
print (r,b)