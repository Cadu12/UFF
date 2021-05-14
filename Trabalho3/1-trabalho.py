def inputDeseja():
    print("Deseja:\n1 - Encriptar\n2 - Desencriptar")
    while True:
        escolha = input("Opção: ")
        if escolha == "1" or escolha == "2":
            return escolha
        else:
            print("Opção inválida.\nDeseja:\n1 - Encriptar\n2 - Desencriptar")
            
def inputSenha():
    print("Insira senha para encriptação: ")
    while True:
        senha = input().upper()
        if not senha:
            print("Senha inválida.")
        elif len(senha) != 5:
            print("Senha inválida.")
        elif senha.isalpha():
            letras = []
            isRepetida = False
            for i in senha:
                if i not in letras:
                    letras.append(i)
                else:
                    isRepetida = True
            
            if not isRepetida:
                return senha
            else:
                print("Senha inválida. Não pode ter letra repetida.")
        else:
            print("Senha inválida.")
            
def inputTexto():
    print("Insira texto: ")
    while True:
        texto = input().upper()
        if not texto:
            print("Texto inválido.")
        if len(texto) <= 100:
            return texto
        else:
            print("Texto inválido.")

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Z", " "]
def tabelaChave(senha):
    tabela = []
    maior = 0
    for i in range(5):
        tabela.append(letras.index(senha[i]) + 1)
        posicao = letras.index(senha[i]) + 2
        if maior < posicao:
            maior = posicao
        
    while True:
        if len(tabela) == 24:
            break
        
        if maior in tabela:
            maior += 1
            continue
        
        tabela.append(maior)
        maior += 1
        
        if maior == 25:
            maior = 1
            
    return tabela
    
def encriptar(senha, texto):
    encriptadoLetras = tabelaChave(senha)
    encriptado = ""
    for i in range(len(texto)):
        encriptado += letras[encriptadoLetras[letras.index(texto[i])] - 1]
        
    return encriptado

def desencriptar(senha, texto):
    desencriptadoLetras = tabelaChave(senha)
    desencriptado = ""    
    for i in range(len(texto)):
        desencriptado += letras[desencriptadoLetras.index(letras.index(texto[i]) + 1)]
    
    return desencriptado

deseja = inputDeseja()
senha = inputSenha()
texto = inputTexto()

if deseja == "1":
    print("Encriptado:", encriptar(senha, texto))
else:
    print("Desencriptado:", desencriptar(senha, texto))