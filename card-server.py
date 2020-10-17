#card-server.py
from tkinter import *
from tkinter import ttk
import random
import socket
import time
import threading

########GAME SETTING##########
global current_number
current_number = '000'

global player
player = {}

global gametable_list
gametable_list = []

def GenerateID(name,ip,port):
	rid = str(random.randint(100,999))
	while rid in player:
		rid = str(random.randint(100,999))
	player[rid] = {'id':rid,'name':name,'ip':ip,'port':port}
	print(player)
	return rid

def DecodeCommand(cmd):
	# 'stg|410|192.168.1.150|7000|Somchai'
	# header = ['ID','IP','NAME','ALL SCORE','TOTAL','SCORE','STATUS']
	if cmd[:3] == 'stg':
		allcmd = cmd.split('|')
		if current_number == allcmd[1]:
			rid = GenerateID(allcmd[-1],allcmd[2],allcmd[3])
			player_data = [rid,allcmd[2],allcmd[-1],'',0,0,'-']
			gametable_list.append(player_data)
			gametable.insert('','end',value=player_data)

def SendCommand(data,serverip,port):
	client = socket.socket()
	client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

	client.connect((serverip,port))
	try:
		client.send(data.encode('utf-8'))

		datafromserver = client.recv(1024).decode('utf-8')
		print('Server: ',datafromserver)
		print('-----------')
	except:
		pass
	client.close()


###############NETWORK################
serverip = '192.168.1.150'
port = 7000

def SERVER():
	while True:
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

		server.bind((serverip,port))
		server.listen(1)
		print('Waiting for client...')

		client, addr = server.accept() # object , ip and number
		print('Connected from: ',str(addr))
		try:
			data = client.recv(1024).decode('utf-8') # ดึงข้อมูลที่ส่งมา
			DecodeCommand(data)
			print('Message from client: ',data)
			client.send('Received!'.encode('utf-8'))
			print('-----------')
		except:
			pass
		client.close()

def StartServer():
	task = threading.Thread(target=SERVER)
	task.start()


GUI = Tk()
GUI.geometry('900x800')
GUI.title('Card Game')

FONT1 = ('Impact',20)

########LEFT TOP##########
F1 = Frame(GUI)
F1.place(x=50,y=50)

##############################
def NewGame():
	global current_number
	rd = random.randint(100,999)
	current_number = str(rd)
	v_gamenumber.set(current_number)

B1 = ttk.Button(F1,text='New Game',command=NewGame)
B1.pack(ipadx=20,ipady=10)
########RIGHT TOP##########
v_gamenumber = StringVar()
v_gamenumber.set('001')
L1 = ttk.Label(GUI,textvariable=v_gamenumber,font=FONT1)
L1.place(x=300,y=50)
########LEFT BOTTOM##########
header = ['ID','IP','NAME','ALL SCORE','TOTAL','SCORE','STATUS']
hw = [70,100,100,200,70,70,70]

gametable = ttk.Treeview(GUI,height=20,column=header,show='headings')
gametable.place(x=50,y=300)

for hd,w in zip(header,hw):
	gametable.heading(hd,text=hd)
	gametable.column(hd,width=w)

########CENTER##########
F2 = Frame(GUI)
F2.place(x=270,y=150)

def RandomCard():
	print('Random Card')

B2 = ttk.Button(F2,text='Random Card',command=RandomCard)
B2.pack(ipadx=30,ipady=20)


StartServer()
GUI.mainloop()