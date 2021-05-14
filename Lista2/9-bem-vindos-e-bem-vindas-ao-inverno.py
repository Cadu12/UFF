a, b, c = [int(i) for i in input().split()]

if a > b and b <= c:
    print(":)")
elif a < b and b >= c:
    print(":(")
elif a < b and b < c and (b - a) > (c - b):
    print(":(")
elif a < b and b < c and (b - a) <= (c - b):
    print(":)")
elif a > b and b > c and (b - c) < (a - b):
    print(":)")
elif a > b and b > c and (b - c) >= (a - b):
    print(":(")
elif a == b:
    if b < c:
        print(":)")
    else:
        print(":(")