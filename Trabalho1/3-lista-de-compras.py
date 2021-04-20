"""
ENTRADA:
2
carne laranja suco picles laranja picles
laranja pera laranja pera pera

SAIDA:
carne laranja picles suco
laranja pera
"""

def getNome(fruta):
    if fruta.isalpha() and fruta.islower() and len(fruta) >= 1 and len(fruta) <= 20:
        return fruta
    else:
        print("Nome: Cadeia de no mínimo 1 e no máximo 19 letras (maiúsculas, minúsculas e sem acentuação), sem espaço sem branco.")

n = int(input())
listas = []
for i in range(n):
    frutas = []
    for j in input().split():
        fruta = getNome(j)
        if fruta not in frutas:
            frutas.append(fruta)
            
    frutas.sort()
    listas.append(frutas)
    
for i in listas:
    print(" ".join(i))
        