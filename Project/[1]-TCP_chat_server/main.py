import socket


HOST = '127.0.0.1' 
PORT = 12345       

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Listen for only one connection

print(f"Server started on {HOST}:{PORT}, waiting for a connection...")

# Accept a single connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address[0]}:{client_address[1]}")

# Simple chat loop (receives and sends messages)
while True:
    message = client_socket.recv(1024).decode('utf-8')
    
    if not message:
        print("Client disconnected.")
        break
    
    print(f"Client: {message}")
    
    # Send a response back to the client
    response = input("You: ")
    client_socket.send(response.encode('utf-8'))

# Close the connection
client_socket.close()
server_socket.close()
