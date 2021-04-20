teste = 1
while True:
    x1, y1, x2, y2 = [int(i) for i in input().split()]
    if x1 == y1 == x2 == y2 == 0:
        break
    
    n = int(input())
    c = 0
    
    if x2 > x1:
        x1, x2 = x2, x1
        
    if y2 > y1:
        y1, y2 = y2, y1
        
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        if (a >= x1 and a <= x2 and b >= y1 and b <= y2) or (a <= x1 and a >= x2 and b <= y1 and b >= y2):
            c += 1
            
    print(f"Teste {teste}\n{c}")
    teste += 1