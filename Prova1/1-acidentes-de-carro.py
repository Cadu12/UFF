x1, y1, w1, h1 = [int(i) for i in input().split()]
x2, y2, w2, h2 = [int(i) for i in input().split()]
print(0 if w1 < x2 or w2 < x1 or h1 < y2 or h2 < y1 or x1 > w2 or x2 > w1 or y1 > h2 or y2 > h1 else 1)