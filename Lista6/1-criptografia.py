n = int(input())
for _ in range(n):
    linha = input()
    nova = ""
    for i in linha:
        ascii = ord(i)
        if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
            nova += chr(ascii + 3)
        else:
            nova += i
    nova = nova[::-1]
    crip = ""
    for i in range(len(nova)):
        if i > (len(nova) / 2) - 1:
            ascii = ord(nova[i])
            crip += chr(ascii - 1)
        else:
            crip += nova[i]
            
    print(crip)