# Caesar Cipher Rabbit
# 基于斐波那契数列为偏移码的变异凯撒
MAX_KEY_SIZE = 26

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

def getfbnq(message):
    fbnq = [1,1]
    a = 1
    b = 1
    while True:
        for i in range(3,len(message)+1):
            count=a+b
            fbnq.append(count)
            a,b=b,count
        print('斐波那契序列密钥已载入:{}'.format(fbnq))
        return fbnq


def getTranslatedMessage(mode, message,fbnq):
    if mode[0] == 'd':
        for i in  range(len(message)):
            fbnq[i] = -fbnq[i]
    translated = ''
    for i in  range(len(message)):
        symbol = message[i]
        if symbol.isalpha():
            key = fbnq[i] % 26
            num = ord(symbol)+ key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

while __name__ ==    '__main__':
    mode = getMode()
    message = getMessage()
    if mode[0] != 'b':
        fbnq = getfbnq(message)

    print('你要翻译的信息是:')
    if mode[0] != 'b':
        print(getTranslatedMessage(mode, message,fbnq))
    else:
        print("此种凯撒变异无需爆破")
