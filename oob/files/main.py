import sys

import specialTokenManipulator
import tokenManipulator

sysCall = sys.argv
fileName = sysCall[1]

file = open("./" + fileName, encoding='utf-8')

text = file.read()

tokenManip = tokenManipulator.TokenManipulator
specialToken = specialTokenManipulator.SpecialTokenManipulator

tokenManip.calculateLIWC(specialToken.cleanerParser(text))


print(tokenManip.pontuacao())