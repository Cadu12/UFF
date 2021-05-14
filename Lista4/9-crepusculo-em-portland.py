n = int(input())
q = []
for i in range(n + 1):
    q.append([int(i) for i in input().split()])
    
linhas = []
for i in range(n):
    linha = ""
    func = 0
    for j in range(n):
        quad = q[i][j : j + 2] + q[i + 1][j : j + 2]
        if sum(quad) >= 2:
            linha += "S"
        else:
            linha += "U"            
    linhas.append(linha)
                
print("\n".join(linhas))