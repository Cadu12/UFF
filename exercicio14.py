matriz = []
for i in range(3):
    matriz.append([int(i) for i in input().split()])

print(max(map(sum, matriz)))