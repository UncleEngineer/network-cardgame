#card-client.py
from tkinter import *
from tkinter import ttk
import random
import socket
GUI = Tk()
GUI.geometry('700x800')
GUI.title('Card Game')

FONT1 = ('Impact',20)
FONT2 = ('Angsana New',20)

########LEFT TOP##########
F1 = Frame(GUI)
F1.pack()

L = ttk.Label(F1,text='รหัสห้อง',font=FONT2).pack()
v_roomnumber = StringVar()
E1 = ttk.Entry(F1,textvariable=v_roomnumber,font=FONT1,width=5)
E1.pack()

L = ttk.Label(F1,text='ชื่อ',font=FONT2).pack()
v_playername = StringVar()
E2 = ttk.Entry(F1,textvariable=v_playername,font=FONT2)
E2.pack()

#############NETWORK###############
def DecodeCommandServer(cmd):
	allcmd = cmd.split('|')
	if allcmd[0] == 'chk':
		playerid = allcmd[1]
		status = allcmd[2]
		v_playerid.set(playerid)
		v_gamestatus.set('-------เชื่อมต่อกับ server แล้ว------')

clientip = '192.168.1.150'
clientport = 7500

def SERVER():
	while True:
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

		server.bind((clientip,clientport))
		server.listen(1)
		print('Waiting for client...')

		client, addr = server.accept() # object , ip and number
		print('Connected from: ',str(addr))
		try:
			data = client.recv(1024).decode('utf-8') # ดึงข้อมูลที่ส่งมา
			#DecodeCommand(data)
			print('Message from client: ',data)
			client.send('Received!'.encode('utf-8'))
			print('-----------')
		except:
			pass
		client.close()

def StartServer():
	task = threading.Thread(target=SERVER)
	task.start()




serverip = '192.168.1.150'
port = 7000

def SendCommand(data):
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

'''
stg = start game
'''
from tkinter import messagebox

def StartGame():
	roomnumber = v_roomnumber.get()
	name = v_playername.get()
	if len(roomnumber) == 3 and len(name) > 0 and roomnumber.isdigit() :
		v_gamestatus.set('กำลังเริ่มเกม')
		cmd = 'stg|{}|{}|{}|{}'.format(roomnumber,serverip,port,name)
		print(cmd)
		SendCommand(cmd)
	else:
		messagebox.showerror('Data Error','กรุณากรอกชื่อห้องและชื่อผู้เล่นให้ถูกต้อง')


B1 = ttk.Button(F1,text='Start',command=StartGame)
B1.pack(ipadx=20,ipady=10)

v_gamestatus = StringVar()
v_gamestatus.set('-------status-------')
gamestatus = ttk.Label(F1,textvariable=v_gamestatus,font=FONT2,foreground='green')
gamestatus.pack()

v_playerid = StringVar()
v_playerid.set('-------ID-------')
playerid = ttk.Label(F1,textvariable=v_playerid,font=FONT1)
playerid.pack()

GUI.mainloop()