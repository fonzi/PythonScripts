# Port 587 used to create sockets 
# 9 carries supported. 
# :) 


import smtplib

#start the smtp library with two inputs the designated client, and port
mailserver = smtplib.SMTP('smtp.gmail.com',587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()

#asks the user to input the information
username = raw_input("Email Address: ")
password = raw_input("Email Password: ")
number = raw_input("Phone Number: ")
carrier = raw_input("Phone Carrier: ")
texttosend = raw_input("Text to send: ")
timestosend = int(raw_input("Times to send: "))

#change to carrier
if carrier == "att":
    sendto = number + '@text.att.net'
elif carrier == "verizon":
    sendto = number + '@vtext.com'
elif carrier == "tmobile":
    sendto = number + '@tmomail.net'
elif carrier == "sprintpcs":
    sendto = number + '@messaging.sprintpcs.com'
elif carrier == "virginmobile":
    sendto = number + '@vmobl.com'
elif carrier == "uscellular":
    sendto = number + '@email.uscc.net'
elif carrier == "nextel":
    sendto = number + '@messaging.nextel.com'
elif carrier == "boost":
    sendto = number + '@myboostmobile.com'
elif carrier == "alltell":
    sendto = number + '@message.alltel.com'
elif carrier == "sprint":
    sendto = number + '@messaging.sprintpcs.com'
else:
    print("Carrier not supported. Sorry!")

mailserver.login(username,password)

x = raw_input("Press enter to launch.")

#send the text 
for x in range(0,timestosend):

    mailserver.sendmail(username, sendto, texttosend)
    print("Sent.")
#close the server 
mailserver.close()

stopapp = raw_input("Application finished. Press enter to close.")
