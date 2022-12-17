from socket import *

HOST = "192.168.1.30"
PORT = 5555

data = ""

print('Connected to server: (press exit to quit)')
serversock = socket(AF_INET, SOCK_STREAM)
serversock.connect((HOST, PORT))
while data != "exit":
    input_String = input()
    serversock.sendall(bytes(input_String, encoding='utf8'))
    data = serversock.recv(1024)
    data = data.decode()
    print("Received: {data}")
serversock.close()