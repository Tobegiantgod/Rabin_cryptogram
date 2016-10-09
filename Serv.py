from socket import *
from time import ctime
from Rabin import *

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print '\nwaiting for message...'
    data,addr=udpSerSock.recvfrom(BUFSIZ)
    keys=Rabin_getkeys()
    udpSerSock.sendto(str(keys[-1]),addr)
    print '\nreceived from ',addr,'returned publickey ',keys[-1]
    ciphertext,addr=udpSerSock.recvfrom(BUFSIZ)
    print '\nreceived ciphertext: ',ciphertext
    cipher=ciphertext.split('!')
    plaintext=Rabin_decode(cipher,keys[0],keys[1])
    print '\ndecrypt it ,get the plaintext:',plaintext,'\ncompleted!'

udpSerSock.close()
