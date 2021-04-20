a, b, c = [float(i) for i in input().split()]

if a >= b and a >= c:
    maior = a
    meio = b
    menor = c
elif b >= a and b >= c:
    maior = b
    meio = a
    menor = c
else:
    maior = c
    meio = a
    menor = b
    
if maior >= meio + menor:
    print("NAO FORMA TRIANGULO")
else:
    if (maior ** 2 == meio ** 2 + menor ** 2):
        print("TRIANGULO RETANGULO")

    if maior ** 2 > meio ** 2 + menor ** 2:
        print("TRIANGULO OBTUSANGULO")
        
    if maior ** 2 < meio ** 2 + menor ** 2:
        print("TRIANGULO ACUTANGULO")
        
    if maior == meio and meio == menor and maior == menor:
        print("TRIANGULO EQUILATERO")

    if (maior == meio and maior != menor and menor != meio) or (meio == menor and maior != meio and maior != menor) or (maior == menor and menor != meio and maior != meio):
        print("TRIANGULO ISOSCELES")