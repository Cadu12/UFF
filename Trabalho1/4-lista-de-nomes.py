"""
1 - ENTRADA:
12
sergio
ana
maria
carlos
eva
joaquim
jo
mara
laura
lucas
ari
paulo

1 - SAIDA:
jo, ana, mara, maria, sergio, joaquim
eva, laura, carlos
ari, lucas
paulo
--------------------
2 - ENTRADA:
13
Alice
Miguel
Sophia
Helena
Heitor
Arthur
Bernardo
Valentina
Davi
Theo
Lorenzo
Isabella
Pedro

2 - SAIDA:
Davi, Alice, Miguel, Lorenzo, Bernardo, Valentina
Theo, Pedro, Sophia, Isabella
Helena
Heitor
Arthur
"""

def getNome():
    while True:
        pessoa = str(input())
        if pessoa.isalpha() and len(pessoa) >= 1 and len(pessoa) <= 19:
            return pessoa
        else:
            print("Nome: Cadeia de no mínimo 1 e no máximo 19 letras (maiúsculas, minúsculas e sem acentuação), sem espaço sem branco.")
            
n = int(input())
pessoas = []
for i in range(n):
    pessoas.append(getNome())
pessoas.sort(key = len)

listas = []
while True:
    if n == 0:
        break
    
    l = 0
    lista = []
    for i in range(n):
        l2 = len(pessoas[i])
        if l != l2:
            lista.append(pessoas[i])
            l = l2
    
    for i in lista:
        pessoas.remove(i)
        
    listas.append(lista)
    n -= len(lista)
    
for i in listas:
    print(", ".join(i))