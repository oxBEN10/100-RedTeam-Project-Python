import socket

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host , port))
        print('Connected to server')
        with open("D:\github\100-RedTeam-Project-Python\Project\Test.txt", "rb") as f :
            data = f.read()
            s.sendall(data)
            print('File sent successfully')
            print(data.decode('utf-8'))
            
            
       