import socket

def start_client(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.connect((host, port))
        print('Connected to server')

        
        with open("Test.txt", "rb") as f:
            while True:
                data = f.read(1024)  # Read file in chunks of 1024 bytes
                if not data:
                    break 
                s.sendall(data)  # Send the chunk to the server

        print('File sent successfully')

start_client()
