from datetime import datetime
import socket

def print_machine_info():
	host_name=socket.gethostname()
	ip_address=socket.gethostbyname(host_name)

	time_now = datetime.now()
	
	print()
	print("Vrijeme pokretanja ovog programa: ", time_now)
	print("Program se izvodi na računalu:")
	print("Host name: %s" % host_name)
	print("IP address: %s" % ip_address)
	print("-----------------------------------------------------------")
if __name__ == '__main__':
	print_machine_info()

