import clr
import USDigital as usd
import USDQSB as qsb
from msvcrt import kbhit
import pyOptoForce as pyof
from time import sleep, clock
from Multimedia import Timer
t0 = 0
dumpList = []
def timerStep(forceSensors):
	#print readOptoForce(forceSensors), encoderCount(mQSB)
	op = readOptoForce(forceSensors)
	global t0
	global dumpList
	t1 = clock()
	dumpList.append([t1 - t0,t1,op])
	t0 = t1
	
	#print(encoderCount(mQSB))
	#print(readOptoForce(forceSensors))	
	

def pyOptoForceInit():
	ports = pyof.OptoPorts(0,1000000)
	portlist = ports.listPorts(True)
	daq1 = pyof.OptoDAQ()
	daq2 = pyof.OptoDAQ()
	sleep(0.1)
	portlist = ports.listPorts(True)
	if(ports.getSize(True) == 2):
		portlist = ports.listPorts(True)
		if(daq2.open(portlist[1],False,1000000)):
			config2 = daq2.getConfig()
			config2.setSpeed(1000)
			#config2.setMode(1)
			
			print 'config was' + str(daq2.sendConfig(config2))
			print('opened port 2!')

	if(daq1.open(portlist[0],False,1000000)):
		config1 = daq1.getConfig()
		config1.setSpeed(1000)
		#config1.setMode(1)
		print 'config was' + str(daq1.sendConfig(config1))
		print('opened port 1!')
	else:
		print ('couldnt open port')
		return NULL
	forceSensors = lambda:0;
	forceSensors.daq1 = daq1;
	forceSensors.daq2 = daq2;
	return forceSensors;

def readOptoForce(forceSensors):
	pack3D1 = pyof.OptoPackage( );
	pack3D2 = pyof.OptoPackage( );

	while(not pack3D1.isCorrect()):
		forceSensors.daq1.read(pack3D1,0,True)
	forceSensors.daq1.read(pack3D1,0,False)
	
	#while(pack3D2.isCorrect()):
	#	forceSensors.daq2.read(pack3D2,0,True)
	#forceSensors.daq2.read(pack3D2,0,False)
	
	
	return [pack3D1.x, 
			pack3D1.y, 
			pack3D1.z, 
			pack3D2.x, 
			pack3D2.y, 
			pack3D2.z],[pack3D1.isCorrect(),pack3D2.isCorrect()]

def closeOptoForce(forceSensors):
	forceSensors.daq1.close()
	forceSensors.daq2.close()
	

def  encoderInit(reset = False):
	#mQSB = usd.QSB_S('COM6',115200)
	mQSB = usd.QSB_D()
	mQSB.Open('COM6')
	#mQSB.Reset()
	mQSB.StreamEncoderCount(1,20)
	#mQSB.StreamRegister(14)
	print mQSB.GetStreamingIntervalRate()
	if(reset == True):
		mQSB.ResetCount()
	mQSB.SetIndexConfiguration(2)	# on index pulse resets counter
	#mQSB.SetTriggerOnIndex(False)	# so triggers are set on index pulse
	return mQSB
def encoderClose(mQSB):
	mQSB.Close()

def encoderCount(mQSB):
	return mQSB.GetCount()
	
	

	
	
if __name__ == "__main__":
	forceSensors = pyOptoForceInit();
	#mQSB = encoderInit()
	timer = Timer()
	timer.Period = 5; # milisecond period 
	timer.Start()
	
	timer.Tick += lambda arg1, arg2 : timerStep(forceSensors)
	
	while(not kbhit()):
		#print(encoderCount(mQSB))
		#optodata,validity = readOptoForce(forceSensors)
		#if True:#(validity[1] and validity[0]):
		#	print optodata
		#	t = clock()
		#	print t - t0
		#	t0 = t
		pass
		
	#encoderClose(mQSB)
	timer.Stop()
	closeOptoForce(forceSensors)
	print dumpList
	