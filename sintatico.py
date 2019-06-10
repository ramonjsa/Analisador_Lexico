import csv
import sys
import re
from LexAnaliser.Simbolo import Simbolo
from LexAnaliser.Lexico import *
from collections import deque

def foo1():
    print('foo1')


def foo2():
    print('foo2')


def foo3():
    print('foo3')


def foo4():
    print('foo4')


def foo5():
    print('foo5')


def foo6():
    print('foo6')


def foo7():
    print('foo7')


def foo8():
    print('foo8')


def foo9():
    print('foo9')


def foo10():
    print('foo10')


def foo11():
    print('foo11')


def foo12():
    print('foo12')


def foo13():
    print('foo13')


def foo14():
    print('foo14')


def foo15():
    print('foo15')


def foo16():
    print('foo16')


def foo17():
    print('foo17')


def foo18():
    print('foo18')


def foo19():
    print('foo19')


def foo20():
    print('foo20')


def foo21():
    print('foo21')


def foo22():
    print('foo22')


def foo23():
    print('foo23')


def foo24():
    print('foo24')


def foo25():
    print('foo25')


def foo26():
    print('foo26')


def foo27():
    print('foo27')


def foo28():
    print('foo28')


def foo29():
    print('foo29')


def foo30():
    print('foo30')


def foo31():
    print('foo31')


def foo32():
    print('foo32')


def foo33():
    print('foo33')


def foo34():
    print('foo34')


def foo35():
    print('foo35')


def foo36():
    print('foo36')


def foo37():
    print('foo37')


def foo38():
    print('foo38')


funcoes = {1: foo1,
           2: foo2,
           3: foo3,
           4: foo4,
           5: foo5,
           6: foo6,
           7: foo7,
           8: foo8,
           9: foo9,
           10: foo10,
           11: foo11,
           12: foo12,
           13: foo13,
           14: foo14,
           15: foo15,
           16: foo16,
           17: foo17,
           18: foo18,
           19: foo19,
           20: foo20,
           21: foo21,
           22: foo22,
           23: foo23,
           24: foo24,
           25: foo25,
           26: foo26,
           27: foo27,
           28: foo28,
           29: foo29,
           30: foo30,
           31: foo31,
           32: foo32,
           33: foo33,
           34: foo34,
           35: foo35,
           36: foo36,
           37: foo37,
           38: foo38
           }









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
            funcoes.get(int(regra))()
        elif (sa.startswith('ACCEPT')):
            print("ACCEPT !!!!!!! compilou")
            break
        else:
            print("rotina de recuperacao de erro")
            break

if __name__ == "__main__":
    main()
