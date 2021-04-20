trilha = 0
trilha_menor = 0
menor = 2 ^ 32 - 1

primeiraVez = True

for i in range(int(input())):
    h = list(map(int, input().split()))

    m = h[0] - 1
    h = h[1:]
    esfotco_ida = 0
    esforco_volta = 0
    esforco_min = 0

    for i in range(m):
        j = h[i] - h[i + 1]
        if j < 0:
            esforco_volta = esforco_volta + abs(j)
        else:
            esfotco_ida = esfotco_ida + j

    esforco_min = min(esfotco_ida, esforco_volta)
     
    if menor > esforco_min:
        menor = esforco_min
        trilha = i + 1
        
        print("encontrado: ")
        print(menor)
        print(trilha)
        print("------")
        
    print(esfotco_ida)
    print(esforco_volta)
    print(esforco_min)
    print("#######################")

print("---FINAL---")
print(trilha)
print(menor)