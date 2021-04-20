print("Fibonacci: ")
vezes = int(input()) + 1

f1 = 0
f2 = 1
f3 = 0
fStr = None

while vezes != 0:
    if fStr is None:
        fStr = str(f1)
    else:
        fStr = fStr + ", " + str(f1)
        
    f3 = f1 + f2
    f2 = f1
    f1 = f3
    
    vezes = vezes - 1
    
print(fStr)