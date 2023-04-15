import socket


HOST = '159.65.135.221'  
PORT = 2222
server_address = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect(server_address)
	data = s.recv(1024).decode("utf-8")
	print(data)
	data = s.recv(1024).decode("utf-8")
	print(data)
	senddata="1\n"
	s.send(senddata.encode())

	while True:
		data = s.recv(1024).decode("utf-8").split("\n")
		print(data)
		data = s.recv(1024).decode("utf-8").split()
		print(data)
		xxx=data[0]
		xxx1=data[1]
		xxx2=data[2]
		print(xxx, xxx1, xxx2)
		if (xxx1 == "div"):
			senddata=str(int(xxx)//int(xxx2))+"\n"
		elif (xxx1 == "mul"):
			senddata=str(int(xxx)*int(xxx2))+"\n"
		elif (xxx1 == "add"):
			senddata=str(int(xxx)+int(xxx2))+"\n"
		elif (xxx1 == "sub"):
			senddata=str(int(xxx)-int(xxx2))+"\n"
		else:
			print(data)
			break
		print(senddata)
		data = s.recv(1024).decode("utf-8").split("\n")
		s.send(senddata.encode())
		data = s.recv(1024).decode("utf-8")
		print(data)