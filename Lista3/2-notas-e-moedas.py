valor = float(input())
troco = valor

print("NOTAS:")
print(int(troco / 100), "nota(s) de R$ 100.00")
troco -= int(troco / 100) * 100

print(int(troco / 50), "nota(s) de R$ 50.00")
troco -= int(troco / 50) * 50

print(int(troco / 20), "nota(s) de R$ 20.00")
troco -= int(troco / 20) * 20

print(int(troco / 10), "nota(s) de R$ 10.00")
troco -= int(troco / 10) * 10

print(int(troco / 5), "nota(s) de R$ 5.00")
troco -= int(troco / 5) * 5

print(int(troco / 2), "nota(s) de R$ 2.00")
troco -= int(troco / 2) * 2

print("MOEDAS:")
troco = round(troco, 2)
print(int(troco / 1), "moeda(s) de R$ 1.00")
troco -= int(troco / 1) * 1

troco = round(troco, 2)
print(int(troco / 0.5), "moeda(s) de R$ 0.50")
troco -= int(troco / 0.5) * 0.5

troco = round(troco, 2)
print(int(troco / 0.25), "moeda(s) de R$ 0.25")
troco -= int(troco / 0.25) * 0.25

troco = round(troco, 2)
print(int(troco / 0.10), "moeda(s) de R$ 0.10")
troco -= int(troco / 0.10) * 0.10

troco = round(troco, 2)
print(int(troco / 0.05), "moeda(s) de R$ 0.05")
troco -= int(troco / 0.05) * 0.05

troco = round(troco, 2)
print(int(troco / 0.01), "moeda(s) de R$ 0.01")
troco -= int(troco / 0.01) * 0.01

################################################################

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    qt_notas = int(valor / nota)
    print('{} nota(s) de R$ {:.2f}'.format(qt_notas, nota))
    valor -= qt_notas * nota

print('MOEDAS:')
for moeda in moedas:
    valor = round(valor, 2)
    qt_moedas = int(valor / moeda)
    print('{} moeda(s) de R$ {:.2f}'.format(qt_moedas, moeda))
    valor -= qt_moedas * moeda