import socket

HOST = 'localhost'   #Define el servidor destino
PORT = 50007       # Define el puerto
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Define protocol IPV4 and TCP protocol
s.connect((HOST, PORT))  # Realiza la conexión al servidor y puerto especificado anteriormente
voto = raw_input("Ingresa tu Voto: ") #Solicita el nombre del candidato
s.send(voto) # Envia el voto al servidor
print s.recv(1024)   #Imprime lo que haya recibido el socket, para recibir es necesaria la conexión del socket
s.close() # Marca el fin del ciclo del socket

