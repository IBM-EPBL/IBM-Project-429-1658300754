import random #Importing random module
import time #Importing time module
temperature_threshold=int(input("enter the threshold value of temperature"))#Obtaining the temperature threshold value
humidity_threshold=int(input("enter the humidity threshold range")) #Obtaining the humidity threshold value
humidity_alarm=0 #Initializing the Humidity_alarm value as 0
fire_alarm=0     #Initializing the Fire_alarm value as 0
while(True):     #Continously generate temp and humidity value and set the value of alarms accordingly and display the information 
    temperature=random.uniform(10,100) #generating random temperature value 
    humidity=random.uniform(1,50)      #generating random humidity percentage
    print("current temperature value is {0:.2f}".format(temperature)) #Display the current temperature value 
    print("current humidity value is {0:.2f} %".format(humidity)) #Display the current humidity value
    time.sleep(1)
    if(temperature>=temperature_threshold and humidity<=humidity_threshold):
        fire_alarm=1      #Fire alarm is set to 1(ON)
        humidity_alarm=1  #Humidity alarm is Set to 1(ON)
        print("Fire alarm and Hudimidity alarm is ON \n")
        time.sleep(2) 
  
    elif (humidity<=humidity_threshold):
        humidity_alarm=1  #Humidity alarm is Set to 1(ON)
        fire_alarm=0      #Fire alarm is set to 0(OFF)
        print("Humidity alarm is ON and Fire alarm is OFF \n")
        time.sleep(2)
    elif(temperature>=temperature_threshold):
        humidity_alarm=0  #Humidity alarm is Set to 0(OFF)
        fire_alarm=1      #Fire alarm is set to 1(ON)
        print("Humidity alarm is OFF and Fire alarm is ON \n")
        time.sleep(2)
    else:
        humidity_alarm=0  #Humidity alarm is Set to 0(OFF)
        fire_alarm=0      #Fire alarm is set to 0(OFF)
        print("Both alarms are OFF \n")
        time.sleep(2)
 
