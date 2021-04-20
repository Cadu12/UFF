vector = []
for i in range(20):
    vector.append(int(input()))
vector.reverse()
for i in range(20):
    print(f"N[{i}] =", vector[i])