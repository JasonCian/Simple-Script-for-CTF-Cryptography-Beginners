#MORSE
encrypt = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.','f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---','k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---','p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-','u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..','A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.','F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-','L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-','R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--','X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}
decrypt = dict(zip(encrypt.values(), encrypt.keys()))
def getMode():
    while True:
        print('请选择加密或解密模式：')
        print('加密:encrypt(e)')
        print('解密:decrypt(d)')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('请输入"encrypt"或"e"或"decrypt"或"d"!')

def getMessage():
    print('请输入你的信息(解密时请用空格区分不同字符)：')
    return input()

def getTranslatedMessage(mode, message):
    translated = ''
    if mode[0] == 'e' :
        lists = message
        for code in lists:
            translated = translated +' '+ (encrypt.get(code))
        return translated
    else:
        lists = message.split(" ")
        for code in lists:
            translated = translated +' '+ (decrypt.get(code))
        return translated
        
while __name__ ==    '__main__':
    mode = getMode()
    message = getMessage()
    print('你要翻译的信息是:')
    print(getTranslatedMessage(mode, message), end=" ")
