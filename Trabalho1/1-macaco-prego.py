"""
ENTRADA:
3
0 6 8 1
1 5 6 3
2 4 9 0
3
0 4 4 0
3 1 7 -3
6 4 10 0
0

SAIDA:
Teste 1
2 4 6 3

Teste 2
nenhum
"""

teste = 1
while True:
    regioes = int(input())
    if regioes <= 0:
        break
    
    print("Teste", teste)
    
    x1, y1, x2, y2 = -10000, 10000, 10000, -10000   
    
    for i in range(regioes):
        a, b, c, d = [int(i) for i in input().split()]
        if a > x1:
            x1 = a
        if b < y1:
            y1 = b
        if c < x2:
            x2 = c
        if d > y2:
            y2 = d
    
    if x2 < x1 or y1 < y2:
        print("nenhum")
    else:
        print(x1, y1, x2, y2)
        
    teste += 1
    print()