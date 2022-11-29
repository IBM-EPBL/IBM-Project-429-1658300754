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
	mydata={'name':'Train1','lat':17.6387448,'lon':78.4754336}
	pub(mydata)
	time.sleep(5)
	mydata={'name':'Train1','lat':17.6341908,'lon':78.4744722}
	pub(mydata)
	time.sleep(5)
	mydata={'name':'Train1','lat':17.6340889,'lon':78.4745052}
	pub(mydata)
	time.sleep(5)
	mydata={'name':'Train1','lat':17.6248626,'lon':78.4720259}
	pub(mydata)
	time.sleep(5)
	mydata={'name':'Train1','lat':17.6248626,'lon':78.47202259}
	pub(mydata)
	time.sleep(5)
	mydata={'name':'Train1','lat':17.6188577,'lon':78.4698726}
	pub(mydata)
	time.sleep(5)
	client.commandCallback=myCommandCallback
client.disconnect()
#apikey  a-sw0rr5-qucajgda23
#api token   StQE8(uMve+86b2OeN
