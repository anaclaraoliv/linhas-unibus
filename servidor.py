import socket
import threading
import pandas as pd

HEADER = 64 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
tbl = pd.read_csv('linhas_onibus.csv',index_col=['Número'])        

def analise_msg(msg):    
    try:
        msg = int(msg)
        nome = tbl.loc[msg, 'Nome']
        if nome:
            return(nome)
    except:
        if type(msg) == int:
            return("Essa linha não existe.")
        else:
            return("Entrada Para Pesquisa Inválida.")

def handle_client(conn, addr): 
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                print("Conexão será encerrada.")
                connected = False

            resp = analise_msg(msg)

            print(f"[{ADDR}] {msg}\n {resp}")
            conn.send(resp.encode(FORMAT))
            
    conn.close()

def start(): 
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() 
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") 

print("[STARTING] server is starting...")
start()
