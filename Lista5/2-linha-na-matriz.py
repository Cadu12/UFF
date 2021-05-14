linha = int(input())
operacao = input()
matriz = [[] for i in range(12)]

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input()))

soma = 0
for i in matriz[linha]:
    soma = soma + i

print(f"{soma:.1f}" if operacao == "S" else f"{soma / 12:.1f}")