chave = input()
codificada = input()

letras = "abcdefghijklmnopqrstuvwxyz"
decriptado = ""

for letra in codificada:
    for i in range(len(chave)):
        if letra == chave[i]:
            decriptado += letras[i]
            
print(decriptado)