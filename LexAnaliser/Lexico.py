from dfa import DFA
import os

lista_de_simbolos = {}
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
        global lista_de_simbolos
        self.dfa.reset()
        ultimo_estado = self.dfa.atual
        #while self.seek < os.path.getsize(self.caminho):
        while self.dfa.atual not in self.dfa.estados_de_rejeicao and self.seek <= os.path.getsize(self.caminho):
            c = self.fonte.read(1)
            self.seek += 1
            self.coluna += 1
            estado = self.dfa.processa_caracter(c)
            if estado not in self.dfa.estados_de_rejeicao :
                ultimo_estado = estado
                lexema +=c
                if c == '\n':
                    self.linha += 1
                    self.coluna = 0
            else:
                self.seek -= 1
                self.fonte.seek(self.seek)
                if self.coluna > 0:
                    self.coluna -= 1


                break
        if ultimo_estado not in self.dfa.estados_de_aceitacao :
            if ultimo_estado == self.dfa.estado_inicial and estado in self.dfa.estados_de_rejeicao:
                print(
                    'erro em ' + lexema+c + ' tipo ' + self.dfa.erros[self.dfa.estados[estado]] + " linha " + str(
                        self.linha) + " coluna " + str(self.coluna))
                return ('', self.dfa.erros[self.dfa.estados[estado]], '-')
            print('erro em ' + lexema + ' tipo ' + self.dfa.erros[self.dfa.estados[ultimo_estado]] + " linha " + str( self.linha) + " coluna " + str(self.coluna))
            return ('', self.dfa.erros[self.dfa.estados[ultimo_estado]],'-')
        lexema = lexema.lstrip()
        estado = self.dfa.processa_string(lexema)
        token = self.dfa.estados[estado]
        simbolo = (lexema, token, '-')
        if token != 'ID':
            print(simbolo)

        else :
            if lexema in lista_de_simbolos:
                lista = lista_de_simbolos[lexema].items()
                tupla = list(lista)
                print ("lexema presente na lista :("+lexema + "|\t"+str(tupla[0][0])+ "|\t"+str(tupla[0][1])+')')
                return (lexema,str(tupla[0][0]),str(tupla[0][1]))
                #print(lexema + lista_de_simbolos[lexema]+lista_de_simbolos[lexema][lista_de_simbolos[lexema]])
            else:
        #if lexema not in lista_de_simbolos:
                print("lexema acressentado a lista de simbolos  : ({} , {} , {})".format(lexema,token,'-'))
                lista_de_simbolos.update({lexema:{ token: '-'}})

        return simbolo


if __name__ == "__main__":

    f = open('../palavras_chave.txt', 'r')

    for linha in f:
        for palavra in linha.split():
            lista_de_simbolos.update({palavra: {palavra: '-'}})
    f.close()
    print('lexico')
    lexico = Lexico("../FONTE.ALG")



    simbolo = lexico.get_token()
    if simbolo[0] not in lista_de_simbolos:
        lista_de_simbolos.update({simbolo[0]: {simbolo[1]: simbolo[2]}})
        #print(simbolo)

    while simbolo[0] != '' :
        simbolo = lexico.get_token()
        #if simbolo[0] not in lista_de_simbolos:
            #lista_de_simbolos.update({simbolo[0]: {simbolo[1]: simbolo[2]}})
            #print(simbolo)

    print("lista de simbolos ao final do processamento")
    lista = sorted(lista_de_simbolos.items())
    for simbolo in lista:
        for token , tipo in simbolo[1].items():
            print(simbolo[0]+'|\t'+token+'|\t'+tipo)

    if 'se' in lista_de_simbolos:
        print('sim')
    else:
        print('nao')
