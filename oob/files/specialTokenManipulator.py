from StringReader import StringReader
from tokenManipulator import TokenManipulator
from tabela import troca_char

class SpecialTokenManipulator(TokenManipulator):
    def __init__(self):
        super().__init__()

    def cleanerParser(self, string):
        for l in string:
            if troca_char(l) != False:
                string += troca_char(l)  # função do modulo 'tabela' para trocar os caracteres
            else:
                string += l

        return StringReader.cleanIt(string)  # Divisão das palavras por espaço e convertendo em lista