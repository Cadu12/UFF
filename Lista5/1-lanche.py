tabela = [
    4.00,
    4.50,
    5.00,
    2.00,
    1.50
]

c, q = [int(i) for i in input().split()]
print(f"Total: R$ {tabela[c - 1] * q:.2f}")