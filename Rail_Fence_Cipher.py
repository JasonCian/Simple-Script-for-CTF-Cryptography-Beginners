# Rail Fence Cipher encrypt
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

def Rail_Fence_Cipher_encrypt():
    message=input("请输入你的信息：")
    print('请输入栅栏行数(1-%s)' % (len(message)))
    key =int(input())
    translated = ''
    for j in range(key):
        for i in range(j,len(message),key):
            translated = translated + message[i]
    print(translated)


def Rail_Fence_Cipher_Decrypt():
    e =input('请输入要解密的字符串\n')
    elen = len(e) #计算字符串长度
    field=[]
    for i in range(2,elen): #做一个循环，从2开始到数字elen（字符串长度）
        if(elen%i==0): #计算哪些数字能整除字符串
            field.append(i) #将能整除的数字append到field里面
    for f in field:
        b = elen // f #用字符串长度除以上面计算出能整除的数字f
        result = {x:'' for x in range(b)} 
        for i in range(elen): #字符串有多少位，就循环多少次
            a = i % b;
            result.update({a:result[a] + e[i]}) #字符串截断，并update新数据
        d = ''
        for i in range(b):
            d = d + result[i]
        print ('分为'+str(f)+'栏时，解密结果为：  '+d+'\n') #输出结果，并开始下一个循环，直到循环结束

while __name__ ==    '__main__':
    mode = getMode()
    if mode[0] == 'e':
        Rail_Fence_Cipher_encrypt()
    if mode[0] == 'd':
        Rail_Fence_Cipher_Decrypt()