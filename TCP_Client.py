import socket

def Main():
    host = '76.218.254.93' #The host on your client needs to be the external-facing IP address of your router. Obtain it from here https://www.whatismyip.com/
    port = 50002 
    s = socket.socket()
    s.connect((host,port))
    string = "this is from the client file" 
    message = bytes(string, 'ascii')
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
    s.close()

if __name__ == '__main__':
    Main()