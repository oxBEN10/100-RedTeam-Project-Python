import socket
import threading

HOST = '127.0.0.1'  
PORT = 12345        

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Listen for a connection

print(f"Server started on {HOST}:{PORT}, waiting for a connection...")

# Accept a single connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address[0]}:{client_address[1]}")

# Function to handle receiving messages
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Client disconnected.")
                break
            print(f"Client: {message}")
        except:
            print("An error occurred while receiving the message.")
            break

# Function to handle sending messages
def send_messages():
    while True:
        try:
            response = input("You: ")
            client_socket.send(response.encode('utf-8'))
        except:
            print("An error occurred while sending the message.")
            break

# Start the two threads: one for sending and one for receiving messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()

# Join the threads to keep them running
receive_thread.join()
send_thread.join()

# Close the connection
client_socket.close()
server_socket.close()
