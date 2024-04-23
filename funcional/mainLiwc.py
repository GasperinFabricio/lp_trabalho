#Linguagem Estrututrada

from tabela import troca_char
import liwc

parse = liwc.load_token_parser("./LIWC2007_Portugues_win.dic")

with open("texto.txt","r", encoding='utf-8') as arquivo: #Ler arquivo txt
    texto=arquivo.read()

#Limpeza do texto
novo_texto=""

for l in texto:
    if troca_char(l) !=False:
        novo_texto+=troca_char(l) #função do modulo 'tabela' para trocar os caracteres
    else:
        novo_texto+=l

novo_texto = novo_texto.split(' ') #Divisão das palavras por espaço e convertendo em lista


#verificar a quantidade de palavras ofensivas, de ansiedade, positivas e negativas
swear,anx,posemo, negemo= 0,0,0,0

for p in novo_texto:
    resp = list(parse(p))
    
    if resp!=[]: #Verifica se a palavra existe no liwc
        if "swear" in resp:
            swear+=1
        if "anx" in resp:
            anx+=1
        if "posemo" in resp:
            posemo+=1
        if "negemo" in resp:
            negemo+=1

posemo = round((posemo/len(novo_texto))*100,2)
negemo = round((negemo/len(novo_texto))*100,2)

print('\n\n')
print(novo_texto)
print('\n')
print(f'Total de palavras: {len(novo_texto)}')
print(f'Palavras ofensivas: {swear}')
print(f'Palavras de ansiedade: {anx}')
print(f'Tom geral negativo: {negemo}%')
print(f'Tom geral positivo: {posemo}%')

