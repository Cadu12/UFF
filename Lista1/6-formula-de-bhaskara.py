from math import sqrt
a, b, c = [float(i) for i in input().split()]
x = (b ** 2) - (4 * a * c)
if a <= 0:
    print("Impossivel calcular")
else:
    try:
        x = sqrt(x)
        r1 = (-b + x) / (2 * a)
        r2 = (-b - x) / (2 * a)
        print(f"R1 = {r1:.5f}\nR2 = {r2:.5f}")
    except:
        print("Impossivel calcular")