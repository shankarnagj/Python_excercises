import socket               # Import socket module

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345 
s.connect((host, port))
comp_info=''               # Reserve a port for your service.

while True :
    msg = s.recv(7)
    if len(msg)<=0 :
        break
    comp_info+=msg.decode("utf-8")

print(comp_info)
   
