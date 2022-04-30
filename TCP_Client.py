"""
Title: TCP_Client.py

Authors:
Quinn Bigane 

Date
4/21/22

This File will implement a client in a TCP connection.
It will send 1 json messages 2kb in size once a second 
for 100 seconds. 
"""

import socket
import time

def Main():
    #Destination IP (Router WAN IP)
#    host = '76.218.254.93' 
    host = '192.168.2.230'
    #Destination port (Port open on router)
    port = 50002 
  
    #Create and connect to the socket
    s = socket.socket()
    s.connect((host,port))
  
    #2kb json string
    buff_string = str({
        "name": "Molecule Man",
        "age": 29,"secretIdentity": "Dan Jukes",
        "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER",
        "BUFFERBUFFERBUFFER"
        ]
        })

    msgs_sent = 0
    while msgs_sent < 10000:
        if not __debug__:
            #code to skip a message     
            if msgs_sent in [7,11,98,86]:
                msgs_sent+=1
                print("client skipped a package because debug enabled")
                continue
        
        #Add ID and timestamp to message
        string = "" 
        string = f"ID: {msgs_sent} sent: {round(time.time() * 1000)} " 
        string += buff_string
        
        if not __debug__:
            #code to add latency
            print("client is waiting to simulate latency in the connection")
            time.sleep(1.7)
        
        #format message
        message = bytes(string, 'ascii')
        #send message
        s.send(message)
        print("Sent")
        #wait 1 second
        time.sleep(1)
        msgs_sent+=1
    s.close()

if __name__ == '__main__':
    Main()
