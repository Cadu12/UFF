n, c, m = [int(i) for i in input().split()]
existes = [int(i) for i in input().split()]
comprados = [int(i) for i in input().split()]

evitaDup = []

for i in range(c):
    for j in range(m):
        if existes[i] == comprados[j]:
            if not comprados[j] in evitaDup:
                evitaDup.append(comprados[j])
                c -= 1

print(c)