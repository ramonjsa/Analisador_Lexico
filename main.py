import sys

from LexAnaliser.Simbolo import Simbolo

# populacao inicial da lista de simbolos
f = open('palavras_chave.txt', 'r')
lista_de_simbolos = []
for palavra in f:
    lista_de_simbolos.append(Simbolo("{}".format(palavra.rstrip("\r\n")), "{}".format(palavra.rstrip("\r\n")), "-"))
f.close()


def main():
    print(sys.argv[1])
    if len(sys.argv) > 1 :
        fonte = open(sys.argv[1], 'r')
        #print(''.join(fonte.read()))
    # imprime a lista de simbolos
    print("\n   lexema   |\t   token   |\t   tipo")
    for simbolo in lista_de_simbolos:
        print(simbolo)


if __name__ == "__main__":
    main()
