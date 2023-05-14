import socket
import local_machine_info

local_machine_info.print_machine_info()

hostname = input("Molimo vas unesite naziv hosta kojeg zelite testirati: ")
hostnameIP = socket.gethostbyname(hostname)

print("\n***********************************************************")
print("Hostname: {}\nIP Address: {}".format(hostname, hostnameIP))
print("***********************************************************\n")


print("Unesite od raspon portova za skeniranje?")
port1 = int(input("Početni port => "))
port2 = int(input("Završni port => "))
print("Odabrani portovi: {} - {}".format(port1,port2))
print("-----------------------------------------------------------")


def portscanner(port):
        if socket.create_connection((hostname, port)):
                print ("\n**Port {} je otvoren.**\n".format(port))

for port in range (port1, port2+1):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((hostnameIP, port))
	print ("Skeniram port: {}..".format(port))
	if result == 0:
		portscanner(port)
		sock.close()
                
print("-----------------------------------------------------------")
print ('Skeniranje portova završeno.')
