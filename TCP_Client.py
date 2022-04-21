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
    #host = '76.218.254.93' 
    host = '172.17.7.175'
    #Destination port (Port open on router)
    port = 50002 
    
    #Create and connect to the socket
    s = socket.socket()
    s.connect((host,port))
    
    buff_string = str({
    "name": "Molecule Man",
    "age": 29,
    "secretIdentity": "Dan Jukes",
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
    while msgs_sent < 10 :
        if msgs_sent == 7:
            msgs_sent+=1
            continue
        #Add ID and timestamp to message
        string = "" 
        string = f"ID: {msgs_sent} sent: {time.time()} " 
        string += buff_string
        message = bytes(string, 'ascii')
        s.send(message)
        print("Sent")
        time.sleep(1)
        msgs_sent+=1
    s.close()

if __name__ == '__main__':
    Main()
