

n = int(input())
instancia = 1
for _ in range(n):
    matriz = []
    solucao = True
    
    for i in range(9):
        matriz.append([int(j) for j in input().split()])
            
    for i in range(9):
        for j in range(9):
            print(i * 3, j * 3)
            
    print(matriz[0][1])

    print("Instancia", instancia)
    print("SIM" if solucao else "NAO")
    instancia += 1