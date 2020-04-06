import socket 
import threading 

HEADER = 64
PORT = 5050 
# this IP was not working on my pc 
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "0.0.0.0"   # this works 
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR, )

def handle_client(conn,addr):
    print("[NEW CONNECTION] {} connected. ".format(addr)) 
    connected = True 
    while connected:
        msg_length = conn.recv(HEADER).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) 
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print("[{}] {}".format(addr,msg))
            conn.send("Message received".encode(FORMAT))

    conn.close()
         

def start():
    server.listen(1)
    print("[LISTENING] Server is listening on {}".format(SERVER))
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[ACTIVE CONNECTIONS] {}".format(threading.activeCount()-1))

print("[STARTING] server is starting...")
start()


