import socket


HEADER = 64
PORT = 5050 
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED"
SERVER = "192.168.146.1"
ADDR = (SERVER,PORT)
 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)   



def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send(input("Enter message to send to server: "))
send(input("Enter message to send to server: "))
send(input("Enter message to send to server: "))
send(input("Enter message to send to server: "))
send(input("Enter message to send to server: "))
send(input("Enter message to send to server: "))
send(DISCONNECT_MESSAGE)