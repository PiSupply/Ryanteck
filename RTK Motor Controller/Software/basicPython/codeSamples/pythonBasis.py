#RTK-000-001 Python Basis
#Licensed under the GNU GPL V3 License
#(C) Pi Supply 2018
#Contributors: Ryan Walmsley, Michael Horne
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor1a = 17
motor1b = 18
motor2a = 22
motor2b = 23

GPIO.setup(motor1a,GPIO.OUT)
GPIO.setup(motor1b,GPIO.OUT)
GPIO.setup(motor2a,GPIO.OUT)
GPIO.setup(motor2b,GPIO.OUT)

def forwards():
    GPIO.output(motor1a,1)
    GPIO.output(motor1b,0)
    GPIO.output(motor2a,1)
    GPIO.output(motor2b,0)

def backwards():
    GPIO.output(motor1a,0)
    GPIO.output(motor1b,1)
    GPIO.output(motor2a,0)
    GPIO.output(motor2b,1)

def left():
    GPIO.output(motor1a,0)
    GPIO.output(motor1b,1)
    GPIO.output(motor2a,1)
    GPIO.output(motor2b,0)

def right():
    GPIO.output(motor1a,1)
    GPIO.output(motor1b,0)
    GPIO.output(motor2a,0)
    GPIO.output(motor2b,1)

def stop():
    GPIO.output(motor1a,0)
    GPIO.output(motor1b,0)
    GPIO.output(motor2a,0)
    GPIO.output(motor2b,0)
