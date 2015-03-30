import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port
s.connect((host,port))

# Receive no more than 1024 bytes
num = 0
gameEnd = False
while not gameEnd:
	s.sendall(bytes(str(num),encoding='ascii'))
	num += 1
	msg = s.recv(1024)
	if msg == "end":
		gameEnd = True
	else:
		print(msg)

s.close()