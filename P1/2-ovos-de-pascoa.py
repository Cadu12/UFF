"""
ENTRADA:
8 8 4 6

SAIDA:
S

==============
ENTRADA:
767 77 384 724

SAIDA:
S
"""

from math import sqrt
a, b, c, d = [int(i) for i in input().split()]
area = sqrt(a ** 2 + b ** 2 + c ** 2)
areaOvo = d * 2
print("S" if area <= areaOvo else "N")