l, c, m, n = [int(i) for i in input().split()]

margaridas = []
for i in range(l):
    margaridas.append([int(i) for i in input().split()])
    
maior = 0

for i in range(0, l, m):
    for j in range(0, c, n):
        lote = 0
        for k in range(i, i + m):
            for l in range(j, j + n):
                lote += margaridas[k][l]
        if lote > maior:
            maior = lote
            
print(maior)