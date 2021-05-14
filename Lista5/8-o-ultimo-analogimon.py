while True:
    try:
        n, m = [int(i) for i in input().split()]
        matriz = []
        for i in range(n):
            matriz.append(input().split())
            
        a = []
        b = []
        
        for i in range(n):
            for j in range(m):
                pos = matriz[i][j]
                if pos == "2":
                    a = [i, j]
                elif pos == "1":
                    b = [i, j]
            
        x = abs(a[0] - b[0])
        y = abs(a[1] - b[1])
        print(x + y)
        
    except:
        break