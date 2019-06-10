class DFA:
    def __init__(self):
        #self.estados= {}
        #self.transicoes = {}
        self.estado_inicial = 0
        self.atual = self.estado_inicial
        self.estados = {-1: 'ERRO',
                   0: "ERRO_0",
                   1: "ERRO_1",
                   2: "ERRO_2",
                   3: "ERRO_3",
                   4: "ERRO_4",
                   5: "ERRO_5",
                   6: "NUM",
                   7: "NUM",
                   8: "NUM",
                   9: "ID",
                   10: "literal",
                   11: "OPM",
                   12: "EOF",
                   13: "OPR",#aqui estava o erro
                   14: "OPR",
                   15: "OPR",
                   16: "OPR",
                   17: "RCB",
                   18: "AB_P",
                   19: "FC_P",
                   20: "PT_V",
                   # (22, "COMENTARIO")
                   }
        self.estados_de_aceitacao=[ 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.estados_de_rejeicao=[-1]


        self.erros={'ERRO':'entrada invalida',
                   'ERRO_0':'entrada vasia',
                   'ERRO_1':'numero incompleto',
                   'ERRO_2': 'numero  incompleto',
                   'ERRO_3': 'numero incompleto',
                   'ERRO_4': 'literal incompleto',
                   'ERRO_5': ' comentario incompleto',
                   }
        self.transicoes = {
            0: {'\n': 0, '\t': 0, '\r': 0, ' ': 0, '0': 6, '1': 6, '2': 6, '3': 6, '4': 6, '5': 6, '6': 6, '7': 6,
                '8': 6,
                '9': 6, 'a': 9, 'b': 9, 'c': 9, 'd': 9, 'e': 9, 'f': 9, 'g': 9, 'h': 9, 'i': 9, 'j': 9, 'k': 9, 'l': 9,
                'm': 9, 'n': 9, 'o': 9, 'p': 9, 'q': 9, 'r': 9, 's': 9, 't': 9, 'u': 9, 'v': 9, 'w': 9, 'x': 9, 'y': 9,
                'z': 9, 'A': 9, 'B': 9, 'C': 9, 'D': 9, 'E': 9, 'F': 9, 'G': 9, 'H': 9, 'I': 9, 'J': 9, 'K': 9, 'L': 9,
                'M': 9, 'N': 9, 'O': 9, 'P': 9, 'Q': 9, 'R': 9, 'S': 9, 'T': 9, 'U': 9, 'V': 9, 'W': 9, 'X': 9, 'Y': 9,
                'Z': 9, '*': 11, '/': 11, '+': 11, '-': 11, '': 12, '"': 4, '{': 5, '<': 13, '>': 14, '=': 16, '(': 18,
                ')': 19, ';': 20},
            1: {'0': 7, '1': 7, '2': 7, '3': 7, '4': 7, '5': 7, '6': 7, '7': 7, '8': 7, '9': 7},
            2: {'0': 8, '1': 8, '2': 8, '3': 8, '4': 8, '5': 8, '6': 8, '7': 8, '8': 8, '9': 8, '+': 3, '-': 3},
            3: {'0': 8, '1': 8, '2': 8, '3': 8, '4': 8, '5': 8, '6': 8, '7': 8, '8': 8, '9': 8},
            4: {'"': 10,'\n': 4, '\t': 4, '\r': 4, ' ': 4, '0': 4, '1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4,
                '8': 4,
                '9': 4, 'a': 4, 'b': 4, 'c': 4, 'd': 4, 'e': 4, 'f': 4, 'g': 4, 'h': 4, 'i': 4, 'j': 4, 'k': 4, 'l': 4,
                'm': 4, 'n': 4, 'o': 4, 'p': 4, 'q': 4, 'r': 4, 's': 4, 't': 4, 'u': 4, 'v': 4, 'w': 4, 'x': 4, 'y': 4,
                'z': 4, 'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4, 'G': 4, 'H': 4, 'I': 4, 'J': 4, 'K': 4, 'L': 4,
                'M': 4, 'N': 4, 'O': 4, 'P': 4, 'Q': 4, 'R': 4, 'S': 4, 'T': 4, 'U': 4, 'V': 4, 'W': 4, 'X': 4, 'Y': 4,
                'Z': 4, '*': 4, '/': 4, '+': 4, '-': 4, '': 4,  '{': 4, '<': 4, '>': 4, '=': 4, '(': 4,
                ')': 4, ';': 4, ':': 4,'\\':4},
            5: {'}': 0},
            6: {'0': 6, '1': 6, '2': 6, '3': 6, '4': 6, '5': 6, '6': 6, '7': 6, '8': 6, '9': 6, '.': 1, 'E': 2},
            7: {'E': 2, '0': 7, '1': 7, '2': 7, '3': 7, '4': 7, '5': 7, '6': 7, '7': 7, '8': 7, '9': 7},
            8: {'0': 8, '1': 8, '2': 8, '3': 8, '4': 8, '5': 8, '6': 8, '7': 8, '8': 8, '9': 8},
            9: {'a': 9, 'b': 9, 'c': 9, 'd': 9, 'e': 9, 'f': 9, 'g': 9, 'h': 9, 'i': 9, 'j': 9, 'k': 9, 'l': 9, 'm': 9,
                'n': 9, 'o': 9, 'p': 9, 'q': 9, 'r': 9, 's': 9, 't': 9, 'u': 9, 'v': 9, 'w': 9, 'x': 9, 'y': 9, 'z': 9,
                'A': 9, 'B': 9, 'C': 9, 'D': 9, 'E': 9, 'F': 9, 'G': 9, 'H': 9, 'I': 9, 'J': 9, 'K': 9, 'L': 9, 'M': 9,
                'N': 9, 'O': 9, 'P': 9, 'Q': 9, 'R': 9, 'S': 9, 'T': 9, 'U': 9, 'V': 9, 'W': 9, 'X': 9, 'Y': 9, 'Z': 9,
                '0': 9, '1': 9, '2': 9, '3': 9, '4': 9, '5': 9, '6': 9, '7': 9, '8': 9, '9': 9, '_': 9},
            13: {'>': 15, '=': 15, '-': 17},
            14: {'=': 15},
        }




    def processa_string(self,entrada):
        atual = self.estado_inicial
        if entrada=='':
            return 12
        for c in entrada:

            if atual in self.transicoes:

                if c in self.transicoes[atual]:

                    atual = self.transicoes[atual][c]
                else:
                    return -1
            else:
                return  -1
        return atual

    def processa_caracter(self,entrada):
        if len(entrada)==0 and self.atual ==0:
            self.atual = 12
            return self.atual
        if self.atual in self.transicoes:
            if entrada in self.transicoes[self.atual]:
                self.atual = self.transicoes[self.atual][entrada]
            else:
                self.atual = -1
        else :
            self.atual = -1
        return self.atual

    def reset(self):
        self.atual = 0

    def incluir_estado(self,estado):
        self.estados.update(estado)
    def remover_estado(self,numero):
        del self.estados[numero]


    def incluir_transicao(self, origem, caracter, destino):
        if origem not in self.transicoes:
            self.transicoes.update({origem:{caracter:destino}})
        else:
            self.transicoes[origem].update({caracter:destino})


    def remover_transicao(self,origem,caracter):
        if origem in self.transicoes:
            self.transicoes[origem].pop(caracter)
       # print(len(self.transicoes[origem]))
        if len(self.transicoes[origem]) == 0 :
            self.transicoes.pop(origem)

if __name__ == "__main__":
    dfa = DFA()

    print(dfa.estados)
    #dfa.incluir_transicao(0,"0",0)
    print(dfa.transicoes)
    #dfa.remover_transicao(0,'0')
    print(dfa.transicoes)
    result = dfa.processa_string('"\\')
    if result:
        print (result)
    else:
        print("entrada invalida")


    print(dfa.estados[result])
    dfa.processa_caracter('"')
    print(dfa.atual)
    dfa.processa_caracter('\\')
    print(dfa.atual)
    dfa.processa_caracter('n')
    print(dfa.atual)