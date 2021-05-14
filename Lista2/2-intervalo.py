n = float(input())
if n > 100 or n < 0:
    print("Fora de intervalo")
else:
    for i in range(4):
        if n >= i * 25 and n <= (i + 1) * 25:
            print("Intervalo", ("[" if i == 0 else "(") + str((i) * 25) + "," + str((i + 1) * 25) + "]")
            break