teste = 1

while True:
    participantes, rodadas = [(int(i)) for i in input().split()]
    if participantes == 0 or rodadas == 0:
        break
    
    part = [(int(i)) for i in input().split()]
    
    for i in range(rodadas):
        acoes = [(int(i)) for i in input().split()]
        npart = acoes[0]
        ordem = acoes[1]
        acoes = acoes[2:]
        
        posacao = 0
        for j in range(npart):
            acao = acoes[j]
            if acao == ordem:
                posacao += 1
            else:
                for k in range(posacao + 1, npart):
                    part[k - 1] = part[k]
    
    print("Teste", teste)
    print(part[0])
    print()
    teste += 1