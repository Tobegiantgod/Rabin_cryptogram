from socket import *
from Rabin import *
HOST='192.168.134.129'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
      data=raw_input('> ')
      if not data:
          break
      udpCliSock.sendto(data,ADDR)
      public_key,ADDR=udpCliSock.recvfrom(BUFSIZ)
      if not public_key:
          break
      print '\nreceived publickey of',ADDR,'\nThe public_key is',public_key
      data=raw_input('\n>please input plaintext: ')
      ciphertext=Rabin_encode(data,int(public_key))
      ciphertext='!'.join(ciphertext)
      print '\nciphertext is :',ciphertext
      print '\nsend it to ',ADDR
      udpCliSock.sendto(ciphertext,ADDR)
      print '\ncompleted!'
udpCliSock.close()
