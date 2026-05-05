import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.29.142'
port = 54321
server_socket.bind((host,port))

server_socket.listen(1)
print("Server is waiting for connection....")

conn, addr = server_socket.accept()
print("Connection to:",addr)

while True:
	message = conn.recv(1024).decode()
	if message.lower()=='exit':
		print("Client disconnected")
		break
	print("Client:",message)

	reply=input("Server:")
	conn.send(reply.encode())
	if reply.lower()=='exit':
		break
conn.close()
server_socket.close()
	