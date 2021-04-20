vec1 = list(map(int, input().split()))
vec2 = list(map(int, input().split()))

vec = []
for i in range(3):
    vec.append(vec1[i] + vec2[i])
    
print(f"x = {vec[0]}, y = {vec[1]}, z = {vec[2]}")