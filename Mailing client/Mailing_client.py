# Note: the connection may close and message not sent due to 
# Resrictions, Firewall or Athorization problems
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import sys

server = smtplib.SMTP('smtp.gmail.com',25, timeout=20) #defining the server(server can be changed depending on the aerver you use eg. gmail, yahoo) and port
server.ehlo() #Starts server

sender = input("Gmail sending message: ")
receiver = input("GMail address of person recieving: ")
#save your password in a text file in the same directory as the code (you can choose to encrypt and decrypt the password) and read it
#but this does not encrypt
try:
    with open('password,txt', 'r') as f: 
        password = f.read()
except:
    sys.exit("Password file not found")

server.login(f'{sender}', password) #logs into the sending email
# Mail content*************************
msg = MIMEMultipart()
msg['From'] = 'yensama7'
msg['To'] = f'{receiver}'
msg['Subject'] = 'Mailing client'

try:
    with open('message.txt', 'r') as f: # opens message
        message = f.read()
except:
    sys.exit("Message file not found")

msg.attach(MIMEText(message, 'plain')) # Attaches message

filename = 'Naruto.jpg' #Image name
try:
    attachment = open(filename, 'rb') #Opens the image
except:
    sys.exit("Image not found")

p = MIMEBase('application', 'octet-stream') #create a payload
p.set_payload(attachment.read())

encoders.encode_base64(p) #Encode image
p.add_header('Content-Disposition',f'attach, filename={filename}')
msg.attach(p)

text = msg.as_string() #turns the message into string
server.sendmail(f'{sender}', f'{receiver}', text)