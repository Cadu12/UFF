a, b, c = [float(i) for i in input().split()]
if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print(f"Perimetro = {a + b + c:.1f}")
else:
    print(f"Area = {(a + b) / 2 * c:.1f}")