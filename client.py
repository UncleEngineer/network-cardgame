import socket

serverip = '192.168.1.150'
port = 7000

while True:
	data = input('DATA: ')
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