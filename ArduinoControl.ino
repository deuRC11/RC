// 소프트웨어 시리얼을 이용해서 블루투스 초기세팅하는 소스
#include <SoftwareSerial.h> 
SoftwareSerial BT(2, 3); //Connect HC-06 TX,RX 

int IN1=7; //뒷바퀴모터 +극을 7번핀에 연결
int IN2=6; //뒷바퀴모터 -극을 6번핀에 연결
int IN3=5; //앞바퀴모터 +극을 5번핀에 연결
int IN4=4; //앞바퀴모터 -극을 4번핀에 연결

char blue; //블루투스 가져오는값
char inDat;//블루투스 가져온값을 넣는 변수
char outDat;

void setup()  
{
  Serial.begin(115200);//시리언모니터번호
  BT.begin(115200);//블루투스연결
  pinMode(IN1,OUTPUT); //뒷바퀴모터
  pinMode(IN2,OUTPUT); //뒷바퀴모터
  pinMode(IN3,OUTPUT); //앞바퀴모터
  pinMode(IN4,OUTPUT); //앞바퀴모터
  pinMode(8,OUTPUT); //뒷바퀴모터제어
  pinMode(9,OUTPUT); //앞바퀴모터제어
}

void loop()
{
  
  if (BT.available())
  {
    inDat = BT.read(); //블루투스에서 전송받은값을 inDat에 넣음
    Serial.write(BT.read()); //가져온값 확인
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

    Serial.println(inDat); //동일하게 값만드는지 확인
    Serial.println(blue); //쓰래기값이 나올때가있어서 수시로 동일하게 값을 만듬

    //직진
    if(blue == 'w'){
    motorA_Rotation(); //블루투스값이 w이면 motorA_Rotation 실행
    }
    //후진
    if(blue == 's'){
    motorA_Reverse(); //블루투스값이 s이면 motorA_Reverse 실행
    }
    //좌회전
    if(blue == 'a'){
    motorB_Rotation(); //블루투스값이 a이면 motorB_Rotation 실행
    }
    //우회전
    if(blue == 'd'){
    motorB_Reverse(); //블루투스값이 d이면 motorB_Reverse 실행
    }
    
    //정지
    if(blue == 'e'){
    stopMotor();    //블루투스값이 e이면 stopMotor 실행
    }

    //저속
    if(blue == 'q'){
    motorA_Rotation2();
    }
    delay(100);
}


//모터A 정회전, 모터B Stop 직진
void motorA_Rotation()
{
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,LOW);
    analogWrite(8, 200); //0~255
    analogWrite(9, 200); //0~255
}
//모터A 정회전, 모터B Stop 속도제어 test 
void motorA_Rotation2()
{
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,LOW);
    analogWrite(8, 100); //0~255
    analogWrite(9, 100); //0~255
}
//모터A 역회전, 모터B Stop 후진
void motorA_Reverse()
{
    digitalWrite(IN1,LOW);
    digitalWrite(IN2,HIGH);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,LOW);
    analogWrite(8, 200); //0~255
    analogWrite(9, 200); //0~255
}
 
//모터A Stop, 모터B 정회전  좌회전                                                  
void motorB_Rotation()
{
  //  digitalWrite(IN1,LOW);
  //  digitalWrite(IN2,LOW);
    digitalWrite(IN3,HIGH);                   
    digitalWrite(IN4,LOW);
    analogWrite(8, 200); //0~255
    analogWrite(9, 200); //0~255
}
 
//모터A Stop, 모터B 역회전 우회전
void motorB_Reverse()
{
  //  digitalWrite(IN1,LOW);
  //  digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,HIGH);
    analogWrite(8, 200); //0~255
    analogWrite(9, 200); //0~255
}
//모터A,B Stop 정지
void stopMotor()
{
    digitalWrite(IN1,LOW);
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,LOW);
}
