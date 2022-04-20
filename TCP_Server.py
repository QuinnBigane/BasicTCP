import socket

def Main():
    host = '192.168.1.120'
    port = 50002
    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    while True:
        print("Waiting To Recv")
        data = c.recv(1024)
        if not data:
            break
        data = str(data).upper()
        print(data)
    c.close()
if __name__ == '__main__':
    Main()