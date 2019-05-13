import csv
import sys
import re
from LexAnaliser.Simbolo import Simbolo
from LexAnaliser.Lexico import *
from collections import deque
def tabela_de_acoes():
    a = []
    with open("acoes.csv") as myfile:
        firstline = True
        for line in myfile:
            if firstline:
                mykeys = "".join(line.split()).split(',')
                firstline = False
            else:
                values = "".join(line.split()).split(',')
                a.append({mykeys[n]: values[n] for n in range(0, len(mykeys))})
    #print(a[77]['id'])
    return a


def main():
    f = open('palavras_chave.txt', 'r')

    for linha in f:
        for palavra in linha.split():
            lista_de_simbolos.update({palavra: {palavra: '-'}})
    f.close()
    print('analizador lexico e sintatico')


    lexico = Lexico("./FONTE.ALG")

    acoes = tabela_de_acoes()

    pilha = deque()
    pilha.append(0)
    a = lexico.get_token()
    print(a)
    while (True):
        s = pilha[pilha.__len__()-1]
        sa =str(acoes[s][a[1]])
        if (sa.startswith('S(')):
            t=re.A('\d+',sa)
            pilha.append(t)
            print(t)
        else if (sa.startswith('R(')) :
            regra = re.A('\d+', sa)
            #todo desempilha modulo de beta da regra
            t = pilha[pilha.__len__()-1]
            pilha.append(regra)
            #todo
            #todo


            print(regra)


if __name__ == "__main__":
    main()
