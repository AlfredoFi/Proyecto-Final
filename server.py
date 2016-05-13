import socket

HOST = ''                 
PORT = 50007             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
while True:
    conn,addr = s.accept()    
    print 'Conexion realizada desde: ',addr
    data = conn.recv(1024) 
    print 'El voto fue para: ',data
    conn.send('Gracias por utilizar el servicio')  
    conn.close()               
