num = 0
comando = None
loop = True

print("Digite 'A', 'B', 'C', 'D', 'E' ou 'X' para entrar com um comando: ")

while loop:
    comando = input().upper()
    if comando == "A":
        num = 10
    elif comando == "B":
        num -= 1
    elif comando == "C":
        num -= 2
    elif comando == "D":
        num += 1
    elif comando == "E":
        print("Numero: " + str(num))
    elif comando == "X":
        loop = False
    else:
        print("Comando desconhecido!")
