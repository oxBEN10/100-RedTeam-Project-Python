import socket

def udp_server(host='0.0.0.0', port=9998):
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print(f'[*] Listening on {host}:{port}')

    while True:
        data, addr = server.recvfrom(1024)
        print(f'[*] Received: {data.decode("utf-8")} from {addr[0]}:{addr[1]}')

if __name__ == '__main__':
    udp_server()
    
    
    
    