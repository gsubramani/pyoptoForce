import pyOptoForce as pyof
from time import sleep
from time import clock
from msvcrt import kbhit
ports = pyof.OptoPorts(3,1000000)
oportlist = ports.listPorts(True)
daq = pyof.OptoDAQ()
print(daq.open(oportlist[0],False,1000000))
print("hello" + str(ports.getSize(True)))

