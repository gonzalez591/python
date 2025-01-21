print("como hacer un cliente y servidor con ruby")
print("1 cliente ")
print("2 servidor")

klk = int(input("dime "))

if klk == 1:
    with open("cliente.txt","a") as file:
        file.writelines(["""require "socket"

klk = TCPsocket.new("0000",1222)

#se encia con puts y recibi con  gets

klk.puts

klk.gets

#al final se cierra la conexion

klk.close"""])


elif klk == 2:
    with open("servidor.txt","w") as file:
        file.writelines(["""require "socket"

klk = TCPsversocket.new("0000",1222)

#se acept la conexion 

kl = klk.acept

#con pus y gets se envia y recibi datos


kl.gets

kl.puts


#al final se cierra la conecion 

kl.close

klk.close
"""])