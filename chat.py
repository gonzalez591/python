import socket

ip = ("10.0.0.131",4444)

while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(ip)
    s.listen(1)
    c,k = s.accept()
    l = c.recv(1024)
    print(l.decode())
    ki = input("chat: ")
    c.send(ki.encode())
    c.close()
    s.close()
