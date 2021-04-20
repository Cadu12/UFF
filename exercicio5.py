vec = list(map(int, input().split()))
conta = {i:vec.count(i) for i in vec}

print(vec)
print(f"Diferentes: {conta}")
    