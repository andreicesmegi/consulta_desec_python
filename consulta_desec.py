#!/usr/share/python3

import socket
import sys

var = sys.argv[1]

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))
s.send((var + "\r\n").encode()) # Maneira 1 de concatenar textos e codifica-los para nao apresentar erro de 'str'
response1 = s.recv(1024).split()
target = response1[19].decode()
s.close()

s1 = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s1.connect((target,43))
s1.send((sys.argv[1] + "\r\n").encode()) # Maneira 2 de concatenar textos e codifica-los
response2 = s1.recv(1024).decode('iso-8859-1') # Adicionando esta iso, os resultados whois.registro.com passam a aparecer corretamente.
print = (response2)


