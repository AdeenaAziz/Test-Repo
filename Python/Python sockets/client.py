
import socket

client = socket.socket()
client.connect(("localhost", 9999))

client.send(b"Hello from Client!")

client.close()
