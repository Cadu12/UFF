y, z, v, w = [int(i) for i in input().split()]

resultado = -1

if y != z and v != w:
    inicio = y
    fim = v
    while inicio <= fim:
        if inicio % y == 0 and inicio % z != 0 and v % inicio == 0 and w % inicio != 0:
            resultado = inicio
            break
        inicio += y

print(resultado)