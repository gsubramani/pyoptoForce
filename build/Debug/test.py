import pyOptoForce as pyof
from time import sleep
from time import clock
from msvcrt import kbhit
ports = pyof.OptoPorts(0,1000000)
portlist = ports.listPorts(True)
daq1 = pyof.OptoDAQ()
daq2 = pyof.OptoDAQ()
sleep(1)
portlist = ports.listPorts(True)
if(ports.getSize(True) == 2):
	portlist = ports.listPorts(True)
	if(daq2.open(portlist[1],False,1000000)):
		print('opened port!')

if(daq1.open(portlist[0],False,1000000)):
	print('opened port!')
else:
	print ('couldnt open port')
	exit()

sleep(0.1)
pack3D1 = pyof.OptoPackage( );
pack3D2 = pyof.OptoPackage( );
t1 = clock()
pack3Dlist1 = [];
pack3Dlist2 = [];
while(not kbhit()):
	daq1.read(pack3D1,0,False)
	daq2.read(pack3D2,0,False)
	pack3Dlist1.append(pack3D1)
	pack3Dlist2.append(pack3D2)
	sleep(0.01)
	print('x = ' + str(pack3D1.x) + ' y = ' + str(pack3D1.y) + ' z = '+ str(pack3D1.z))
	print(' x = ' + str(pack3D2.x) + ' y = ' + str(pack3D2.y) + ' z = '+ str(pack3D2.z) +'\n')

t2 = clock()
print(t2 - t1)
daq1.close()
daq2.close()