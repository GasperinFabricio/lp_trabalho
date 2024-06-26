dicionario = {
    'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h',
    'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p',
    'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
    'Y': 'y', 'Z': 'z',
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
    'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
    'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
    'ã': 'a', 'õ': 'o',
    'ç': 'c',
    'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u',
    'Â': 'a', 'Ê': 'e', 'Î': 'i', 'Ô': 'o', 'Û': 'u',
    'À': 'a', 'È': 'e', 'Ì': 'i', 'Ò': 'o', 'Ù': 'u',
    'Ã': 'a', 'Õ': 'o',
    'Ç': 'c',
    'ñ': 'n', 'Ñ': 'n',
    'ª': '', 'º': '', '°': '',
    '´': '', '`': '',
    '¨': '', '^': '',
    '~': '',
    '¿': '', '¡': '',
    '§': '', '®': '', '©': '', '™': '',
    '¹': '', '²': '', '³': '', '⁴': '', '⁵': '', '⁶': '', '⁷': '', '⁸': '', '⁹': '', '⁰': '',
    '¼': '', '½': '', '¾': '', '⅐': '', '⅑': '', '⅒': '', '⅓': '', '⅔': '', '⅕': '', '⅖': '',
    '⅗': '', '⅘': '', '⅙': '', '⅚': '', '⅛': '', '⅜': '', '⅝': '', '⅞': '', '⅟': '',
    '¬': '', '¦': '', '¶': '', 'µ': '', '£': '', '$': '', '¢': '', '€': '',
    '«': '', '»': '', '“': '', '”': '', '‘': '', '’': '', '‛': '', '‚': '',
    '„': '', '‟': '', '†': '', '‡': '', '•': '', '‣': '', '․': '', '‥': '',
    '…': '', '‰': '', '‱': '', '′': '', '″': '', '‴': '', '‵': '', '‶': '',
    '‷': '', '‸': '', '‹': '', '›': '', '※': '', '‼': '', '‽': '',
    '⁇': '', '⁈': '', '⁉': '', '⁑': '', '⁒': '',
    '⁓': '', '⁒': '', ' ': '',
    '₠': '', '₡': '', '₢': '', '₣': '', '₤': '', '₥': '', '₦': '', '₧': '', '₨': '',
    '₩': '', '₪': '', '₫': '', '€': '', '₭': '', '₮': '', '₯': '', '₰': '', '₱': '',
    '₲': '', '₳': '', '₴': '', '₵': '', '₶': '', '₷': '', '₸': '', '₹': '', '₺': '',
    '₻': '', '₼': '', '₽': '', '₾': '',
    '℀': '', '℁': '', 'ℂ': '', '℃': '', '℄': '', '℅': '', '℆': '', 'ℇ': '', '℈': '',
    '℉': '', 'ℊ': '', 'ℋ': '', 'ℌ': '', 'ℍ': '', 'ℎ': '', 'ℏ': '', 'ℐ': '', 'ℑ': '',
    'ℒ': '', 'ℓ': '', '℔': '', 'ℕ': '', '№': '', '℗': '', '℘': '', 'ℙ': '', 'ℚ': '',
    'ℛ': '', 'ℜ': '', 'ℝ': '', '℞': '', '℟': '', '℠': '', '℡': '', '™': '', '℣': '',
    'ℤ': '', '℥': '', 'Ω': '', '℧': '', 'ℨ': '', '℩': '', 'K': '', 'Å': '', 'ℬ': '',
    'ℭ': '', '℮': '', 'ℯ': '', 'ℰ': '', 'ℱ': '', 'Ⅎ': '', 'ℳ': '', 'ℴ': '', 'ℵ': '',
    'ℶ': '', 'ℷ': '', 'ℸ': '', 'ℹ': '', '℺': '', '℻': '', 'ℼ': '', 'ℽ': '', 'ℾ': '',
    'ℿ': '', '⅀': '', '⅁': '', '⅂': '',
    '0': '', '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '',
    ',': '', '.': '', ':': '', ';': '', '!': '', '?': '', '-': '', '_': '', '(': '', ')': '',
    '[': '', ']': '', '{': '', '}': '', '"': '', "'": '', '<': '', '>': '', '/': '', '\\': '',
    '|': '', '@': '', '#': '', '%': '', '&': '', '*': '', '+': '', '=': '', '~': '','\n':' ',',':''

}

def troca_char(char):
    if char in dicionario: 
        return dicionario[char]
    else:
        return False
