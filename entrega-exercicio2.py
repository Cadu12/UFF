def getNome():
    while True:
        jogador = str(input())
        if jogador.isalpha() and len(jogador) >= 1 and len(jogador) <= 10:
            return jogador
        else:
            print("Nome: Cadeia de no mínimo um e no máximo dez letras (maiúsculas e minúsculas), sem espaço sem branco.")
            
def getDedos():
    while True:
        dados = int(input())
        if dados >= 0 and dados <= 5:
            return dados
        else:
            print("Dados: mínimo zero e no máximo cinco.")

jogos = 1
while True:
    partidas = int(input())
    if partidas == 0:
        break
    
    jogador1 = getNome()
    jogador2 = getNome()
    
    print(f"Teste {jogos}")
    for i in range(partidas):    
        a, b = [(int(i)) for i in input().split()]
        if (a + b) % 2 == 0:
            print(jogador1)
        else:
            print(jogador2)
    jogos += 1
    print()