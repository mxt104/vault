import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.29.142'
port = 54321
client_socket.connect((host,port))

while True:
	message=input("Client:")

	client_socket.send(message.encode())
	if message.lower()=='exit':
		break

	reply = client_socket.recv(1024).decode()
	print("Server:",reply)
	if reply.lower()=='exit':
		break

client_socket.close()