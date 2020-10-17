#card-server.py
from tkinter import *
from tkinter import ttk
import random
GUI = Tk()
GUI.geometry('700x800')
GUI.title('Card Game')

FONT1 = ('Impact',20)

########LEFT TOP##########
F1 = Frame(GUI)
F1.place(x=50,y=50)
########GAME SETTING##########
global current_number
current_number = '000'

global player
player = {}

def GenerateID(name,ip,port):
	rid = str(random.randint(100,999))
	while rid in player:
		rid = str(random.randint(100,999))
	player[rid] = {'id':rid,'name':name,'ip':ip,'port':port}

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
header = ['ID','NAME','ALL SCORE','TOTAL','SCORE','STATUS']
hw = [70,100,200,70,70,70]

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


GUI.mainloop()