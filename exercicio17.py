from functools import cmp_to_key

def ordena(pais1, pais2):    
    if pais1[1] > pais2[1]:
        return 1
    elif pais1[1] == pais2[1]:
        if pais1[2] > pais2[2]:
            return 1
        elif pais1[2] == pais2[2]:
            if pais1[3] > pais2[3]:
                return 1
            elif pais1[3] == pais2[3]:
                return 0
            elif pais1[3] < pais2[3]:
                return -1
        elif pais1[2] < pais2[2]:
            return -1
    elif pais1[1] < pais2[1]:
        return -1

n = int(input())
paises = []
for i in range(n):
    paises.append(input().split())
    
paises.sort(key = lambda m: (m[1], m[2], m[3], m[0]))

for i in paises:
    print("===", i)