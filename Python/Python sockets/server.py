import socket

server = socket.socket()
server.bind(("localhost", 9999))
server.listen()

print("Server is running... Waiting for connection...")

client_socket, client_addr = server.accept()
print("Connected to:", client_addr)

data = client_socket.recv(1024)
print("Client says:", data.decode())

client_socket.close()
server.close()