# Exercise 12.10
# Ex1

import socket

url = input('Enter url: ')
try:
    hostname = url.strip().split('/')[2]
except:
    print('Improperly formatted URL')
    exit()

mysock = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
mysock.connect((hostname, 80))
cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()
mysock.send(cmd)

while True:
    data = mysock.recv(2048)
    if(len(data) < 1):
        break
    print(data.decode(), end='\n')

mysock.close()
