while True:
    n = int(input())
    if n <= 0:
        break
    
    if n == 1:
        print("1\n")
        continue
    
    padding = len(str(2 ** (n - 1 + n - 1)))
    for i in range(n):
        print(str(2 ** i).rjust(padding), end = " ")
        for j in range(n - 1):
            print(str(2 ** (i + j + 1)).rjust(padding), end = " " if j != n - 2 else "\n")
        
    print()