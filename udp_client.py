import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("Hello server this is test for UDP protocol".encode(), ("127.0.0.1", 5000))
print("Request Sent")