n = int(input())
for i in range(n):
    m = int(input())
    p = [int(i) for i in input().split()]
    pOrdem = sorted(p, reverse = True)
    t = 0
    for i in range(m):
        if p[i] != pOrdem[i]:
            t += 1
    print(m - t)