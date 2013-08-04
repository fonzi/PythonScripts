import socket

sock = socket.socket()      #Create sock
host = socket.gethostname() #Get host name
port = 12345                #Port 12345
sock.connect((host, port))  #Connect to the server
print sock.recv(1024)       #Print the sock
sock.close()                #close the sock