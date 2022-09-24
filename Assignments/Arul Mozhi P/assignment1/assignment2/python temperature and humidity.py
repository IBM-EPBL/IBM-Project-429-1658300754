from random import uniform
import time

tempThresh=int(input("Enter temperature threshold:"))
humidThresh=int(input("Enter humidity threshold range:")) 
humidAlarm=0 
fireAlarm=0

while(True):     
    temperature=uniform(1,75) 
    humidity=uniform(1,50)      
    print("current temperature {0:.2f}: ".format(temperature))
    print("current humidity {0:.2f} %: ".format(humidity))
    time.sleep(1)
    if(temperature>=tempThresh and humidity<=humidThresh):
        fire_alarm=1     
        humidAlarm=1      
        print("Fire and Hudimidity alarm is ON \n")
        time.sleep(2) 
  
    elif (humidity<=humidThresh):
          
        fireAlarm=0
        humidAlarm=1
        print("Fire alarm is OFF and humidity alarm is ON \n")
        time.sleep(2)
    elif(temperature>=tempThresh):
      
        fireAlarm=1
        humidAlarm=0
        print("Fire alarm is ON and humid alarm is OFF\n")
        time.sleep(2)
    else:
        humidAlarm=0  
        fireAlarm=0      
        print("Fire and humid alarms are OFF \n")
        time.sleep(2)



