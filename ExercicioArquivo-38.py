import os
dir: str = ''
arq: str = ''

def main():
    arquivoPermissao: str = '/tmp/exercicios/'
    os.chmod(arquivoPermissao, 0o744)

    n: int = 0
    cont: int = 0
    maiorNumero: int = 0
    menorNumero: int = 0

    n = int(input("Digite um número: "))
    maiorNumero = n
    menorNumero = n
    gravarNumero(n, cont)
    cont += 1

    while (cont != 5):
        n = int(input("Digite um número: "))
        gravarNumero(n, cont)
        maiorNumero, menorNumero = NumMaiorMenor(n, maiorNumero, menorNumero)
        cont += 1
    gravarResultado(maiorNumero, menorNumero)
    

def NumMaiorMenor(numero: int, maior: int, menor: int):
    if (numero > maior):
        maior = numero
    elif (numero < menor):
        menor = numero
    return(maior, menor)

def gravarNumero(numeroDigitado, contador):
    global dir
    global arq

    dir = '/tmp/exercicios/'
    arq = 'ex38.txt'
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    arquivo: str = ''

    linha = str(numeroDigitado) + "\n"

    if(os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        arquivo = dir + arq
        enc = 'utf-8'
        if (os.path.exists(arquivo)):
            if (contador == 0):
                tipo = 'w'
            else:
                tipo = 'a'
        with open (arquivo, tipo, encoding=enc) as file:
            file.write(linha)
    else:
        print('Diretorio invalido')

def gravarResultado(maiorNumero, menorNumero):
    global dir
    global arq

    dir = '/tmp/exercicios/'
    arq = 'ex38.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    arquivo: str = ''

    linha = "Maior número:" + str(maiorNumero) + " / Menor número:" + str(menorNumero) + "\n"

    if(os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        arquivo = dir + arq
        enc = 'utf-8'
        if (os.path.exists(arquivo)):
            tipo = 'a'
        with open (arquivo, tipo, encoding=enc) as file:
            file.write(linha)
    else:
        print('Diretorio invalido')

if (__name__ == "__main__"):
    main()
