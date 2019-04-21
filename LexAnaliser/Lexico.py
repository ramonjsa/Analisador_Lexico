from LexAnaliser import Simbolo
from dfa import dfa
from dfa import DFA
class Lexico:
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

if __name__ == "__main__":
    f = open('../palavras_chave.txt', 'r')
    lista_de_simbolos = {}
    for palavra in f:
        lista_de_simbolos.update({palavra:{palavra:'-'}})
        #.append(Simbolo.Simbolo("{}".format(palavra.rstrip("\r\n")), "{}".format(palavra.rstrip("\r\n")), "-"))
    f.close()
    print(lista_de_simbolos)
    print('lexico')
    fonte = open("../FONTE.ALG", 'r')
    lexico = Lexico(fonte.read())
    #print(lexico.dfa.estados)
    #print(lexico.dfa.transicoes)
    #print(lexico.dfa.estados[lexico.dfa.processa_string('inicio')])
    #print(lexico.entrada)
    novo_simbolo = lexico.get_Token()
    print(novo_simbolo)
    #print(novo_simbololexema)
    if novo_simbolo not in lista_de_simbolos:
        lista_de_simbolos.update(novo_simbolo[])
    for simbolo in lista_de_simbolos:
        print(simbolo)