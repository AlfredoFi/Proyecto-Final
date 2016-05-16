import socket   

HOST = ''                #Define all possible hosts
PORT = 50007             #Working port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Define protocol IPv4 and TCP protocol
s.bind((HOST, PORT))   #Bind the socket to address
s.listen(5)
while True:
    conn,addr = s.accept()  #Accept a connection. The socket must be bound to an address and listening for connections.  
    print 'Conexion realizada desde: ',addr
    data = conn.recv(1024)  #Enable a server to accept connections. If backlog is specified, it must be at least 0
    print 'El voto fue para: ',data
    conn.send('Gracias por utilizar el servicio')  #Send data to the socket. The socket must be connected to a remote socket. 
    conn.close()               #Mark the socket closed.
