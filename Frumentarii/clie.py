
# Message Sender
import os
from socket import *
import socketserver
# import terminalv2 as tml
import logging
import json
from threading import local
from art import *
from tqdm import tqdm, trange
from time import sleep
from colorama import Fore, Back, Style,init
from termcolor import colored
import os
# import client
# from header import print_header as ph


s = socket(AF_INET, SOCK_DGRAM)
try:
# doesn't even have to be reachable
    s.connect(('10.255.255.255', 1))
    IP = s.getsockname()[0]
except Exception:
    IP = '127.0.0.1'
finally:
    s.close()
TCP_IP = gethostbyname(IP)
TCP_PORT = 13000

message = {
    
}
'''
message = {
    "type" : "handshake" or "message"
    "from" : "username"
    "to"   : "username"
    "msg"  : "Hello World!"
    
    }'''
def client_side(server_add):

    TCP_IP = server_add
    TCP_PORT = 13000
    BUFFER_SIZE = 1024
    MESSAGE = input("send: ")
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(bytes(MESSAGE, 'utf-8'))
    data = s.recv(BUFFER_SIZE)
    s.close() 
    #TODO keep it alive
    return server_add



class MyTCPHandler(socketserver.BaseRequestHandler):
    
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('ClientLogger')
        self.logger.debug('__init__')
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
        return
            
    def handle(self):
        while 1:
            self.data = self.request.recv(1024)
            if not self.data:
                break
            self.data = self.data.strip()
            data = self.data
            self.request.send(self.data.upper())
            #TODO change the read_message to handle both handle_types and call the appropriate func
            MyTCPHandler.read_message(data)
    
    def client_handshake(server_add,username):

        sendto = "blank"
        handle_type = "handshake"
        TCP_IP = server_add
        TCP_PORT = 5005
        BUFFER_SIZE = 1024
        handle_type = "handshake"
        message_dict = {
        "type" : handle_type,
        "from" : username,
        "to"   : sendto,
        "msg"  : "Hello World!"        
        }
        #TODO add erroor handliong to send to GUI
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        message = str(message_dict)
        message = json.dumps(message).encode('utf-8')
        s.send((message))
        #tml.message.send_message(message_dict)
    
        
    def read_message(data):
        
        data = data[1:]
        data = data.split(",")
        handle_type = str(data[0])
        message = str(data[1])
    
    def send_message(message, server_add):
        
        username = message["from"]
        raw_message = input(username + ": ")
        handle_type = "message"
        to = str(server_add)
        TCP_IP = server_add
        TCP_PORT = 13000
        BUFFER_SIZE = 1024
        message = {
            "type" : handle_type,
            "from" : username,
            "to"   : to,
            "msg"  : raw_message  
        }
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        str(message)
        message = json.dumps(message).encode('utf-8')
        s.send(bytes(message))

    
    def exchange():
        pass
        
    def close():
        pass
    
    def restart():
        pass
    
    def update():
        pass
    
    def get_usr(username, server_add):
        
        message = {
            "type" : "usrrequest",
            "from" : username,
            "to"   : "NULL",
            "msg"  : "NULL"
        }
                
        TCP_IP = server_add
        TCP_PORT = 13000
        BUFFER_SIZE = 1024        
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        str(message)
        message = json.dumps(message).encode('utf-8')
        s.send(bytes(message))
        MyTCPHandler.handle()

if __name__ == "__main__":
    
    HOST, PORT = TCP_IP , TCP_PORT
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()

class start_up():
    
    def estblish_connection(server_add,username):
        
        server_add = '192.168.10.108' #TODOinput("Please enter a server IP: ")
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        #client.MyTCPHandler.client_handshake(server_add,username)
        
    
class message():
        
    def send_message(message_dict):
        server_add = '192.168.1.103'
        MyTCPHandler.send_message(message_dict,server_add)
    
    def get_message(username,message):
        
        username = Fore.RED + username
        message = Fore.RED + message
        print("<",username,">", ": ", message)
        
    def get_users():
        
        server_add = '192.168.1.103'
        #MyTCPHandler.get_usr(username, server_add)
        
#TODO add encryption 
#TODO add decryption
#TODO Add keys and storage 