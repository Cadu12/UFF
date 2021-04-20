n = int(input())

for i in range(n):
    msg = ""
    frase = input()
    for j in range(len(frase)):
        if j == 0 and frase[j] != " ":
            msg += frase[j]
        else:
            try:
                if frase[j] == " " and frase[j + 1] != " " and ((ord(frase[j + 1]) >= 97 and ord(frase[j + 1]) <= 122)):
                    msg += frase[j + 1]
            except:
                pass                
    
    print(msg)