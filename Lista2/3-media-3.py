a, b, c, d = [float(i) for i in input().split()]
media = (a * 2 + b * 3 + c * 4 + d) / 10
print(f"Media: {media:.1f}",)
if media >= 7:
    print("Aluno aprovado.")
elif media >= 5 and media < 7:
    print("Aluno em exame.")
    mediaFinal = float(input())
    print("Nota do exame:", mediaFinal)
    media = (media + mediaFinal) / 2
    if media >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {media:.1f}")
    else:
        print("Aluno reprovado.")
else:
    print("Aluno reprovado.")