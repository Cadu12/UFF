n = int(input())
r = [int(i) for i in input().split()]

queda = 0
for i in range(n - 1):
    if r[i] > r[i + 1]:
        queda = i + 2
        break

print(queda)