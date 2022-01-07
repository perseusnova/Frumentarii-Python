import json
import os
import sys
import time
from socket import *
# import terminalv2 as tml
from threading import local
from time import sleep
from typing import ValuesView

# import terminalv2 as tmlv2
import PySimpleGUI as sg
from art import *
from colorama import Back, Fore, Style, init
from PySimpleGUI.PySimpleGUI import SELECT_MODE_SINGLE
from termcolor import colored
from tqdm import tqdm, trange
from pyupdater.client import Client
from client_config import ClientConfig

import clie as clie

APP_NAME = ClientConfig(); APP_NAME
APP_VERSION = '1.1.1'

def print_status_info(info):
    total = info.get(u'total')
    downloaded = info.get(u'downloaded')
    status = info.get(u'status')
    print(downloaded, total, status)
    
client = Client(ClientConfig())
client.refresh()

client.add_progress_hook(print_status_info)
app_update = client.update_check(APP_NAME, APP_VERSION)

if app_update is not None:
    
    app_update.download()
    
if app_update.is_downloaded():
    
    app_update.extract_overwrite()
    
if app_update.is_downloaded():
    
    app_update.extract_restart()

# #684 , 89
# sg.theme('DarkPurple6')
# animation = r'E:\GIT\chatterminal\giphy.gif'
# #this is for the Layout Design of the Window
# layout = [[sg.Image(animation, key='animated')]]

# #This Creates the Physical Window
# window = sg.Window().Layout(layout)
# while True:
#     event, values = window.Read(timeout=100) # every 100ms, fire the event sg.TIMEOUT_KEY
#     window.find_element("animated").UpdateAnimation(animation, time_between_frames=100)

#     if event is None :
#         break
#TODO animtion
#TODO sizing of windows

sg.theme('DarkPurple6')
str_text = 'what should we call you?'
str_serv = 'which server do you want to connect to?'
#this is for the Layout Design of the Window
layout = [[sg.Text(str_text,key='text')],
              [sg.InputText('',key='username')],
              [sg.Text(str_serv)],
              [sg.InputText('',key='server')],
              [sg.Submit('Submit')],
          ]
#This Creates the Physical Window
window = sg.Window('frumentarii', icon=r'E:\GIT\chatterminal\1200px-Globe_icon.svg.ico').Layout(layout).Finalize()
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Submit':
        username = str(values['username'])
        server_add = str(values['server'])
        break
    
window.close()

sg.theme('DarkPurple6')
str_text = 'just setting up'
#this is for the Layout Design of the Window
layout = [[sg.Text(str_text,key='text')],
              [sg.ProgressBar(1, orientation='h', size=(20, 20), key='progress')],
          ]
#This Creates the Physical Window
window = sg.Window('frumentarii', icon=r'E:\GIT\chatterminal\1200px-Globe_icon.svg.ico').Layout(layout).Finalize()

progress_bar = window.find_element('progress')
update_text = window.find_element('text')

#This Updates the Window
#progress_bar.UpdateBar(Cur100ent Value to show, Maximum Value to show)
progress_bar.UpdateBar(5, 100)

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
time.sleep(.5)

progress_bar.UpdateBar(1, 100)

client_address = "client IP = ", IP
update_text.update(client_address)
time.sleep(.5)

usrlist = {
    
}


'''message = {
    "type" : "handshake" or "message"
    "from" : "username"
    "to"   : "username"
    "msg"  : "Hello World!"
    
    }'''

update_text.update('Loaded client side')
progress_bar.UpdateBar(20, 100)
time.sleep(.5)

update_text.update('loaded TCP handler 1')
progress_bar.UpdateBar(30, 100)
time.sleep(.5)

progress_bar.UpdateBar(50, 100)
update_text.update('loaded startup')
time.sleep(.5)

progress_bar.UpdateBar(55, 100)
update_text.update('pinging server')
time.sleep(.5)
response = os.system("ping -n 1 " + server_add)

#and then check the response...
if response == 0:
    progress_bar.UpdateBar(60, 100)
    update_text.update('server is live')
    time.sleep(.5)
else:
    window.close()
    sg.theme('DarkPurple6')
    #this is for the Layout Design of the Window
    layout = [[sg.Text('Error: could not get a response from the server!')],
                [sg.Submit('Okay')],
            ]
    #This Creates the Physical Window
    window = sg.Window('Error', icon=r'E:\GIT\chatterminal\1200px-Globe_icon.svg.ico').Layout(layout).Finalize()
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Okay':
            break
    window.close()


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
update_text.update('connected to server!')
progress_bar.UpdateBar(65, 100)

#I paused for 3 seconds at the end to give you time to see it has completed before closing the window
update_text.update('loading GUI')
progress_bar.UpdateBar(70, 100)
progress_bar.UpdateBar(100, 100)
time.sleep(3)
#This will Close The Window
window.Close()
# if __name__ == "__main__":
    
#     HOST, PORT = TCP_IP , TCP_PORT
#     server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
#     server.serve_forever()
#serverIP = serveradd = start_up.estblish_connection(); serveradd

usrlist = {
    "Jack": "is cool",
    "Momo": "is cool",
    "Con": "is cool",
    "Umami": "is cool"
}
users = []
for user in usrlist.keys():
    
    users.append(user)

# users = ', '.join(users)
serverIP = ('Server address: ' + server_add)
serverIP = str(''.join(serverIP))
loggedin = str('Logged in as: '+ username)
loggedin = str(''.join(loggedin))
messagetext = 'connected \n'

#p = subprocess.Popen(["powershell.exe", "python server.py"])
Layout1 = [
          [sg.Text(serverIP, key='address'), sg.Text(loggedin, key='logname')],
          [sg.Text('please type who you would like to messge')],
          [sg.Text('Users: '), sg.Text(users)],
          [sg.Text('Send To: '), sg.InputText('',do_not_clear=False, key='userlist')],
          [sg.Submit('Ok')],
          ]

window = sg.Window('Frumentarii', icon=r'E:\GIT\chatterminal\1200px-Globe_icon.svg.ico', size=(679,956)).Layout(Layout1)
update_text = window.find_element('address')
update_user = window.find_element('userlist')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    
    elif event == 'Ok':
        
        sendto = values['userlist']
        window.close()
        break
    
Layout2 = [
          [sg.Text(serverIP, key='address'), sg.Text(loggedin, key='logname')],
          [sg.Text('sending a message to: ')], [sg.Text(str(sendto))],
          [sg.Multiline(messagetext, key='messages', do_not_clear=True)],
          [sg.Text('Message: '), sg.InputText('',do_not_clear=False)],
          [sg.Submit('Send')],
          ]

window = sg.Window('Frumentarii', icon=r'E:\GIT\chatterminal\1200px-Globe_icon.svg.ico', size=(679,956)).Layout(Layout2)
update_messages = window.find_element('messages')
update_name = window.find_element('logname')

while True:
    event, values =window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Send':
        
        message = values[0]
        update_messages.print(username+': '+message)
        handle_type = "message"
        to = sendto
        TCP_IP = server_add
        TCP_PORT = 5005
        BUFFER_SIZE = 1024
        message = {
            "type" : handle_type,
            "from" : username,
            "to"   : to,
            "msg"  : message  
        }
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        str(message)
        message = json.dumps(message).encode('utf-8')
        s.send(bytes(message))

    
window.close()
# tmlv2.init_terminal()
# tmlv2.help_screen()
# sleep(5)

# tmlv2.start_up.estblish_connection()
# tmlv2.message.get_users()
