import socket
import threading

HOST = '127.0.0.1'  
PORT = 12345       

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"UDP Server started on {HOST}:{PORT}, waiting for messages...")

client_address = None  # To store the address of the client once a message is received

# Function to handle receiving messages
def receive_messages():
    global client_address
    while True:
        try:
            # Receive message from the client
            message, client_address = server_socket.recvfrom(1024)
            message = message.decode('utf-8')
            if not message:
                print("Client disconnected.")
                break
            print(f"Client: {message}")
        except Exception as e:
            print(f"An error occurred while receiving the message: {e}")
            break

# Function to handle sending messages
def send_messages():
    global client_address
    while True:
        try:
            if client_address:
                # Get input from the server to send to the client
                response = input("You: ")
                server_socket.sendto(response.encode('utf-8'), client_address)
        except Exception as e:
            print(f"An error occurred while sending the message: {e}")
            break

# Start the two threads: one for sending and one for receiving messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()

# Join the threads to keep them running
receive_thread.join()
send_thread.join()

# Close the socket when done
server_socket.close()
