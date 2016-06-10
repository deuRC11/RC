import RPi.GPIO as gpio
import time

FRONT_GO = 23 #IC1,2EN
FRONT_DIR = 24 #IC1A
FRONT_EN = 18

DRIVE_GO = 22  #IC3A
DRIVE_DIR = 27 #IC3,4EN
DRIVE_EN = 17


def left():
    gpio.setmode(gpio.BCM)
    gpio.output(DRIVE_GO, gpio.LOW)
    gpio.output(DRIVE_DIR, gpio.HIGH)
def right():
    gpio.setmode(gpio.BCM)
    gpio.output(DRIVE_GO, gpio.HIGH)
    gpio.output(DRIVE_DIR, gpio.LOW)
def backward():
    gpio.setmode(gpio.BCM)
    gpio.output(FRONT_DIR, gpio.HIGH)
    gpio.output(FRONT_GO, gpio.LOW)
    gpio.output(DRIVE_GO, gpio.LOW)
    gpio.output(DRIVE_DIR, gpio.LOW)
def forward():
    gpio.setmode(gpio.BCM)
    gpio.output(FRONT_DIR, gpio.LOW)
    gpio.output(FRONT_GO, gpio.HIGH)
     gpio.output(DRIVE_GO, gpio.LOW)
    gpio.output(DRIVE_DIR, gpio.LOW)
def stop():
    gpio.setmode(gpio.BCM)
    gpio.output(FRONT_GO, gpio.LOW)
    gpio.output(FRONT_DIR, gpio.LOW)
    gpio.output(DRIVE_GO, gpio.LOW)
    gpio.output(DRIVE_DIR, gpio.LOW)

def initMotors():
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
pwm = gpio.PWM(FRONT_EN,500)
pwm2 = gpio.PWM(DRIVE_EN,500)
pwm.start(100)
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


                            
