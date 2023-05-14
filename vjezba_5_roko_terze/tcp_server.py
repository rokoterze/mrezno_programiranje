import socket

server_socket = socket.socket()
host = socket.gethostname()
port = 99

server_socket.bind((host,port))

print("Waiting for connection...")
server_socket.listen(5)

while True:
    conn,addr = server_socket.accept()
    print("Got connection from",addr)
    conn.send(b'Server Saying Hi!')
    conn.close()