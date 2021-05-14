"""
ENTRADA:
4 50
55 55 45 45

SAIDA:
10
--------------------
ENTRADA:
5 84
94 72 17 39 84

SAIDA:
77
"""

n, h = [int(i) for i in input().split()]
alturas = [int(i) for i in input().split()]

index = 0
movimentos = 0
while True:
    if alturas[index] == h:
        if index == n - 1:
            break
        else:
            index += 1
    else:
        movimentos += 1
        if alturas[index] > h:
            alturas[index] -= 1
            alturas[index + 1] -= 1
        else:
            alturas[index] += 1
            alturas[index + 1] += 1
    
print(movimentos)