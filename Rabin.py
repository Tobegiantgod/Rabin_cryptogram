# encoding: utf-8
import random,math

#素数判定函数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#秘钥生成函数
def Rabin_getkeys():
    private_keys=[i for i in range(100,10000) if isPrime(i) and i%4==3]
    first_private_key=random.choice(private_keys)
    second_private_key=random.choice(private_keys)
    publice_key=first_private_key*second_private_key
    keys=[first_private_key,second_private_key,publice_key]
    return keys

#加密函数
def Rabin_encode(message,puk):
    plaintext=message
    ciphertext=[]
    public_keys=puk
    #public_keys=Rabin_getkeys()[-1]
    for i in plaintext:
        ciphertext.append(str(hash(str(ord(i)))))
        ciphertext.append(str((ord(i)+100)*(ord(i)+100)%public_keys))
    return ciphertext

#解密函数
def Rabin_decode(message,fk,sk):
    ciphertext=message
    plaintext=[]
    p=fk
    q=sk
    #keys=Rabin_getkeys()
    #p=keys[0]
    #q=keys[1]
    temp=0
    for i in range(p):
        if (i*q)%p==1:
            temp=i
            break
    a=q*temp
    temp=0
    for i in range(q):
        if (i*p)%q==1:
            temp=i
            break
    b=p*temp
    for i in range(len(ciphertext)):
        if i%2==1:
            m_temp=[]
            m=[]
            m_temp.append(pow(int(ciphertext[i]),(p+1)/4)%p)
            m_temp.append(p-pow(int(ciphertext[i]),(p+1)/4)%p)
            m_temp.append(pow(int(ciphertext[i]),(q+1)/4)%q)
            m_temp.append(q-pow(int(ciphertext[i]),(q+1)/4)%q)
            m.append((a*m_temp[0]+b*m_temp[2])%(p*q)-100)
            m.append((a*m_temp[0]+b*m_temp[3])%(p*q)-100)
            m.append((a*m_temp[1]+b*m_temp[2])%(p*q)-100)
            m.append((a*m_temp[1]+b*m_temp[3])%(p*q)-100)
            for each_m in m:
                if hash(str(each_m))==int(ciphertext[i-1]):
                    plaintext.append(chr(each_m))
    return ''.join(plaintext)

if __name__=='__main__':
    keys=Rabin_getkeys()
    print keys  #打印公钥与私钥，前两位为私钥用于解密，最后一位为公钥，用于加密
    print Rabin_encode('hello,world',keys[-1]) #打印加密结果
    print Rabin_decode(Rabin_encode('hello,world',keys[-1]),keys[0],keys[1])  #打印解密结果
