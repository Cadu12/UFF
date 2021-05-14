a, b = [int(i) for i in input().split()]
print("Sao Multiplos" if a == b or (a > b and a % b == 0) or (a < b and b % a == 0) else "Nao sao Multiplos")