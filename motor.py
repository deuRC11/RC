// 모터 작동 테스트

import RPi.GPIO as gpio
import time

FRONT_DIR = 25 #IC1A
FRONT_GO = 10 #IC1,2EN

DRIVE_GO = 17 #IC3A
DRIVE_DIR = 4 #IC3,4EN

def right():
    gpio.setmode(gpio.BCM)
    gpio.output(DRIVE_GO, gpio.HIGH)
    gpio.output(DRIVE_DIR, gpio.HIGH)
def left():
    gpio.setmode(gpio.BCM)
    gpio.output(DRIVE_GO, gpio.HIGH)
    gpio.output(DRIVE_DIR, gpio.LOW)
def backward():
    gpio.setmode(gpio.BCM)
    gpio.output(FRONT_DIR, gpio.HIGH)
    gpio.output(FRONT_GO, gpio.HIGH)
def forward():
    gpio.setmode(gpio.BCM)
    gpio.output(FRONT_DIR, gpio.LOW)
    gpio.output(FRONT_GO, gpio.HIGH)
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
forward()
time.sleep(2)
backward()
time.sleep(2)
left()
time.sleep(2)
right()
time.sleep(2)
stop()

