f1, f2, f3 = sorted([(int(i)) for i in input().split()])
vidro = 200
altura = 100

aberta = f1
    
if f3 < vidro * 2:
    aberta += vidro * 2 - f3

if f2 <= f1 + vidro:
    if f3 > f2 + vidro:
        aberta += f3 - (f2 + vidro)
else:
    aberta += f2 - (f1 + vidro)
    
print(aberta * altura)