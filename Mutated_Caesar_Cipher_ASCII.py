# Caesar Cipher --ASCII
# 建立在ASCII编码表里第32位到126位编码的变异凯撒

def getMode():
    while True:
        print('请选择加密或解密模式,或者选择暴力破解：')
        print('加密:encrypt(e)')
        print('解密:decrypt(d)')
        print('暴力破解:brute(b)')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('请输入"encrypt"或"e"或"decrypt"或"d"或"brute"或"b"!')

def getMessage():
    print('请输入你的信息：')
    return input()

def getKey():
    key = 0
    while True:
        print('请输入密钥数字(1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >=1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for i in  range(len(message)):
        symbol = message[i]
        num = ord(symbol)+ key
        if num > 126:
            num -= 95
        elif num < 32:
            num += 95
        translated += chr(num)
    return translated
while __name__ ==    '__main__':
    mode = getMode()
    message = getMessage()
    if mode[0] != 'b':
        key = getKey()

    while __name__ ==    '__main__':
        print('你要翻译的信息是:')
        if mode[0] != 'b':
            print(getTranslatedMessage(mode, message, key))
        else:
            for key in range(1, MAX_KEY_SIZE + 1):
                print(key, getTranslatedMessage('decrypt', message, key))
