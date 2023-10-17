import socket
import tkinter
from time import strftime
from tkinter import LEFT,BOTH,E

HEADER = 64 
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER  = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) 

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)
connected = True

def send_close():
    msg = DISCONNECT_MESSAGE
    print("Conexão encerrada.")
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    cliente.send(send_length)
    cliente.send(message)
    root.destroy()
    root.quit()

def set_clock():
 clock.config(text = strftime("%H:%M"))
 clock.after(1000,set_clock)

def send():
    msg = str(entry1.get())
    print(f'Entrada: {msg}')
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    cliente.send(send_length)
    cliente.send(message)
    resp = (cliente.recv(2048)).decode(FORMAT)
    print(f"Resposta: {resp}\n")
    resp_label['text'] = resp
    resp_label.pack()

root = tkinter.Tk()
root.title('Linhas_Fortaleza')
root.geometry('600x350')
root.resizable(0,0)

fram1= tkinter.Frame(root, bg = "#0B615E",width=500, pady=20)
fram2=tkinter.Frame(root, bg="#E0F8F7", width=50)

label1 = tkinter.Label(fram1, width=15, bg="#0B615E",fg="white",text='DIGITE A LINHA:', font="Helvetica 15 bold", pady=10)
entry1 = tkinter.Entry(fram1, justify='center', bg="#1C1C1C", fg="#FF8000", width=20 ,font=('Helvetica', 20, 'bold'),borderwidth = 0)
clock = tkinter.Label(fram1, width=10, bg="#0B615E", fg = "white", font="Helvetica 13 bold", pady=20)
resp_label = tkinter.Label(fram2, text='', width=100, bg="#fff111", fg="red", pady=30, font="Helvetica 15 bold")
btn_buscar = tkinter.Button(fram2, fg="white", pady=8, bg = "#2E9AFE", width=20, text='Buscar', borderwidth = 0, command=send, activebackground="#E0F8F7", font="Helvetica 10 bold")
btn_close = tkinter.Button(fram2, fg="white", pady=8, width=7, text='Fechar', bg ="#A9230E", borderwidth = 0, activebackground="#E0F8F7", command=send_close, font="Helvetica 10 bold")

fram1.pack(fill=BOTH)
fram2.pack(fill=BOTH)

clock.pack(anchor=E)
label1.pack()
entry1.pack()
btn_buscar.pack()
resp_label.pack()
btn_close.pack(side=LEFT)

set_clock()
root.protocol("WM_DELETE_WINDOW",send_close)
root.mainloop()

