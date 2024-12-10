import time

while True:
    try:
        print("    _______  ")
        print("   |       | ")
        print("   |       | ")
        print("   |_______| ")
        print("  /         \\")
        print(" /___________\\")
        print("|   SOCKET    |")
        print("|___________  |")
        print("   |       |   ")
        print("   |       |   ")
        print("   |_______|   ")
        time.sleep(2)

        klk = "bienvenido"
        print(klk)
        time.sleep(2)
        lol = "este script te crea un cliente y un servidor "
        print(lol.upper())
        time.sleep(2)
        ju = "1 - cliente"
        print(ju)
        time.sleep(1)
        hy = "2 - servidor "
        print(hy)
        time.sleep(1)
        h = "3 - exit "
        print(h)
        time.sleep(1)
        j = int(input("dime "))
        if j == 1:
            with open("cliente.py","a") as file:
                file.writelines(["""import socket \n

while True:
    ip = ("10.0.0.131",4444)
    s = socket.socket()
    s.connect(ip)
    ju = input("shell@shell$ ")
    s.send(ju.encode())
    print(s.recv(1021).decode())
    s.close()
"""])
    
        elif j == 2:
            with open("servidor.py","a") as file:
                file.writelines(["""import socket
import subprocess

ip = ("10.0.0.131",4444)
while True:
    s = socket.socket()
    s.bind(ip)
    s.listen(1)

    juan,k = s.accept()

    f = juan.recv(1021).decode()
    print(f)
    j = subprocess.run(f"cmd.exe /c {f}",shell=True,capture_output=True,text=True)
    h = j.stdout
    juan.send(h.encode())
    juan.close()
    s.close()"""])
        elif j == 3:
            baba = "quires salir ?"
            print(baba)
            l = input("dime si o no ")
            try:

                if l == "si":
                    k = "ok saliendo ..."
                    print(k)
                    time.sleep(2)
                    break
                elif l == "no":
                    u = "ok"
                    print(u)
            except:
                kaka = "hubo un error"
                print(kaka.title())
    
    except:
        print("error[-]".upper())
    finally:
        print("espero que te guste ")