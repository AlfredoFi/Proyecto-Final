import socket

HOST = 'localhost' 
PORT = 50007       
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
voto = raw_input("Ingresa tu Voto: ")
s.send(voto)
print s.recv(1024)
s.close()

