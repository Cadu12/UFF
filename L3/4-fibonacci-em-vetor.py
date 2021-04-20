t = int(input())
for i in range(t):
    n = int(input())
    
    if n >= 1:
        v = [0, 1]
        for j in range(2, n + 1):
            v.append(v[j - 1] + v[j - 2])
        print(f"Fib({n}) = {v[len(v) - 1]}")
    else:
        print("Fib(0) = 0")