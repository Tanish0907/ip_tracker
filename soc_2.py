# first of all import the socket library
import socket			
import strength
# next create a socket object
s = socket.socket()		
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345			

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))		
print ("socket binded to %s" %(port))

# put the socket into listening mode192.168.129.91
s.listen(5)	
print ("socket is listening")		

# a forever loop until we interrupt it or
# an error occurs
while True:

    # Establish connection with client.
    c, addr = s.accept()	
    print ('Got connection from', addr )
    stre=-(strength.get_wifi_signal_strength())
    stre=str(stre)
    # send a thank you message to the client. encoding to send byte type.
    c.send(stre.encode())

    # Close the connection with the client
   

    # Breaking once connection closed

