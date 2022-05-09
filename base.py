#encoding=utf-8
import base64
def getMode():
    while True:
        print('请选择加密或解密')
        print('加密:encrypt(e)')
        print('解密:decrypt(d)')
        mode = input().lower()
        if mode in 'encrypt e decrypt d '.split():
            return mode
        else:
            print('请输入"encrypt"或"e"或"decrypt"或"d"!')
            
def getMessage():
    print('请输入你的信息：')
    return input()


def getType():
    typel = 0
    while True:
        print('请输入base类型(16或32或64)')
        typel = int(input())
        if (typel ==16 or typel ==32 or typel ==64):
            return typel


def base16_encrypt():
    print("base16加密结果: ", end="")
    print(base64.b16encode(message))

def base32_encrypt():
    print("base23加密结果: ", end="")
    print(base64.b32encode(message))

def base64_encrypt():
    print("base64加密结果: ", end="")
    print(base64.b64encode(message))

def base16_decrypt():
    print("base16解密结果: ", end="")
    print(base64.b16decode(message))

def base32_decrypt():
    print("base32解密结果: ", end="")
    print(base64.b32decode(message))

def base64_decrypt():
    print("base64解密结果: ", end="")
    print(base64.b64decode(message))


def getTranslatedMessage(mode, message, typel):
    if mode[0] == 'e':
        if typel == 16:
            base16_encrypt()
        elif typel ==32:
            base32_encrypt()
        elif typel ==64:
            base64_encrypt()
    else:
        if typel == 16:
            base16_decrypt()
        elif typel ==32:
            base32_decrypt()
        elif typel ==64:
            base64_decrypt()
        
 
mode = getMode()
message = str.encode(getMessage())
typel = getType()
getTranslatedMessage(mode, message, typel)










