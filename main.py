import sys

from LexAnaliser.Simbolo import Simbolo
from LexAnaliser.Lexico import *



def main():
    f = open('palavras_chave.txt', 'r')

    for linha in f:
        for palavra in linha.split():
            lista_de_simbolos.update({palavra: {palavra: '-'}})
    f.close()
    print('analizador lexico')
    lexico = Lexico("./FONTE.ALG")

    simbolo = lexico.get_token()
    while simbolo[0] != '':
        simbolo = lexico.get_token()
    print("tabela de simbolos ao final do processamento")
    print("lexema     \t|\t   token     \t|\ttipo")
    lista = sorted(lista_de_simbolos.items(), reverse=True)
    for simbolo in lista:
        for token, tipo in simbolo[1].items():
            print(simbolo[0] + '\t|\t' + token + '\t|\t' + tipo)


if __name__ == "__main__":
    main()
