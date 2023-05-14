import socket


client_socket = socket.socket()
host = socket.gethostname()
host_ip = socket.gethostbyname(host)
port = 9999

message = b"Hello, World!" 
# bez "b" je greska [byte]

print("UDP target IP: %s" % host_ip)
print("UDP target port: %s" % port)
print("Message: %s" % message)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.sendto(message, (host, port))