"""
ENTRADA:
2
3
ESQ
DIR
EXEC 2
5
ESQ
EXEC 1
EXEC 2
EXEC 1
EXEC 4

SAIDA:
1
-5
"""

n = int(input())
for i in range(n):
    x = 0
    c = int(input())
    linhas = []
    for j in range(c):
        comando = input().lower()
        comandoSplit = comando.split()
        linhas.append(comando)
        
        if comandoSplit[0] == "esq":
            x -= 1
        elif comandoSplit[0] == "dir":
            x += 1
        elif comandoSplit[0] == "exec":
            if len(linhas) <= 1:
                print("não tem linhas para exec")
            elif int(comandoSplit[1]) - 1 == j:
                print("não pode ser preso no loop")
            else:
                linha = linhas[int(comandoSplit[1]) - 1].split()
                while True:
                    if linha[0] == "esq":
                        x -= 1
                        break
                    elif linha[0] == "dir":
                        x += 1
                        break
                    else:
                        linha = linhas[int(linha[1]) - 1].split()
                            
    print(x)