#Cryptography_tool_box
import sys
import Caesar_Cipher
import Mutated_Caesar_Cipher_ASCII
import Mutated_Caesar_Cipher_Rabbit
import base
import Rail_Fence_Cipher
import Morse

MAX_KEY_SIZE_1 = 26
MAX_KEY_SIZE_3 = 95

def GetToolMode():
    print('-------------------------------------------')
    print('请输入你需要使用的加解密工具：')
    print('(1)凯撒加密，解密和爆破')
    print('(2)基于ASCII的变异凯撒加密，解密和爆破')
    print('(3)基于斐波那契数列为偏移量的凯撒加密，解密')
    print('(4)base16,base32,base64的加密，解密')
    print('(5)栅栏密码的加密和解密')
    print('(6)MORSE密码的加密和解密')
    print('-------------------------------------------')
    return input()

def GetTool(toolmode):
    if toolmode == '1':
        mode = Caesar_Cipher.getMode()
        message = Caesar_Cipher.getMessage()
        if mode[0] != 'b':
            key = Caesar_Cipher.getKey()
        print('你要翻译的信息是:')
        if mode[0] != 'b':
            print(Caesar_Cipher.getTranslatedMessage(mode, message, key))
        else:
            for key in range(1, MAX_KEY_SIZE_1 + 1):
                print(key, Caesar_Cipher.getTranslatedMessage('decrypt', message, key))
        a = input("-------------------------------------------\n已运行完毕，输入back回到选择界面，\n或输入其他任意字符退出\n-------------------------------------------\n")
        if a == 'back':
            return
        else:
            sys.exit()
    elif toolmode == '2':
        mode = Mutated_Caesar_Cipher_ASCII.getMode()
        message = Mutated_Caesar_Cipher_ASCII.getMessage()
        if mode[0] != 'b':
            key = Mutated_Caesar_Cipher_ASCII.getKey()
        print('你要翻译的信息是:')
        if mode[0] != 'b':
            print(Mutated_Caesar_Cipher_ASCII.getTranslatedMessage(mode, message, key))
        else:
            for key in range(1, MAX_KEY_SIZE_3 + 1):
                print(key, Mutated_Caesar_Cipher_ASCII.getTranslatedMessage('decrypt', message, key))
    elif toolmode == '3':
        mode = Mutated_Caesar_Cipher_Rabbit.getMode()
        message = Mutated_Caesar_Cipher_Rabbit.getMessage()
        if mode[0] != 'b':
            fbnq = Mutated_Caesar_Cipher_Rabbit.getfbnq(message)
        print('你要翻译的信息是:')
        if mode[0] != 'b':
            print(Mutated_Caesar_Cipher_Rabbit.getTranslatedMessage(mode, message,fbnq))
        else:
            print("此种凯撒变异无需爆破")
    elif toolmode == '4':
        mode = base.getMode()
        message = str.encode(base.getMessage())
        typel = base.getType()
        base.getTranslatedMessage(mode, message, typel)
    elif toolmode == '5':
        mode = Rail_Fence_Cipher.getMode()
        if mode[0] == 'e':
            Rail_Fence_Cipher.Rail_Fence_Cipher_encrypt()
        if mode[0] == 'd':
            Rail_Fence_Cipher.Rail_Fence_Cipher_Decrypt()
    elif toolmode == '6':
        mode = Morse.getMode()
        message = Morse.getMessage()
        print('你要翻译的信息是:')
        print(Morse.getTranslatedMessage(mode, message), end=" ")

while __name__ ==    '__main__':
    toolmode = ''
    toolmode = GetToolMode()
    GetTool(toolmode)
