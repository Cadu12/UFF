vetor = [2.5, 7.5, 10.0, 4.0]
media = sum(vetor)/(len(vetor))

print(media)
for i in range(len(vetor)):
    if vetor[i] > media:
        print(f"Valor mais próximo da média: {vetor[i]}")
        break