h = list(map(int, input().split()))
print(h)

m = h[0] - 1
h = h[1:]
esfotco_ida = 0
esforco_volta = 0
esforco_min = 0

for i in range(m):
    j = h[i] - h[i + 1]
    if j < 0:
        esforco_volta = esforco_volta + abs(j)
    else:
        esfotco_ida = esfotco_ida + j

esforco_min = min(esfotco_ida, esforco_volta)    

print(esfotco_ida)
print(esforco_volta)
print(esforco_min)