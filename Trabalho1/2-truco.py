"""
1
1 2 3 1 3 2

1 0
--------------------
2
1 5 6 6 3 4
5 6 2 11 13 12

1 1
--------------------
5
1 2 11 12 7 6
3 5 1 13 1 4
4 5 7 11 12 13
1 5 6 3 5 2
5 6 7 4 5 2

3 2
"""
cartas = {}
cartas[4] = 1
cartas[5] = 2
cartas[6] = 3
cartas[7] = 4
cartas[12] = 5
cartas[11] = 6
cartas[13] = 7
cartas[1] = 8
cartas[2] = 9
cartas[3] = 10

jogador1 = 0
jogador2 = 0

n = int(input())
for i in range(n):
    partida = [(int(i)) for i in input().split()]
    soma1 = 0
    soma2 = 0
    
    for j in range(3):
        if cartas[partida[j]] >= cartas[partida[j + 3]]:
            soma1 += 1
        else:
            soma2 += 1
            
    if (soma1 > soma2):
        jogador1 += 1
    else:
        jogador2 += 1
        
print(jogador1, jogador2)