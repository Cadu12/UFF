matriz = []
for i in range(4):
    matriz.append([int(i) for i in input().split()])

print(max(map(max, matriz)))