teste = 1

while True:
    n, m = [int(i) for i in input().split()]
    if n == 0 or m == 0:
        break
    
    maior = -201
    menor = 201
    soma = 0
    temp = []
    
    for i in range(n):
        temp.append(int(input()))
    
    for i in range(n - (m - 1)):
        soma = 0
        for j in range(i, i + m):
            soma += temp[j]
        
        maior = max(soma, maior)
        menor = min(soma, menor)
    
    print("Teste", teste)
    print(menor // m, maior // m)
    print()
    teste += 1