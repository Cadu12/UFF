lista = [['Brasil', 'Italia', [10,9]], ['Brasil', 'Espanha', [5, 7]], ['Italia','Espanha', [7,8]]]
listas = {}
total = 0

for i in range(len(lista)):
    for j in range(2):
        if lista[i][j] not in listas:
            listas[lista[i][j]] = lista[i][2][j]
        else:
            listas[lista[i][j]] += lista[i][2][j]
            
        total += lista[i][2][j]

print(f"Total: {total}")
print(f"Menor: {min(listas)}")
print(f"Maior: {max(listas)}")