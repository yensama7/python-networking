import threading
import socket


#Define a host and a port for our server
#you can use your router's ip address to communicate by
#connecting the devices to the router
#change the host to the ip address of your router on the client and server, choose a port
#run server and client on one device and client on the other
#you can start chatting 

host = '127.0.0.1'#localhost
port = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Creates connection
server.bind((host, port))# Binds the server to the host
server.listen()# Listens for incoming connection

clients = []
nicknames = []

def broadcast(message):# Brodcast to every client on the server
    for client in clients:
        client.send(message)

def handle(client):# Handles requests
    while True:
        try:
            message = client.recv(1024)#1024 is the bytes
            broadcast(message)
        except:
            index = clients.index(client)#removes client if connection fails
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat".encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():#Accepts connections
    while True:
        client, address = server.accept()# Returns client and address of client
        print(f"connected with {str(address)}")

        client.send('NICK'.encode('ascii'))#Gets nickname from client
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)# Appends client name to the clients list

        print(f"Nickname of the client is {nickname}")
        broadcast(f'{nickname} Joined the chat'.encode('ascii'))
        client.send("connected to the server".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening......")
receive()
