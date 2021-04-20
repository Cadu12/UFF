teste = 1

while True:
    n, m = [int(i) for i in input().split()]
    if n == 0 or m == 0:
        break
    
    soma = 0
    temp = []
    
    for i in range(m):
        temp.append(int(input()))
        soma += temp[i]
    
    maior = soma
    menor = soma
    
    for i in range(m, n):
        temp.append(int(input()))
        soma = soma + temp[i] - temp[i - m]
        maior = max(soma, maior)
        menor = min(soma, menor)
    
    print(f"Teste {teste}\n{int(menor / m)} {int(maior / m)}\n")
    teste += 1