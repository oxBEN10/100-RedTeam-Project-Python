import socket

HOST = '0.0.0.0'  
PORT = 12345        

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server started on {HOST}:{PORT}, waiting for a connection...")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address[0]}:{client_address[1]}")

# Open a file to write the incoming data
with open('received_file.txt', 'wb') as file:
    print("Receiving file...")
    while True:
        # Receive data in chunks of 1024 bytes
        data = client_socket.recv(1024)
        if not data:
            # Stop receiving when no more data
            break
        file.write(data)  # Write the received data to the file

print("File received successfully.")
client_socket.close()
server_socket.close()
