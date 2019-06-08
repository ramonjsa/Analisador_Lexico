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
                #print(a[a.__len__()-1])
    #print("30 OPRD ="+a[30]['OPRD'])
    return a
def regra_modulo():
    a = {}
    with open("regramod.csv") as myfile:
        for line in myfile:
            values = "".join(line.split()).split(',')

            a.update({values[0]: values[1]})

    return a
def regra_A():
    a = {}

    with open("regra_nao_terminal.csv") as myfile:
        for line in myfile:
            values = "".join(line.split()).split(',')
            a.update({values[0]: values[1]})
    return a

def producao():
    a = {}

    with open("producoes.csv") as myfile:
        for line in myfile:
            values = "".join(line.split()).split(',')
            a.update({values[0]: values[1]})
    return a

def main():
    f = open('palavras_chave.txt', 'r')

    for linha in f:
        for palavra in linha.split():
            lista_de_simbolos.update({palavra: {palavra: '-'}})
    f.close()
    print('analizador lexico e sintatico')


    lexico = Lexico("./FONTE2.ALG")

    acoes = tabela_de_acoes()
    modulo = regra_modulo()
    prod=producao()
    print(prod)
    #print (modulo['9'])
    nTerminal = regra_A()
    #print(modulo)
    pilha = deque()
    pilha.append(0)

    a = lexico.get_token()
    #print(pilha)
    print(a)

    while (True):

        s = pilha[pilha.__len__()-1]
        print("s ="+str(s))
        print("a = "+a[1])
        #print(acoes[int(s)])
        sa =str(acoes[int(s)][a[1]])
        print("sa ="+sa)

        if (sa.startswith('S(')):
            #t=re.A('\d+',sa)
            t=re.search('\d+',sa).group(0)
            print("t = "+t)
            pilha.append(t)
            a = lexico.get_token()
        elif(sa.startswith('R(')):
            regra = re.search('\d+',sa).group(0)
            print("regra"+str(regra))
            #todo desempilha modulo de beta da regra
            k=int(modulo[str(regra)])
            print("|B| ="+str(k))
            for i in range(0, k):
                pilha.pop()
            t = pilha[pilha.__len__()-1]
            print("t ="+str(t))
            A = nTerminal[regra]
            print("A = "+ A)
            gotoTA=str(acoes[int(t)][A])
            print("goto[ta] ="+gotoTA)
            pilha.append(gotoTA)
            print(prod.get(regra))
        elif (sa.startswith('ACCEPT')):
            print("ACCEPT !!!!!!! compilou")
            break
        else:
            print("rotina de recuperacao de erro")
            break

if __name__ == "__main__":
    main()
