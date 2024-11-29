import socket

ip = ("10.0.0.131",4444)

while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(ip)
    k = input("chat: ")
    s.send(k.encode())
    l = s.recv(1024)
    print(l.decode())
    s.close()