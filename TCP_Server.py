"""
Title: TCP_Server.py

Authors:
Quinn Bigane 

Date
4/21/22

This File will implement a server in a TCP connection.
It will recieve json messages and, if it is in test mode,
it will parse those messages and determine the reliability 
percentage and average latency of the connection.
"""

#TODO: Parse all the recieved messages for reliability percentages based on ID
#TODO: Parse all the recieved messages for a latency based on timestamps


import socket 
import time

def Main():
    #Source IP (rotuer LAN IP)
    #host = '192.168.1.120'
    host = '172.17.7.175'
    #Source Port
    port = 50002

    #Create and conenct to the socket
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()

    #create a list to hold info
    messages = {}
    while True:
        #receive the data
        print("Waiting To Recv")
        data = c.recv(3072)
        if not data:
            break

        #add a timestamp of when we received
        recv_time = str(time.time())
        data = str(data).upper()
        final = f"recieved: {recv_time} {data}"
        #parse that info
        toks = final.split()
        #tok 1 is recv'd time, tok 3 is ID, tok 5 is sent time
        messages[toks[3]] = f"{toks[1]} {toks[5]}"
    
    
    messages_expected = 10
    messages_recv = 0
    avg_latency = 0
    for i in range(messages_expected):
        key = str(i)
        if key in messages.keys():
            messages_recv +=1
            message_toks = messages[key].split()
            avg_latency += float(message_toks[0]) - float(message_toks[1])
    avg_latency /= messages_recv
    reliability = messages_recv/messages_expected
    print(f"Reliability: {reliability * 100}")
    print(f"Average Latency: {avg_latency}")
    c.close()
if __name__ == '__main__':
    Main()