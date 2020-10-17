import socket

serverip = '192.168.1.150'
port = 7000

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
		print('Message from client: ',data)
		client.send('Received!'.encode('utf-8'))
		print('-----------')
	except:
		pass
	client.close()

