import RPi.GPIO as GPIO
import time

en_pin = 11
//앞 모터
m1a_pin = 17
m1b_pin = 10
//뒤 모터
m2a_pin = 4
m2b_pin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(en_pin, GPIO.OUT)
GPIO.setup(m1a_pin, GPIO.OUT)
GPIO.setup(m1b_pin, GPIO.OUT)
pwm = GPIO.PWM(en_pin, 500)
pwm.start(0)

speed=50

while True:
    cmd = raw_input("Command, f/r :")
    direction = cmd[0]
//앞모터
    if direction == "q":
        print “1TF”
        GPIO.output(m1a_pin, True)
        GPIO.output(m1b_pin, False)
    elif direction == "w":
        print “1FT”
        GPIO.output(m1a_pin, False)
        GPIO.output(m1b_pin, True)
    elif direction == "e":
        print “1TT”
        GPIO.output(m1a_pin, True)
        GPIO.output(m1b_pin, True)
    elif direction == "r":
        print “1FF”
        GPIO.output(m1a_pin, False)
        GPIO.output(m1b_pin, False)
//뒷모터
    if direction == "a":
        print “2TF”
        GPIO.output(m2a_pin, True)
        GPIO.output(m2b_pin, False)
    elif direction == "s":
        print “2FT”
        GPIO.output(m2a_pin, False)
        GPIO.output(m2b_pin, True)
    elif direction == "d":
        print “2TT”
        GPIO.output(m2a_pin, True)
        GPIO.output(m2b_pin, True)
    elif direction == "f":
        print “2FF”
        GPIO.output(m2a_pin, False)
        GPIO.output(m2b_pin, False)

    print “speed=”, speed
    pwm.ChangeDutyCycle(abs(speed))
