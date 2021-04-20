from random import randint

linhas = []
for i in range(8):
    linha = []
    for j in range(8):
        linha.append(randint(0, 9))
    linhas.append(linha)
    print(linha)

print(sum(map(sum, linhas)))