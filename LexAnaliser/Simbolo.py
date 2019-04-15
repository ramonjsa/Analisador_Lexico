class Simbolo:
    lexema = ""
    token = ""
    tipo = ""
    def __init__(self,lexema,token,tipo):
        self.lexema = lexema
        self.token = token
        self.tipo = tipo

    def __repr__(self):
        return 'Simbolo({},{},{})'.format(self.lexema,
                                          self.token,
                                          self.tipo)
    def __repr__(self):
        return '({}\t|{}\t|{})'.format(self.lexema,
                                          self.token,
                                          self.tipo)


if __name__ == "__main__":
    simbolo = Simbolo("125", "digito", "-")
    print(simbolo)
    lista_de_simbolos = []
    lista_de_simbolos.append( Simbolo("125","digito","-"))
    lista_de_simbolos.append( Simbolo("1252", "digito", "-"))
    lista_de_simbolos.append( Simbolo("1225", "digito", "-"))
    print(lista_de_simbolos)
