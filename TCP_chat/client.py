import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55556))
def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')#Gets info from the server
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()#Closes connection if it does get a message
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve) # Threading for recieve function
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()