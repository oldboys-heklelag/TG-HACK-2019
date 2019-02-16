import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(("35.204.28.195",5555))

for i in range(55):
	ting=s.recv(1024)
	print(ting)
	s.send(ting)

s.close()
