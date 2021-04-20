from math import sqrt

def isFibonot(n):
    raiz1 = 5 * n * n + 4
    raiz2 = 5 * n * n - 4
    a = int(sqrt(raiz1))
    b = int(sqrt(raiz2))
    return a * a == raiz1 or b * b == raiz2

n = int(input())
i = 1
r = 0
while n >= i:
    r += 1
    if not isFibonot(r):
        i += 1

print(r)