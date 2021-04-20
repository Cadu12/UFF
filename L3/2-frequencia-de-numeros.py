v = {}
for i in range(int(input())):
    n = int(input())
    if n in v:
        v[n] += 1
    else:
        v[n] = 1
        
for i in sorted(v.items()):
    print(f"{i[0]} aparece {i[1]} vez(es)")