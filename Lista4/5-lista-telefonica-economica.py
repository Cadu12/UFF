while True:
    try:
        n = int(input())
        v = []
        c = 0
        for i in range(n):
            t = str(input())
            v.append(t)

        v.sort()
        tel = v[0]
        
        for i in range(1, n):
            for j in range(len(v[i])):
                if tel[j] == v[i][j]:
                    c += 1
                else:
                    tel = v[i]
                    break
                
        print(c)
    except:
        break