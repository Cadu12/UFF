lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40, 50, 60]
lista_intercalada = []
lista_loop = 0

for i in range(len(lista1)):
    lista_intercalada.append(lista1[i])
    for j in range(len(lista2)):
        if str(lista1[i])[0] == str(lista2[j])[0]:
            lista_intercalada.append(lista2[j])
            lista_loop += 1
            
for i in range(len(lista2) - lista_loop):
    lista_intercalada.append(lista2[lista_loop+i])
    
print(lista_intercalada)