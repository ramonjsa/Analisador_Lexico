from LexAnaliser import Simbolo
from dfa import dfa
from dfa import DFA
import os


class Lexico:
    def __init__(self, fonte):
        self.caminho = fonte
        self.fonte = open(fonte, 'r')

        self.dfa = DFA.DFA()
        self.linha = 0
        self.coluna = 0
        self.seek = 0

    def get_token(self):
        lexema = ''

        # print(self.fonte.__sizeof__())
        while self.seek < os.path.getsize(self.caminho):  # self.fonte.__sizeof__():
            # print (self.seek)
            c = self.fonte.read(1)
            # print (ord(c))
            self.seek += 1
            self.coluna += 1
            if self.dfa.processa_string(lexema +c) >= 0:
                lexema += c
                # print(ord(c))
                if c == '\n':
                    self.linha += 1
                    self.coluna = 0
            else:
                self.seek -= 1
                self.fonte.seek(self.seek)
                if self.coluna > 0: self.coluna -= 1
                break

        lexema = lexema.lstrip()
        estado = self.dfa.processa_string(lexema)
        token = self.dfa.estados[estado]
        simbolo = (lexema, token, '-')

        #print('{} linha {} coluna {}'.format(simbolo, self.linha, self.coluna))
        return (lexema, token, '-')

    '''
    def __init__(self,entrada):
        self.entrada=""
        self.entrada = entrada
        print(DFA)
        self.dfa = DFA.DFA()
        self.linha =0
        self.coluna=0
    
    def get_Token(self):
        inicio = self.coluna
        lexema = ''
        i=inicio
        while (self.entrada[i]!=' '):
            if self.entrada[i]== '\n':
                self.linha+=1

                break
            lexema=lexema + self.entrada[i]
            #print(lexema)
            i=i+1
        print(lexema)
        print(self.dfa.processa_string(lexema))
        estado = self.dfa.processa_string(lexema)
        print (self.dfa.atual)
        for c in lexema:
            self.dfa.processa_caracter(c)
        estado = self.dfa.atual
        print(estado)
        token = self.dfa.estados[self.dfa.processa_string(lexema)]
        #token = Simbolo.Simbolo(lexema,token,'-')
        token = {lexema:{token:'-'}}

        #token = "id"
        return token
    '''


if __name__ == "__main__":

    f = open('../palavras_chave.txt', 'r')
    lista_de_simbolos = {}
    for linha in f:
        for palavra in linha.split():
            lista_de_simbolos.update({palavra: {palavra: '-'}})
            #lista_de_simbolos.append((palavra,palavra,'-'))
        #.append(Simbolo.Simbolo("{}".format(palavra.rstrip("\r\n")), "{}".format(palavra.rstrip("\r\n")), "-"))
    f.close()
    # print(lista_de_simbolos)
    print('lexico')
    lexico = Lexico("../FONTE.ALG")

    simbolo = lexico.get_token()
    if simbolo[0] not in lista_de_simbolos:
        #lista_de_simbolos.append(simbolo)
        lista_de_simbolos.update({simbolo[0]: {simbolo[1]: simbolo[2]}})
        #print(simbolo)

    while simbolo[0] != '':
        # while lexico.seek < os.path.getsize(lexico.caminho):
        simbolo = lexico.get_token()
        if simbolo[0] not in lista_de_simbolos:
            #lista_de_simbolos.append(simbolo)
            lista_de_simbolos.update({simbolo[0]: {simbolo[1]: simbolo[2]}})
            #print(simbolo)

    # fonte = open("../FONTE.ALG", 'r')
    # lexico = Lexico(fonte.read())
    # print(lexico.dfa.estados)
    # print(lexico.dfa.transicoes)
    # print(lexico.dfa.estados[lexico.dfa.processa_string('inicio')])
    # print(lexico.entrada)
    # novo_simbolo = lexico.get_Token()
    # print(novo_simbolo)

    # print(novo_simbololexema)
    '''if novo_simbolo not in lista_de_simbolos:
        lista_de_simbolos.update(novo_simbolo[])
    '''
    print("lista de simbolos ao final do processamento")
    lista = sorted(lista_de_simbolos.items())
    for simbolo in lista:
        for token , tipo in simbolo[1].items():
            print(simbolo[0]+'|\t'+token+'|\t'+tipo)

    #print(lista_de_simbolos)
