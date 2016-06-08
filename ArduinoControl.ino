// 소프트웨어 시리얼을 이용해서 블루투스 초기세팅하는 소스
#include <SoftwareSerial.h> 
SoftwareSerial BT(2, 3); //Connect HC-06 TX,RX 

//모터A 컨트롤
int IN1=7;
int IN2=6;
//모터B 컨트롤
int IN3=5;
int IN4=4;

char blue; //블루투스 가져오는값

void setup()  
{
  Serial.begin(115200);
  BT.begin(115200);//블루투스연결
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
}

void loop()
{
  char inDat;
  char outDat;
  
  if (BT.available())
  {
    inDat = BT.read();
    Serial.write(BT.read());
  }
  
  if (Serial.available())
  {
    outDat = Serial.read();
    BT.write(Serial.read());
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
    else if(inDat =='q')
    blue ='q';

    Serial.println(inDat);
    Serial.println(blue);

    //직진
    if(blue == 'w'){
    motorA_Rotation();
    }
    //후진
    if(blue == 's'){
    motorA_Reverse();
    }
    //좌회전
    if(blue == 'a'){
    motorB_Rotation();
    }
    //우회전
    if(blue == 'd'){
    motorB_Reverse();
    }
    
    //정지
    if(blue == 'e'){
    stopMotor();
    }

    //저속
    if(blue == 'q'){
    motorA_Rotation2();
    }

    delay(100);
}

//모터A,B Stop 정지
void stopMotor()
{
    digitalWrite(IN1,LOW);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,LOW);
}
 
 
//모터A 정회전, 모터B Stop 직진
void motorA_Rotation()
{
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,LOW);
}
//모터A 정회전, 모터B Stop 속도제어 test 
void motorA_Rotation2()
{
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,LOW);
    analogWrite(8, 20); //0~255
    analogWrite(9, 20); //0~255
    Serial.println("speed");
}
//모터A 역회전, 모터B Stop 후진
void motorA_Reverse()
{
    digitalWrite(IN1,LOW);
    digitalWrite(IN2,HIGH);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,LOW);
}
 
//모터A Stop, 모터B 정회전  좌회전                                                  
void motorB_Rotation()
{
 //   digitalWrite(IN1,LOW);
 //   digitalWrite(IN2,LOW);
    digitalWrite(IN3,HIGH);
    digitalWrite(IN4,LOW);
}
 
//모터A Stop, 모터B 역회전 우회전
void motorB_Reverse()
{
 //   digitalWrite(IN1,LOW);
 //   digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,HIGH);
}
