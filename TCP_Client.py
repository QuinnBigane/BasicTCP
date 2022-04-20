import socket
import time

def Main():
    host = '76.218.254.93' #The host on your client needs to be the external-facing IP address of your router. Obtain it from here https://www.whatismyip.com/
    port = 50002 
    s = socket.socket()
    s.connect((host,port))
    msgs_to_send = 100
    while msgs_to_send > 0 :
        string = "this is from the client file" 
        message = bytes(string, 'ascii')
        s.send(message)
        time.sleep(10)
        msgs_to_send-=1
    s.close()

if __name__ == '__main__':
    Main()
