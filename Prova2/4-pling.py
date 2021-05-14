n = int(input())
cassinos = [int(i) for i in input().split()]
if len(cassinos) > n:
    cassinos = cassinos[:n]
    
numero = cassinos[0]
sequencia = 0
maior = 1

for i in cassinos:
    if i == numero:
        sequencia += 1
        
        if maior < sequencia:
            maior = sequencia
    else:
        if maior < sequencia:
            maior = sequencia
        
        numero = i
        sequencia = 1
        
print(maior)