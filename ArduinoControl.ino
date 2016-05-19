#include <MeOrion.h>
#include <Arduino.h>
#include <SoftwareSerial.h>
#include <Wire.h>


MeBluetooth bluetooth(PORT_4);
MeDCMotor motor_9(9);
MeDCMotor motor_10(10);

char blue;


void setup() {
  Serial.begin(115200);
  bluetooth.begin(115200);
  pinMode(13, OUTPUT);
  Serial.println("Bluetooth Start!");
}

void loop() {
  //블루투스 값 가져옴
    char inDat;
    char outDat;
    if(bluetooth.available())
    {
        inDat = bluetooth.read();
        Serial.println(inDat);
    }
    if(Serial.available())
    {
        outDat = Serial.read();
        bluetooth.write(outDat);
    }

//블루투스 가져온값을 아두이노 변수값을 동일하게만들어줌
    if(inDat =='e')
    blue ='e';
    else if(inDat =='w')
    blue ='w';
    else if(inDat =='a')
    blue ='a';
    else if(inDat =='s')
    blue ='s';
    else if(inDat =='d')
    blue ='d';

    

    Serial.println(inDat);
    Serial.println(blue);
    //motor_9.run(-50);
    //motor_10.run(50);

    //직진
    if(blue == 'w'){
    motor_9.run(-50);
    motor_10.run(50);
    }
    //후진
    if(blue == 's'){
    motor_9.run(50);
    motor_10.run(-50);
    }
    //좌회전
    if(blue == 'a'){
    motor_9.run(50);
    motor_10.run(50);
    }
    //우회전
    if(blue == 'd'){
    motor_9.run(-50);
    motor_10.run(-50);
    }
    
    //정지
    if(blue == 'e'){
    motor_9.run(0);
    motor_10.run(0);
    }

    delay(100);
}
