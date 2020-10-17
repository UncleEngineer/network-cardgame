#card-client.py
from tkinter import *
from tkinter import ttk
import random
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

def StartGame():
	v_gamestatus.set('กำลังเริ่มเกม')

B1 = ttk.Button(F1,text='Start',command=StartGame)
B1.pack(ipadx=20,ipady=10)

v_gamestatus = StringVar()
v_gamestatus.set('-------status-------')
gamestatus = ttk.Label(F1,textvariable=v_gamestatus,font=FONT2,foreground='green')
gamestatus.pack()

GUI.mainloop()