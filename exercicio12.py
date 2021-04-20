mapa = [[False] * 500 for i in range(500)]
n = int(input())
i = 0
r = 0
mito = False

for i in range(n):
    x, y = [(int(i) - 1) for i in input().split()]
    if mapa[x][y]:
        mito = True
    else:
        mapa[x][y] = True
        
print('1' if mito else '0')