import socket
host='192.168.0.103'
port=9000
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
client,address=server.accept()
while True:
    print(f"Connected to {address}")
    cmd=input("Enter a command: ")
    client.send(cmd.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))