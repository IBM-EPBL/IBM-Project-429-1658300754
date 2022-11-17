import wiotp.sdk.device
import time
import random
myconfig={
    "identity": {
        "orgId":"sw0rr5",
        "typeId":"GPS",
        "deviceId":"Train1"
    },
    "auth": {
        "token":"kYH!(2sM47Cm-&0!h7"
    }
}


def myCommandCallback(cmd):
	print("Message from IBM IoT platform: %s"% cmd.data['command'])
	m=cmd.data['command']
client=wiotp.sdk.device.DeviceClient(config=myconfig,logHandlers=None)
client.connect()
def pub(data):
	client.publishEvent(eventId="status",msgFormat="json",data=mydata,qos=0,onPublish=None)
	print("Data sent Sucessfully :",mydata)
while True:
	mydata={'name':'Train1','lat':12.951604,'lon':80.141067}
	pub(mydata)
	time.sleep(5)
	mydata={'name':'Train1','lat':12.951327,'lon':80.140869}
	pub(mydata)
	time.sleep(5)
	mydata={'name':'Train1','lat':12.950871,'lon':80.140530}
	pub(mydata)
	time.sleep(5)
	mydata={'name':'Train1','lat':12.950052,'lon':80.139915}
	pub(mydata)
	time.sleep(5)
	mydata={'name':'Train1','lat':12.949189,'lon':80.139297}
	pub(mydata)
	time.sleep(5)
	mydata={'name':'Train1','lat':12.948667,'lon':80.138973}
	pub(mydata)
	time.sleep(5)
	client.commandCallback=myCommandCallback
client.disconnect()

