import time
import serial
from MouseController import MouseController
import threading


 
# Iniciando conexao serial
comport = serial.Serial('/dev/ttyUSB0', 9600,timeout=1)
time.sleep(2)
mouse = MouseController()

#comport = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) # Setando timeout 1s para a conexao

def InfoComSerial():
	print '\nObtendo informacoes sobre a comunicacao serial\n'
	# Iniciando conexao serial
	time.sleep(1.8) # Entre 1.5s a 2s
	
	print 'Device conectado: %s ' % (comport.name)
	print 'Dump da configuracao:\n %s ' % (comport)
	print '\n###############################################\n'
	# Fechando conexao serial
	comport.close()

def sentData(data):
	comport.write(data)

def readData(sport):
	sentData("a")
	while(True):
		data = sport.readline()
		moveMouse(data)
	comport.close()

def processData(str):
	moveMouse(str)
	

def clickMouse(data):
	return null

def moveMouse(data):
	if(len(data) > 0):
		x,y =  data.split("@")
		intx = int(x)
		inty = int(y)
		print intx
		print inty
		mouse.setPosition(intx,inty)
		


thread = threading.Thread(target=readData, args=(comport,))
thread.start()