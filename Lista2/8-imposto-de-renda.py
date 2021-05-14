salario = float(input())

if salario <= 2000.0:
    print("Isento")
else:
    imposto = 0
    if salario <= 3000.0:
        imposto = (salario - 2000.0) * 0.08
    elif salario <= 4500.0:
        imposto = (salario - 3000.0) * 0.18 + (1000.0 * 0.08)
    else:
        imposto = (salario - 4500.0) * 0.28 + (1500.0 * 0.18) + (1000.0 * 0.08)
    
    print(f"R$ {imposto:.2f}")  