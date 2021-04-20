operacao = input()
matriz = [[] for i in range(12)]

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input()))
        
soma = 0

c = 0
l = 5
r = 7
for i in range(7, 12):
    for j in range(l, r):
        soma += matriz[i][j]
    l -= 1
    r += 1
        
print(f"{soma:.1f}" if operacao == "S" else f"{soma / 12:.1f}")
