n = int(input())
par = []
imp = []

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)
        
par.sort()
imp.sort(reverse = True)
        
for i in (par, imp):
    for j in i:
        print(j)