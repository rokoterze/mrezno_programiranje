import socket
import datetime
import local_machine_info

print(datetime.datetime.now())
local_machine_info.print_machine_info()

host = socket.gethostname()
port = 12345

client_socket = socket.socket()

client_socket.connect((host, port))

upit = input('Unesite tekst: ')
unos_ime='roko terze'

if(upit == unos_ime):
    print('Unos nije podržan!')

client_socket.sendall(upit.encode('ascii'))


data = client_socket.recv(1024)


print (data)
client_socket.close()
