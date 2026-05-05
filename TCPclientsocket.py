import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = "www.google.com"
server_port = 80

client_socket.connect((server_host, server_port))

request = "GET / HTTP/1.1\r\nHOST: www.google.com\r\nConnection: close\r\n\r\n"

client_socket.send(request.encode())

response = b""
while True:
	data = client_socket.recv(4096)
	if not data:
		break
	response += data

print(response.decode(errors="ignore"))

client_socket.close()