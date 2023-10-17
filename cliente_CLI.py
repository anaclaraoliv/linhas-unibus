import socket

HEADER = 64 
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER  = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)
connected = True

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    cliente.send(send_length)
    cliente.send(message)
    resp = (cliente.recv(2048)).decode(FORMAT)
    print(resp)

while connected:
    msg = str(input("Insira o número da linha:"))
    if msg == DISCONNECT_MESSAGE:
        print("Conexão encerrada.")
        send(msg)
        connected = False
    send(msg)

