import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(("35.204.2.149",10000))

ting=s.recv(1024)
ting=ting.split('\n')[1]
print(ting)
ting=eval(ting)
s.send(str(ting)+"\n")

for i in range(1005):
	ting=s.recv(1024)
	print(ting)
	ting=ting.split('\n')[2]
	ting=eval(ting)
	s.send(str(ting)+"\n")

s.close()
