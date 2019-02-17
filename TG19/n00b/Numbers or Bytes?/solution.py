import socket
from binascii import hexlify, unhexlify
from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote("bytes.tghack.no", 2010)

for i in range(1000):
	print r.recvline()
	ting=r.recvline()
	print ting
	command=r.recvuntil(" ")
	print command
	if "Number?" in command:
		r.sendline(str(bytes_to_long(unhexlify(ting.strip()))))
	else:
		r.sendline(str(hexlify(long_to_bytes(ting))))
	print r.recvline()
	
print r.recvline()
r.close()
