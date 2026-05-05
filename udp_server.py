import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 5000))

print("Server listening...")

data, addr = server.recvfrom(1024)
print("Recieved:", data.decode())