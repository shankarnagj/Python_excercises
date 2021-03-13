import socket               # Import socket module

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   cli, addr = s.accept()     # Establish connection with client.
   print (f'Got connection from {addr}')
   cli.send(bytes('Thank you for connecting',"utf-8"))
   cli.close()  