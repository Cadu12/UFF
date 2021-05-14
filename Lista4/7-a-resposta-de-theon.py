n = int(input())
p = [int(i) for i in input().split()]
menor = 20
posicao = 1
for i in range(n):
    if p[i] < menor:
        menor = p[i]
        posicao = i + 1
print(posicao)