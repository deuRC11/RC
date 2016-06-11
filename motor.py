import RPi.GPIO as gpio
import time

FRONT_GO = 23 # rc카의 직진방향 제어를 위한 핀
FRONT_DIR = 24 # rc카의 후진방향 제어를 위한 핀
FRONT_EN = 18 # rc카 모터 속도조절을 위한 핀

DRIVE_GO = 22  # rc카의 좌방향 제어를 위한 핀
DRIVE_DIR = 27 # rc카의 우방향 제어를 위한 핀
DRIVE_EN = 17 # rc카 모터 속도조절을 위한 핀


def left(): # 좌방향
    gpio.setmode(gpio.BCM)
    gpio.output(DRIVE_GO, gpio.LOW)
    gpio.output(DRIVE_DIR, gpio.HIGH)
def right(): # 우방향
    gpio.setmode(gpio.BCM)
    gpio.output(DRIVE_GO, gpio.HIGH)
    gpio.output(DRIVE_DIR, gpio.LOW)
def backward(): # 후진
    gpio.setmode(gpio.BCM)
    gpio.output(FRONT_DIR, gpio.HIGH)
    gpio.output(FRONT_GO, gpio.LOW)
    gpio.output(DRIVE_GO, gpio.LOW)
    gpio.output(DRIVE_DIR, gpio.LOW)
def forward(): # 직진
    gpio.setmode(gpio.BCM)
    gpio.output(FRONT_DIR, gpio.LOW)
    gpio.output(FRONT_GO, gpio.HIGH)
     gpio.output(DRIVE_GO, gpio.LOW)
    gpio.output(DRIVE_DIR, gpio.LOW)
def stop(): # 정지
    gpio.setmode(gpio.BCM)
    gpio.output(FRONT_GO, gpio.LOW)
    gpio.output(FRONT_DIR, gpio.LOW)
    gpio.output(DRIVE_GO, gpio.LOW)
    gpio.output(DRIVE_DIR, gpio.LOW)

def initMotors(): # GPIO 실행을 위한 GPIO 셋업 함수
    gpio.setwarnings(False)
    gpio.setmode( gpio.BCM )
    gpio.setup(FRONT_GO, gpio.OUT)
    gpio.setup(FRONT_DIR, gpio.OUT)
    gpio.setup(DRIVE_GO, gpio.OUT)
    gpio.setup(DRIVE_DIR, gpio.OUT)
    gpio.output(FRONT_GO, gpio.LOW)
    gpio.output(FRONT_DIR, gpio.LOW)
    gpio.output(DRIVE_GO, gpio.LOW)
    gpio.output(DRIVE_DIR, gpio.LOW)

initMotors()
gpio.setup(FRONT_EN, gpio.OUT)
gpio.setup(DRIVE_EN, gpio.OUT)
pwm = gpio.PWM(FRONT_EN,500) # 앞뒤 방향 모터 속도값 설정
pwm2 = gpio.PWM(DRIVE_EN,500) # 좌우 방향 모터 속도값 설정
pwm.start(100) # pwm 시작
pwm2.start(100) 

#forward()
#time.sleep(2)
#backward()
#time.sleep(2)
#backward()
#time.sleep(2)
#left()
#time.sleep(2)
#right()
#3time.sleep(2)
#stop()


                            
