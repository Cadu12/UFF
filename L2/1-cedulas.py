valor = int(input())
print(valor)

troco = valor

print(int(troco // 100), "nota(s) de R$ 100,00")
troco -= (troco // 100) * 100

print(int(troco // 50), "nota(s) de R$ 50,00")
troco -= (troco // 50) * 50

print(int(troco // 20), "nota(s) de R$ 20,00")
troco -= (troco // 20) * 20

print(int(troco // 10), "nota(s) de R$ 10,00")
troco -= (troco // 10) * 10

print(int(troco // 5), "nota(s) de R$ 5,00")
troco -= (troco // 5) * 5

print(int(troco // 2), "nota(s) de R$ 2,00")
troco -= (troco // 2) * 2

print(int(troco // 1), "nota(s) de R$ 1,00")
troco -= (troco // 1) * 1