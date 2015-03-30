import socket
import time
import select
from game import gameEngine

# create a socket object
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host,port))

# queue up to 5 requests
serversocket.listen(5)

# create empty game object
engine = gameEngine.gameEngine()
clientsockets = []

while engine.canAdd():
	# establish a connection
	clientsocket,addr = serversocket.accept()
	
	print("Got a connection from %s" % str(addr))
	clientsockets.append(clientsocket)
	engine.addPlayer("Player"+str(engine.numPlayers))

turn = 0
timelimit = 0.1
currTime = time.time()
print("There are %s players" % str(len(clientsockets)))
while turn < engine.maxTurns:
	actions = []
	ready = [[]]
	endTime = time.time()
	if endTime - currTime < timelimit:
		continue
	ready = select.select(clientsockets,[],[],endTime-currTime)
	currTime = endTime
	turn += 1
	for clientsocket in ready[0]:
		actions.append(clientsocket.recv(1024))
		clientsocket.sendall(bytes("done",encoding='ascii'))
		
	for i in range(len(actions)):
		print ("%s sends %s" % (engine.getPlayerName(i),actions[i]))
	
for clientsocket in clientsockets:
	clientsocket.sendall(bytes("end",encoding='ascii'))
	clientsocket.close()