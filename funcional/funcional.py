import collections
import sys
import re
import liwc

parse = liwc.load_token_parser("./LIWC2007_Portugues_win.dic")


#Declaração de subclasse tupla, imutável.
Texto = collections.namedtuple('Texto', [
    'texto'
])

Pontos = collections.namedtuple('Pontos',[
    'swear',
    'anx',
    'posemo',
    'negemo'
])


def clean_text(text):

    cleaned_text = re.sub(r'[/^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]+$/]', ' ', text)

    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    cleaned_text = re.sub(r',', '', text)

    cleaned_text = cleaned_text.lower()

    cleaned_text = cleaned_text.split()

    return cleaned_text


def parseTexto(texto, n, ponto):
    if n == 0:
        return ponto
    else:
        resp = list(parse(n))

        conditions = {
            "swear": "swear" in resp,
            "anx": "anx" in resp,
            "posemo": "posemo" in resp,
            "negemo": "negemo" in resp
        }

        filtered_conditions = filter(lambda condition: conditions[condition], conditions)

        def update_ponto(condition, ponto):
            if condition == "swear":
                return Pontos(swear=ponto.swear + 1, anx=ponto.anx, posemo=ponto.posemo, negemo=ponto.negemo)
            elif condition == "anx":
                return Pontos(swear=ponto.swear, anx=ponto.anx + 1, posemo=ponto.posemo, negemo=ponto.negemo)
            elif condition == "posemo":
                return Pontos(swear=ponto.swear, anx=ponto.anx, posemo=ponto.posemo + 1, negemo=ponto.negemo)
            elif condition == "negemo":
                return Pontos(swear=ponto.swear, anx=ponto.anx, posemo=ponto.posemo, negemo=ponto.negemo + 1)

        return parseTexto(texto, n - 1, update_ponto(next(filtered_conditions, None), ponto))

# def parseTexto(texto, n, ponto):
#     if(n == 0):
#         return ponto
#     else:
#         resp = list(parse(n))
#
#         if resp != []:  # Verifica se a palavra existe no liwc
#             if "swear" in resp:
#                 return parseTexto(texto, n - 1, Pontos(swear=ponto.swear + 1, anx=0, posemo=0, negemo=0))
#             if "anx" in resp:
#                 return parseTexto(texto, n - 1, Pontos(swear=0, anx=ponto.anx + 1, posemo=0, negemo=0))
#             if "posemo" in resp:
#                 return parseTexto(texto, n - 1, Pontos(swear=0, anx=0, posemo=ponto.posemo + 1, negemo=0))
#             if "negemo" in resp:
#                 return parseTexto(texto, n - 1, Pontos(swear=0, anx=0, posemo=0, negemo=ponto.negemo + 1))


sys_arg = sys.argv
textFile = open(sys.argv[1], "r", encoding='utf-8')

texto = Texto(texto=textFile.read())

pontuacao = parseTexto(clean_text(texto.texto), len(clean_text(texto.texto)), Pontos(0, 0, 0, 0))

print("Pontuação do texto: ", pontuacao)

