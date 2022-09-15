#include <Servo.h>
Servo myservo;
int buzz=13;//indicates gas
int smoke = A0;//indicates sensor is connected to A0
int sensorThres=20;//The threshold value
int led_red=10;
int pir=2;

void setup()
{

pinMode(buzz,OUTPUT);
pinMode(led_red,OUTPUT);
pinMode(pir,INPUT);
myservo.attach(9);
pinMode(A0,INPUT);
Serial.begin(9600);
}

void loop()//loops
{

    //Gas detection   
int gas_value=analogRead(smoke);//reads sensor value
int dig_gas_val=map(gas_value,0,1023,0,255);
int val=digitalRead(pir);
Serial.println(val);
  
if (dig_gas_val > sensorThres)//sees if it reached threshold value
{

digitalWrite( buzz, HIGH);//turns on buzzer
tone(13,500);
digitalWrite(led_red,HIGH);
Serial.println("somke detected");
  
}
  
else//if it hasn't reached threshold value
{

digitalWrite( buzz, LOW);//turns buzzer off
Serial.println("somke not detected");
  
}
delay(100);//delay 0.1 sec
 
 
  //automatic door opening
if(val==HIGH)
{
  myservo.write(70);
}
 else
 {
   //digitalWrite(led,LOW);
   myservo.write(10);
 }
  delay(10);

}