import pyOptoForce as pyof
from time import sleep
from time import clock
from msvcrt import kbhit
ports = pyof.OptoPorts(0,1000000)
portlist = ports.listPorts(False)
daq = pyof.OptoDAQ()
sleep(1)
if(daq.open(portlist[0],False,1)):
	print('opened port!')
else:
	print ('couldnt open port')
	exit()

sleep(1)
pack3D = pyof.OptoPackage( );

t1 = clock()
pack3Dlist = [];
while(not kbhit()):
	daq.read(pack3D,0,False)
	pack3Dlist.append(pack3D)
	sleep(0.01)
	print('x = ' + str(pack3D.x) + ' y = ' + str(pack3D.y) + ' z = '+ str(pack3D.z) +'\n')

t2 = clock()
print(t2 - t1)


daq.close()