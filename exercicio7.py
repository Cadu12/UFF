from random import randint

vec = []
pos = []

for i in range(20):
    rand = randint(-10, 10)
    vec.append(rand)
    if rand > 0:
        pos.append(rand)

print(vec)
print(pos)
print(list(set(pos)))