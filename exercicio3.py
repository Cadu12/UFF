dStr = None
vezes = 0

num = int(input("Numero: "))

n = 0
while n <= num:
    n = n + 1
    if num % n == 0:
        vezes = vezes + 1
        if dStr is None:
            dStr = str(n)
        else:
            dStr = dStr + ", " + str(n)

if vezes == 1:
    print("Primo")
else:
    print(str(vezes) + " divisores: ")
    print(dStr)