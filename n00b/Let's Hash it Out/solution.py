# Python 2.7
import socket
import hashlib

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(("35.204.26.212", 2001))

def main():

    mottatt = s.recv(1024)
    encrypt(mottatt)

    for i in range(999):
        print "No. answers: ", (i+2)

        mottatt = s.recv(1024)
        encrypt(mottatt)

    flag = s.recv(1024)
    print "\n" + flag


def encrypt(string):
    print string

    toEncrypt = (string.split(':'))[1][1:]
    length = len(toEncrypt) - 7
    toEncrypt = toEncrypt[0:length]

    encryption = (((string.split(","))[0]).split(" "))[-1]

    if encryption == 'MD5':
        answer = hashlib.md5(toEncrypt).hexdigest()
        s.send(answer + "\n")
        print answer + "\n"

    elif encryption == 'SHA256':
        answer = hashlib.sha256(toEncrypt).hexdigest()
        s.send(answer + "\n")
        print answer + "\n"

    elif encryption == 'SHA512':
        answer = hashlib.sha512(toEncrypt).hexdigest()
        s.send(answer + "\n")
        print answer + "\n"


main()
s.close()
