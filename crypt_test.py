import datetime

# Alfabetos
alfab1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfab2 = 'abcdefghijklmnopqrstuvwxyz'

#
# Substituição simples
#
def substitution1(lista, alt):
    result = []
    map1 = {}
    map2 = {}
    if (alt == 'atbash'):
        # Espelhamento (atbash)
        map1 = dict(zip(alfab1, alfab1[::-1]))
        map2 = dict(zip(alfab2, alfab2[::-1]))
    else:
        # Rotação (caesar)
        shift = list(alfab1[alt:]) + list(alfab1[:alt])
        map1 = dict(zip(alfab1, shift))
        shift = list(alfab2[alt:]) + list(alfab2[:alt])
        map2 = dict(zip(alfab2, shift))
    # Realização das substituições através dos dicionários
    for i, char in enumerate(lista):
        if char in list(alfab1):
            result.append(map1[char])
        elif char in list(alfab2):
            result.append(map2[char])
        else:
            result.append(char)
    return result

#
# Substituição polialfabética
#
def substitution2(lista, key, s):
    result = []
    for i, char in enumerate(lista):
        # Simulação da criptografia via tabela
        if (char in list(alfab1)):
            result.append((list(alfab1).index(char) + (list(alfab1).index(key[i])) * s) % len(list(alfab1)))
        elif (char in list(alfab2)):
            result.append((list(alfab2).index(char) + (list(alfab2).index(key[i])) * s) % len(list(alfab2)))
        else:
            result.append(-1)
        # Diferenciação entre maiúsculas e minúsculas
        if (result[i] != -1):
            if (char.isupper()):
                result[i] = list(alfab1)[result[i]]
            if (char.islower()):
                result[i] = list(alfab2)[result[i]]
        else:
            result[i] = lista[i]
    return result

#
# Cifras:
# - Atbash (subst. simples)
# - César (subst. simples)
# - Vigenère (subst. polialfabética) 
#
def atbash(args):
    print('> [atbash]')
    texto = ''.join(substitution1(list(leitura()), 'atbash'))
    dump(texto)

def caesar(args):
    print('> [caesar]')
    op = 0
    if (args[0] == 'ENCRYPT'):
        op = int(args[2])
    if (args[0] == 'DECRYPT'):
        op = int(args[2]) * -1
    texto = ''.join(substitution1(list(leitura()), op))
    dump(texto)

def vigenere(args):
    print('> [vigenere]')
    op = 0
    if (args[0] == 'ENCRYPT'):
        op = 1
    if (args[0] == 'DECRYPT'):
        op = -1
    chave = []
    args[2] = args[2].lower()
    for i, char in enumerate(list(leitura())):
        # Caractere permanece caso não pertença aos alfabetos
        if (not (char in list(alfab1) or char in list(alfab2))):
            chave.insert(i, char)
        chave.append(args[2][i % (len(args[2]))])
        # Diferenciação entre maiúsculas e minúsculas
        if (char.isupper()):
            chave[i] = chave[i].upper()
        if (char.islower()):
            chave[i] = chave[i].lower()
        # Garantia de que os arrays terão o mesmo tamanho
        if (len(chave) == len(list(leitura()))):
            break
    texto = ''.join(substitution2(list(leitura()), chave, op))
    dump(texto)

#
# Verificações de entrada
#
def verif_1(args):
    # Checagem arg.1
    if (args[0] == 'ENCRYPT' or args[0] == 'DECRYPT'):
        verif_2(args)
    else:
        print('!> erro: arg.1 invalido [ENCRYPT/DECRYPT]')

def verif_2(args):
    # Checagem arg.2
    alg = 0
    try:
        if (int(args[1]) > 0 and int(args[1]) < 4):
            alg = int(args[1])
        else:
            print('!> erro: arg.2 invalido [numero fora do limite 1-3]')
    except:
        print('!> erro: arg.2 invalido [precisa ser um numero]')
    # Checagem arg.3
    if (alg == 1):
        atbash(args)
    elif (alg == 2):
        verif_3c(args)
    elif (alg == 3):
        verif_3v(args)

def verif_3c(args):
    # Checagem arg.3 (Caesar)
    alg = 0
    try:
        if (int(args[2]) > 0 and int(args[2]) < 26):
            alg = int(args[2])
        else:
            print('!> erro: arg.3 invalido [numero fora do limite 1-25]')
    except:
        print('!> erro: arg.3 invalido [precisa ser um numero]')
    # Chamada do método sem retorno de exceção posterior
    if (alg != 0):
        caesar(args)

def verif_3v(args):
    # Checagem arg.3 (Vigenere)
    flag = False
    try:
        if (args[2].isalpha()):
            flag = True
        else:
            print('!> erro: arg.3 invalido [somente letras]')
    except IndexError:
        print('!> erro: arg.3 inexistente')
    # Chamada do método sem retorno de exceção posterior
    if (flag):
        vigenere(args)

#
# Funções de entrada e saída
#
def leitura():
    try:
        # Leitura do arquivo text.txt
        f = open("text.txt", "r", encoding="utf8")
        file_lines = ''
        for line in f:
            file_lines += line
        f.close()
        return file_lines    
    except FileNotFoundError:
        # Disparo de exceção
        print('!> erro: arquivo "text.txt" nao encontrado')
        return None

def dump(out):
    # Criação do dumpfile
    now = datetime.datetime.now()
    n2 = now.strftime("%Y%m%d%H%M%S") + ".txt"
    dumpfile = open(n2.strip(), "w")
    # Escrita no dumpfile
    dumpfile.write(out)
    dumpfile.close()
    print('> salvo no arquivo: ', n2)

#
# Função principal
#
def main():
    if (leitura() != None):
        # Argumentos de entrada
        args = input('> comando: ').split(' ')
        verif_1(args)

main()
