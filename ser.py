
import socket



l = input("dime la ip de la maquina vitima ")
k = int(input("dime el puerto "))

ip = (l,k)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(ip)
s.listen(1)

ki,lo = s.accept()

print("se conecto la ip",lo)

klk = ki.recv(2024)

print(klk.decode())

s.close()
ki.close()
