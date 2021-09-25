
import socket
import sys

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))
s.send (sys.argv[1]+"\r\n")
response1 = s.recv(1024).split()
target = response1[19]
s.close()
print (target)


s1 = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s1.connect((target,43))
s1.send (sys.argv[1]+"\r\n")
response2 = s1.recv(1024)
print = (response2)

