# Threaded port scanning
import socket
import threading
from queue import Queue

target = "192.168.70.234" #Target IP
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates connecton
        sock.connect((target, port)) # Connects to target
        return True
    except:
        return False


def fill_queue (port_list): #Creates a queue of scanned ports
    for port in port_list:
        queue.put(port)

def worker(): #Working function of the code
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f"Port {port} is open!")
            open_ports.append(port)


port_list = range(1, 1024)#List of ports
fill_queue(port_list)

thread_list = []

for t in range(1000):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:#starts thread
    thread.start()

for thread in thread_list: #waits for all the threaads to complete  
    thread.join()

print("Open ports are:", open_ports)