from random import randint

lista = []
lista2 = []

for i in range(10):
    lista.append(randint(1, 6))
    
for i in range(6):
    lista2.append(lista.count(i))
    
print(lista)
print(lista2)
    