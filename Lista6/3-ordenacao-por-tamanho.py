n = int(input())
for _ in range(n):
    strs = input().split()
    strs.sort(key = len, reverse = True)
    print(" ".join(strs))