from random import randint

vec = []
conta = 0

for i in range(50):
    rand = randint(1, 6)
    
    vec.append(rand)
    
    if rand == 6:
        conta += 1        
        
print((conta/50) * 100)