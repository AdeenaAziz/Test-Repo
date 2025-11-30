# Python Socket Demo

A simple Client–Server project created while learning the Python Socket library. This project demonstrates how two programs can communicate with each other over a network using TCP sockets.

## Features

- Basic socket creation
- Server listens on a port
- Client connects to server
- Client sends a message to server
- Server receives and prints the message

## Project Files

- **server.py** - Starts the server, listens for incoming client connections, receives data
- **client.py** - Connects to the server and sends a message

## How to Run the Project

1. **Start the Server:**  
   Run `server.py`  
   You should see:  
   `Server is running...`  
   `Waiting for connection...`

2. **Run the Client:**  
   Run `client.py`  
   The server will print the message sent by the client.

## Requirements

- Python 3.x
- Uses built-in socket module only
