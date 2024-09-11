import socket

# Server settings
HOST = '127.0.0.1'  
PORT = 12345     
# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"UDP Server started on {HOST}:{PORT}, waiting for a message...")

# Server loop to handle one client at a time
while True:
    # Receive message from the client
    message, client_address = server_socket.recvfrom(1024)
    message = message.decode('utf-8')

    if not message:
        print("Client disconnected.")
        break
    
    print(f"Client [{client_address}]: { message}")
    
    # Get server response and send it back to the client
    response = input("You: ")
    server_socket.sendto(response.encode('utf-8'), client_address )

# Close the socket when done
server_socket.close()
